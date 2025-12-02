use std::fs;
use std::fs::read_to_string;

fn main() {
   
    let chars:Vec<Vec<char>> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(
            |x| x.chars()
            .collect::<Vec<char>>())
        .collect();
    let n: usize = chars.len(); 
    let m: usize = chars[0].len();
    let mut gears: Vec<Vec<i32>> = vec![vec![0; m]; n];
    let mut gearsAdd: Vec<Vec<bool>> = vec![vec![false; m]; n];
    let mut sum = 0;
    println!("{}:{}", n, m);
    // println!("{}:{}", chars.len(), chars[139].len());

    for i in 0..n {
        let mut cur = 0;
        let mut is_part = false;
        let mut rows: Vec<usize> = Vec::new();
        let mut cols: Vec<usize> = Vec::new();
        for j in 0..m {
            let c = chars[i][j];
            // if i == 0 {
            //     print!("{}", c);
            // }
            if c.is_digit(10) {
                cur = cur * 10 + (c as i32 - '0' as i32);
                if i > 0 {
                    if j > 0 {
                        if is_special_char(chars[i - 1][j-1]) {
                            rows.push(i - 1);
                            cols.push(j - 1);
                        }
                    }
                    if is_special_char(chars[i - 1][j]) {
                        rows.push(i - 1);
                        cols.push(j);
                    }
                    if j < m - 1 {
                        if is_special_char(chars[i - 1][j + 1]) {
                            rows.push(i - 1);
                            cols.push(j + 1);
                        }
                    }
                }
                if j > 0 {
                    if is_special_char(chars[i][j - 1]) {
                        rows.push(i);
                        cols.push(j - 1);
                    }
                }
                if j < m - 1 {
                    if is_special_char(chars[i][j + 1]) {
                        rows.push(i);
                        cols.push(j + 1);
                    }
                }
                if i < n - 1 {
                    if j > 0 {
                        if is_special_char(chars[i + 1][j - 1]) {
                            rows.push(i + 1);
                            cols.push(j - 1);
                        }
                    }
                    if is_special_char(chars[i + 1][j]) {
                        rows.push(i + 1);
                        cols.push(j);
                    }
                    if j < m - 1 {
                        if is_special_char(chars[i + 1][j + 1]) {
                            rows.push(i + 1);
                            cols.push(j + 1);
                        }
                    }
                }
            }
            else {

                let mut changed: Vec<Vec<bool>> = vec![vec![false; m]; n];
                for i in 0..rows.len() {
                    // println!("{}{}", rows[i], cols[i]);

                    if changed[rows[i]][cols[i]] {
                        continue;
                    }
                    changed[rows[i]][cols[i]] = true;
                    if gears[rows[i]][cols[i]] == 0 {
                        gears[rows[i]][cols[i]] = cur;
                    }
                    else if gears[rows[i]][cols[i]] != -1 && !gearsAdd[rows[i]][cols[i]] {
                        print!("FOIUND GEAR");
                        println!("{} {}", gears[rows[i]][cols[i]], cur);
                        gears[rows[i]][cols[i]] *= cur;
                        gearsAdd[rows[i]][cols[i]] = true;
                    }
                    else  {
                        gearsAdd[rows[i]][cols[i]] = false;
                        gears[rows[i]][cols[i]] = -1;
                    }
                }
                rows = Vec::new();
                cols = Vec::new();
                cur = 0;
            }
        }
        let mut changed: Vec<Vec<bool>> = vec![vec![false; m]; n];
        for i in 0..rows.len() {
            if changed[rows[i]][cols[i]] {
                continue;
            }
            changed[rows[i]][cols[i]] = true;
            if gears[rows[i]][cols[i]] == 0 {
                gears[rows[i]][cols[i]] = cur;
            }
            else if gears[rows[i]][cols[i]] != -1 && !gearsAdd[rows[i]][cols[i]] {
                print!("FOIUND GEAR");
                gears[rows[i]][cols[i]] *= cur;
                gearsAdd[rows[i]][cols[i]] = true;
            }
            else  {
                gearsAdd[rows[i]][cols[i]] = false;
                gears[rows[i]][cols[i]] = -1;
            }
        }
        
    }

    for i in 0..n {
        for j in 0..m {
            if gears[i][j] != -1 && gearsAdd[i][j] {
                println!("ADDING {}", gears[i][j]);
                sum += gears[i][j];
            }

        }

    }

    println!("{}", sum)

}


fn is_special_char(c: char) -> bool {
   return c == '*';
    //return c == '*';
}