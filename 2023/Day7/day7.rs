use std::fs::read_to_string;
use std::collections::HashMap;
use std::fmt;
use std::convert::TryInto;

struct Hand {
    cards: [char; 5],
    bid: u64,
    hand_type: HandType
}

#[derive(PartialEq, Eq, PartialOrd, Ord, Copy, Clone)]
enum HandType {
    HighCard = 0,
    OnePair = 1,
    TwoPair = 2,
    ThreeOfAKind = 3,
    FullHouse = 4,
    FourOfAKind = 5,
    FiveOfAKind = 6
}

impl fmt::Display for HandType {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            HandType::HighCard => write!(f, "HighCard"),
            HandType::OnePair => write!(f, "OnePair"),
            HandType::TwoPair => write!(f, "TwoPair"),
            HandType::ThreeOfAKind => write!(f, "ThreeOfAKind"),
            HandType::FullHouse => write!(f, "FullHouse"),
            HandType::FourOfAKind => write!(f, "FourOfAKind"),
            HandType::FiveOfAKind => write!(f, "FiveOfAKind"),
        }
    }
}

fn create_hand(hand: String) -> Hand {
    let parts: Vec<String> = hand.split(' ').map(|x| x.to_string()).collect::<Vec<String>>();
    let cards: [char; 5] = parts[0].chars().collect::<Vec<char>>().try_into().unwrap();


    let mut letter_counts: HashMap<char, i32> =
        parts[0]
            .chars()
            .fold(HashMap::new(), |mut map, c| {
                *map.entry(c).or_insert(0) += 1;
                map
            });
    let mut hand_type = HandType::HighCard;
    for (letter, count) in &letter_counts {
        if *letter == 'J' {
            continue;
        }
        hand_type = match count {
            5 => HandType::FiveOfAKind,
            4 => HandType::FourOfAKind,
            3 => if matches!(hand_type, HandType::OnePair) {HandType::FullHouse} else {HandType::ThreeOfAKind},
            2 => if matches!(hand_type, HandType::OnePair) {HandType::TwoPair} else if matches!(hand_type, HandType::ThreeOfAKind) {HandType::FullHouse} else {HandType::OnePair},
            _ => hand_type
        }
    }

    hand_type = match letter_counts.entry('J').or_default() {
        4 | 5 => HandType::FiveOfAKind,
        3 => if matches!(hand_type, HandType::OnePair) { HandType::FiveOfAKind } else {HandType::FourOfAKind},
        2 => if matches!(hand_type, HandType::ThreeOfAKind) { HandType::FiveOfAKind } else if matches!(hand_type, HandType::OnePair) {HandType::FourOfAKind} else {HandType::ThreeOfAKind}
        1 => if matches!(hand_type, HandType::FourOfAKind) { HandType::FiveOfAKind } else if matches!(hand_type, HandType::ThreeOfAKind) {HandType::FourOfAKind} 
        else if matches!(hand_type, HandType::TwoPair) {HandType::FullHouse} else if matches!(hand_type, HandType::OnePair) {HandType::ThreeOfAKind} else {HandType::OnePair}
        _ => hand_type
    };

    // println!("{} {} {}",cards.iter().collect::<String>(),  parts[1], hand_type.to_string());
    return Hand {cards: cards, bid: parts[1].parse::<u64>().unwrap(), hand_type: hand_type};
}


fn main() {
    let mut hands:Vec<Hand> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(|x| x.to_string())
        .map(|x| create_hand(x))
        .collect();


    let card_ord = [ 'J', '2','3' ,'4' , '5', '6','7' , '8', '9', 'T' , 'Q', 'K', 'A'];
    // hands[0].cards.iter().for_each(|card| print!("{}", card_ord.iter().position(|c| c == card).unwrap()));
    hands.sort_unstable_by_key(|hand| (hand.hand_type, hand.cards.iter().map(|card| card_ord.iter().position(|c| c == card).unwrap()).collect::<Vec<usize>>()));


    let n: u64 = hands.len() as u64;
    for hand in &hands {
        println!("{} {} {}",hand.cards.iter().collect::<String>(), hand.bid, hand.hand_type.to_string())
    }

    let res: u64 = hands.iter().enumerate().fold(0, |acc, (i, hand)| acc + (i as u64 + 1) * hand.bid);

    println!("{}", res);



}