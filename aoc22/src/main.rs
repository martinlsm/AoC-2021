use std::cmp::{max, min};
use std::fs;

fn set_cubiod(
    matrix: &mut [[[bool; 101]; 101]; 101],
    val: bool,
    x0: i64,
    x1: i64,
    y0: i64,
    y1: i64,
    z0: i64,
    z1: i64,
) {
    for x in max(-50, x0) + 50..min(50, x1) + 51 {
        for y in max(-50, y0) + 50..min(50, y1) + 51 {
            for z in max(-50, z0) + 50..min(50, z1) + 51 {
                matrix[x as usize][y as usize][z as usize] = val;
            }
        }
    }
}

fn main() {
    let mut matrix: [[[bool; 101]; 101]; 101] = [[[false; 101]; 101]; 101];

    let input_str = fs::read_to_string("input22").unwrap();
    for line in input_str.lines() {
        let x_idx = line.find("x=").unwrap();
        let x0_start = x_idx + 2;
        let x0_end = x_idx + line[x_idx..].find("..").unwrap();
        let x1_start = x0_end + 2;
        let x1_end = x_idx + line[x_idx..].find(",").unwrap();

        let x0: i64 = line[x0_start..x0_end].parse().unwrap();
        let x1: i64 = line[x1_start..x1_end].parse().unwrap();

        let y_idx = line.find("y=").unwrap();
        let y0_start = y_idx + 2;
        let y0_end = y_idx + line[y_idx..].find("..").unwrap();
        let y1_start = y0_end + 2;
        let y1_end = y_idx + line[y_idx..].find(",").unwrap();

        let y0: i64 = line[y0_start..y0_end].parse().unwrap();
        let y1: i64 = line[y1_start..y1_end].parse().unwrap();

        let z_idx = line.find("z=").unwrap();
        let z0_start = z_idx + 2;
        let z0_end = z_idx + line[z_idx..].find("..").unwrap();
        let z1_start = z0_end + 2;
        let z1_end = line.len();

        let z0: i64 = line[z0_start..z0_end].parse().unwrap();
        let z1: i64 = line[z1_start..z1_end].parse().unwrap();

        let mut val = false;
        if line.starts_with("on") {
            val = true;
        }

        set_cubiod(&mut matrix, val, x0, x1, y0, y1, z0, z1);
    }

    let mut sum: u64 = 0;
    for &d0 in matrix.iter() {
        for &d1 in d0.iter() {
            for &val in d1.iter() {
                if val {
                    sum += 1;
                }
            }
        }
    }

    println!("{}", sum);
}
