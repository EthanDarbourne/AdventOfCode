use std::fs::read_to_string;
use std::cmp;


fn main() {



    let lines:Vec<Vec<char>> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(
            |x| x.chars()
            .collect::<Vec<char>>())
        .collect();


    // find S

    // replace S with each of the 4 pipe types and see if you can make a loop
    // choose distance / 2

    let x = lines
    .iter()
    .enumerate()
    .filter(|&r| (*(r.1)).iter().cloned().collect::<Vec<char>>().iter().any(|&d| d  == 'S')).collect::<Vec<(usize, &Vec<char>)>>()[0].0;
    let y = lines[x].iter().enumerate().find(|&r| *(r.1) == 'S').unwrap().0 as usize;

    println!("{} {}", x, y);

    let mut res = 0;
    res = cmp::max(res, ReplacePipe(lines, 'F', x, y));
    res = cmp::max(res, ReplacePipe(lines, 'L', x, y));
    res = cmp::max(res, ReplacePipe(lines, 'J', x, y));
    res = cmp::max(res, ReplacePipe(lines, '7', x, y));
}