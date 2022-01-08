use std::cmp::{max, min};
use std::fs;

type Point = [i64; 3];
const X: usize = 0;
const Y: usize = 1;
const Z: usize = 2;
type Cuboid = [Point; 2];

fn intersect(c0: &Cuboid, c1: &Cuboid) -> Option<Cuboid> {
    let x0 = max(c0[0][X], c1[0][X]);
    let x1 = min(c0[1][X], c1[1][X]);
    let y0 = max(c0[0][Y], c1[0][Y]);
    let y1 = min(c0[1][Y], c1[1][Y]);
    let z0 = max(c0[0][Z], c1[0][Z]);
    let z1 = min(c0[1][Z], c1[1][Z]);

    if x0 < x1 && y0 < y1 && z0 < z1 {
        return Some([[x0, y0, z0], [x1, y1, z1]]);
    }

    None
}

fn cut_away_intersect(c0: &Cuboid, c1: &Cuboid) -> Vec<Cuboid> {
    let mut res: Vec<Cuboid> = Vec::new();

    // A
    if c1[0][X] > c0[0][X] {
        let c = [
            [c0[0][X], c0[0][Y], c0[0][Z]],
            [c1[0][X], c0[1][Y], c0[1][Z]],
        ];
        res.push(c);
    }

    // B
    if c1[1][X] < c0[1][X] {
        let c = [
            [c1[1][X], c0[0][Y], c0[0][Z]],
            [c0[1][X], c0[1][Y], c0[1][Z]],
        ];
        res.push(c);
    }

    // C
    if c1[1][Y] < c0[1][Y] {
        let c = [
            [c1[0][X], c1[1][Y], c0[0][Z]],
            [c1[1][X], c0[1][Y], c0[1][Z]],
        ];
        res.push(c);
    }

    // D
    if c0[0][Y] < c1[0][Y] {
        let c = [
            [c1[0][X], c0[0][Y], c0[0][Z]],
            [c1[1][X], c1[0][Y], c0[1][Z]],
        ];
        res.push(c);
    }

    // E
    if c0[0][Z] < c1[0][Z] {
        let c = [
            [c1[0][X], c1[0][Y], c0[0][Z]],
            [c1[1][X], c1[1][Y], c1[0][Z]],
        ];
        res.push(c);
    }

    // F
    if c1[1][Z] < c0[1][Z] {
        let c = [
            [c1[0][X], c1[0][Y], c1[1][Z]],
            [c1[1][X], c1[1][Y], c0[1][Z]],
        ];
        res.push(c);
    }

    res
}

fn sum_cubes(cuboids: &Vec<Cuboid>) -> u128 {
    let mut sum: u128 = 0;
    for &c in cuboids {
        let dx = c[1][X] - c[0][X];
        let dy = c[1][Y] - c[0][Y];
        let dz = c[1][Z] - c[0][Z];
        sum += (dx * dy * dz) as u128;
    }

    sum
}

fn main() {
    let mut cuboids: Vec<(bool, Cuboid)> = Vec::new();
    let input_str = fs::read_to_string("input22").unwrap();
    for line in input_str.lines() {
        let x_idx = line.find("x=").unwrap();
        let x0_start = x_idx + 2;
        let x0_end = x_idx + line[x_idx..].find("..").unwrap();
        let x1_start = x0_end + 2;
        let x1_end = x_idx + line[x_idx..].find(",").unwrap();

        let x0: i64 = line[x0_start..x0_end].parse().unwrap();
        let x1: i64 = line[x1_start..x1_end].parse::<i64>().unwrap() + 1;

        let y_idx = line.find("y=").unwrap();
        let y0_start = y_idx + 2;
        let y0_end = y_idx + line[y_idx..].find("..").unwrap();
        let y1_start = y0_end + 2;
        let y1_end = y_idx + line[y_idx..].find(",").unwrap();

        let y0: i64 = line[y0_start..y0_end].parse().unwrap();
        let y1: i64 = line[y1_start..y1_end].parse::<i64>().unwrap() + 1;

        let z_idx = line.find("z=").unwrap();
        let z0_start = z_idx + 2;
        let z0_end = z_idx + line[z_idx..].find("..").unwrap();
        let z1_start = z0_end + 2;
        let z1_end = line.len();

        let z0: i64 = line[z0_start..z0_end].parse().unwrap();
        let z1: i64 = line[z1_start..z1_end].parse::<i64>().unwrap() + 1;

        let mut val = false;
        if line.starts_with("on") {
            val = true;
        }

        let c = [[x0, y0, z0], [x1, y1, z1]];
        cuboids.push((val, c))
    }

    let mut res: Vec<Cuboid> = Vec::new();
    for &(v, c1) in &cuboids {
        if res.is_empty() {
            if v {
                res.push(c1);
            }
        } else {
            let mut new_res: Vec<Cuboid> = Vec::new();
            for &c0 in &res {
                match intersect(&c0, &c1) {
                    Some(c_intersect) => {
                        let split_cuboids: Vec<Cuboid> = cut_away_intersect(&c0, &c_intersect);
                        new_res.extend(split_cuboids);
                    },
                    None => new_res.push(c0),
                }
            }
            if v {
                new_res.push(c1);
            }
            res = new_res;
        }
    }

    println!("{}", sum_cubes(&res));
}