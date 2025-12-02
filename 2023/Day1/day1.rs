use std::fs;

fn main_part1() {
    let file_path = "input.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut sum = 0;
    let lines = contents.split('\n');
    for line in lines {
        let (mut l, mut r) = (-1i32, -1i32);
        for c in line.chars() {
            let val = c as i32 - '0' as i32;
            if c.is_digit(10) {
                if l == -1 {
                    l = val;
                }
                r = val;
            }

        }
        sum += l * 10 + r;
    }

    println!("{}", sum)

}

fn main() {
    let file_path = "input.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let mut sum = 0;
    let lines = contents.split('\n');
    for line in lines {
        let (mut l, mut r) = (-1i32, -1i32);
        
        for (i, c) in line.char_indices() {
            for j in 0.. digits.len() {
                let digit = digits[j];
                if i + digit.len() <= line.len() && line[i..(i + digit.len())] == *digit {
                    if l == -1 {
                        l = j as i32;
                    }
                    r = j as i32; 
                }
            }
            let val = c as i32 - '0' as i32;
            if c.is_digit(10) {
                if l == -1 {
                    l = val;
                }
                r = val;
            }
        }
        sum += l * 10 + r;
    }

    println!("{}", sum)

}