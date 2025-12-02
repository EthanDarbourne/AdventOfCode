use std::fs;

fn main_part1() {
    let file_path = "input.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut sum = 0;
    let lines = contents.split('\n');
    for line in lines {


        let gamesList = line.split(':');
        let games = line.split(';');
        let (mut l, mut r) = (-1i32, -1i32);
        for game in games {
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