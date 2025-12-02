use std::collections::VecDeque;
use std::collections::HashMap;
use std::fs::read_to_string;

struct Move {
    cur: String,
    left: String,
    right: String
}


fn create_move(s: String) -> Move {

    return Move {cur: (&s[0..3]).to_string(), left: (&s[7..10]).to_string(), right: (&s[12..15]).to_string()};
}

fn main() {



    let mut lines:Vec<String> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(|x| x.to_string())
        .collect();


    let directions = lines[0].chars().collect::<Vec<char>>();


    let mut mp: HashMap<String, Vec<&Move>> = HashMap::new();
    let moves: Vec<Move> = (&lines[2..]).iter().map(|x| create_move(x.to_string())).collect();
    moves.iter().for_each(|m| mp.entry((*m.cur).to_string()).or_insert_with(|| Vec::new()).push(m));

    let n = directions.len();
    let start = "AAA";
    let end = "ZZZ";
    let mut q: VecDeque<String> = VecDeque::new();

    moves.iter().filter(|m| m.cur.chars().nth(2) == Some('A')).for_each(|m| q.push_back(m.cur.to_string()));

    // q.push_back(start.to_string());
    let mut steps = 0;
    let mut complete = false;
    while !q.is_empty() {
        
        let m = q.len();
        for _i in 0..m {
            let dir = directions[steps % n];

            
            let front = q.pop_front().unwrap();
    
            let nextSteps = mp.get(&front).unwrap();
            nextSteps.iter().for_each(|step| {
                if step.cur.chars().nth(2) == Some('Z') {println!("{}", steps)}
                
                else if dir == 'R'  {
                    q.push_back(step.right.to_string());
                }
                else {
                    q.push_back(step.left.to_string());
                }
            });
        }
        steps += 1;

        if !q.iter().any(|x| x.chars().nth(2) != Some('Z')) {break;}
    }

    println!("{}", steps);
    
}