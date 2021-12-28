const X_ADD: [i128; 14] = [12,11,13,11,14, -10,11,-9,-3,13, -5,-10,-4,-5];
const Y_ADD: [i128; 14] = [4,11,5,11,14, 7,11,4,6,5, 9, 12,14,14];
const Z_DIV: [i128; 14] = [1,1,1,1,1,26,1,26,26,1,26,26,26,26];

fn solve(mut z: i128, s: String) -> Option<String> {
    if Z_DIV.iter().fold(1, |lhs, rhs| lhs * rhs) <= z {
        return Option::None;
    }

    let i = s.len() - 1;
    let w: i128 = s[i..i+1].parse().unwrap();

    if Z_DIV[i] == 26 && !((z % 26) + X_ADD[i] == w) {
        return Option::None; 
    }

    if (z % 26) + X_ADD[i] == w {
        z /= Z_DIV[i];
    } else {
        z /= Z_DIV[i];
        z *= 26;
        z += w + Y_ADD[i];
    }

    if s.len() == 14 {
        if z == 0 {
            return Option::Some(s);
        } else {
            return Option::None;
        }
    }

    // for ww in 1..10 { // part 2
    for ww in (1..10).rev() {
        let ss = format!("{}{}", s, ww);
        if let Some(s) = solve(z, ss) {
            return Some(s);
        }
    }

    Option::None
}

fn do_solve() -> Option<String> {
    // for s in 1..10 { // part 2
    for s in (1..10).rev() {
        match solve(0, s.to_string()) {
            Some(out) => return Some(out),
            None => (),
        }
    }

    None
}

fn main() {
    match do_solve() {
        Some(s) => println!("{}", s),
        None => println!("No solution..."),
    };
}
