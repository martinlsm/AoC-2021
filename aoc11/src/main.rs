use std::cmp::{max, min};
use std::collections::VecDeque;
use std::fs;

fn push_to_neighbours(
    incr_q: &mut VecDeque<(usize, usize)>,
    row: i32,
    col: i32,
    height: i32,
    width: i32,
) {
    for rn in max(0, row - 1)..min(height, row + 2) {
        for cn in max(0, col - 1)..min(width, col + 2) {
            if (rn, cn) == (row, col) {
                continue;
            }

            incr_q.push_back((rn as usize, cn as usize));
        }
    }
}

fn main() {
    // Parse matrix.
    let lines: String = fs::read_to_string("input11").unwrap();
    let lines = lines.lines();
    let mut matrix: Vec<Vec<u8>> = Vec::new();

    for line in lines {
        let mut row = Vec::new();
        for c in line.chars() {
            row.push(c.to_digit(10).unwrap() as u8);
        }
        matrix.push(row);
    }

    let height = matrix.len();
    let width = matrix[0].len();

    let mut total_flashes: u64 = 0;

    for i in 1.. {
        // Push all octopuses for incrementing.
        let mut incr_q: VecDeque<(usize, usize)> = VecDeque::new();
        for r in 0..height {
            for c in 0..width {
                incr_q.push_back((r, c));
            }
        }

        // Process queue.
        while !incr_q.is_empty() {
            let (r, c) = incr_q.pop_front().unwrap();
            matrix[r][c] += 1;
            if matrix[r][c] == 10 {
                push_to_neighbours(&mut incr_q, r as i32, c as i32, height as i32, width as i32);
            }
        }

        // Reset flashed octopuses.
        let mut round_flashes = 0;
        for r in 0..height {
            for c in 0..width {
                if matrix[r][c] >= 10 {
                    matrix[r][c] = 0;
                    round_flashes += 1;
                }
            }
        }

        total_flashes += round_flashes;
        println!(
            "Round {}: {} round flashes, {} total flashes",
            i, round_flashes, total_flashes
        );

        if round_flashes == (height * width) as u64 {
            break;
        }
    }
}
