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

    let mut counts:Vec<u32> = Vec::new();

    let times = lines[0].split(':').collect::<Vec<&str>>()[1].chars().filter(|&num| num != ' ').collect::<Vec<char>>().iter().collect::<String>().parse::<u64>().unwrap();
    let distances = lines[1].split(':').collect::<Vec<&str>>()[1].chars().filter(|&num| num != ' ').collect::<Vec<char>>().iter().collect::<String>().parse::<u64>().unwrap();

 
    let mut count = 0;
    for hold in 0..times {
        let travel = (times - hold) * hold;
        if travel > distances {
            count += 1;
        }
    }
    counts.push(count);
    

    let mut res = 1;
    for i in 0..counts.len() {
        res *= counts[i];
    }



    println!("{}", res);
}