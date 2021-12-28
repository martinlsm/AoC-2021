use std::thread;

const X_ADD: [i128; 14] = [12,11,13,11,14, -10,11,-9,-3,13, -5,-10,-4,-5];
const Y_ADD: [i128; 14] = [4,11,5,11,14, 7,11,4,6,5, 9, 12,14,14];
const Z_DIV: [i128; 14] = [1,1,1,1,1,26,1,26,26,1,26,26,26,26];

fn run_python(inp_str: &str) -> i128 {
    let mut z: i128 = 0;
    let count: usize = 14;

    for i in 0..count {
        let w: i128 = inp_str[i..i+1].parse().unwrap();

        if (z % 26) + X_ADD[i] == w {
            z /= Z_DIV[i];
        } else {
            z /= Z_DIV[i];
            z *= 26;
            z += w + Y_ADD[i];
        }
    }

    z
}

fn solve(mut z: i128, s: String) -> Option<String> {
    if s.len() == 2 {
        println!("{}XXXXXXXXXXXX", s);
    }

    if s.len() == 14 {
        if z == 0 {
            return Option::Some(s);
        } else {
            return Option::None;
        }
    }

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

    for ww in ["9","8","7","6","5","4","3","2","1"].iter() {
        let ss = format!("{}{}", s, ww);
        match solve(z, ss) {
            Some(s) => return Some(s),
            None => (),
        }
    }

    Option::None
}

fn do_solve(begin: usize, end: usize) -> Option<String> {
    let space = ["9","8","7","6","5","4","3","2","1"];
    for s in space[begin..end].iter() {
        match solve(0, s.to_string()) {
            Some(s) => return Some(s),
            None => (),
        }
    }

    None
}

fn main() {
    let inp_str = String::from("12312312312311");
    let py_res = run_python(&inp_str);
    println!("z = {}", py_res);

    let mut threads = Vec::new();
    for i in 0..9 {
        let thrd = thread::spawn(move || {
            match do_solve(i, i+1) {
                Some(s) => println!("Solution found: {}", s),
                None => println!("No solution..."),
            }
        });
        threads.push(thrd);
    }

    for thrd in threads {
        thrd.join().unwrap();
    }
}
