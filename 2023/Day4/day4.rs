use std::fs;
use std::fs::read_to_string;
use std::cmp;

fn main() {
   
    let lines:Vec<String> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(|x| x.to_string())
        .collect();



    let n: usize = lines.len(); 
    let m: usize = lines[0].len();

    let mut total_score = 0;

    let mut copies = vec![1; n];
    let mut index: usize = 0;
    for line in lines {
        let game = line.split(':').collect::<Vec<&str>>();
        let numbers = game[1].split('|').collect::<Vec<&str>>();

        let right_nums = numbers[0].split(' ').filter(|num| num.len() > 0).map(|x| x.parse::<i32>().unwrap() ).collect::<Vec<i32>>();
        let guess_nums = numbers[1].split(' ').filter(|num| num.len() > 0).map(|x| x.parse::<i32>().unwrap() ).collect::<Vec<i32>>();

        let mut card_score = 0;
        for num in guess_nums {
            if right_nums.iter().any(|&x| x == num) {
                card_score += 1;
            }
        }
        if card_score > 0 {
            total_score += i32::pow(2, card_score - 1) * copies[index];
            for i in 1..card_score + 1 {
                copies[index + i as usize] += copies[index];
            }
        }
        println!("Copies: {}, {}, {}", copies[index], card_score, total_score);
        

        index += 1;
    }
    println!("{}", copies.iter().map(|&i| i as u32).sum::<u32>());
}