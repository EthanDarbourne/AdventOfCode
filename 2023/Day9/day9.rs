use std::fs::read_to_string;


fn collect_diff(s: String) -> i64 {
    

    let mut nums: Vec<i64> = s.split(' ').map(|x| x.parse::<i64>().unwrap()).collect();

    let mut newVal = nums[0];
    let mut mult = 1;
    while nums.iter().any(|&x| x != 0) {

        let back = nums.len() - 1;
        
        for i in 0..back {
            nums[i] = nums[i + 1] - nums[i];
        }
        newVal -= nums[0] * mult;
        mult *= -1;
        nums.remove(back);
    }
    println!("{}", newVal);
    return newVal as i64;
}


fn main() {



    let mut lines:Vec<i64> = read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(|x| x.to_string())
        .map(|x| collect_diff(x))
        .collect();


    println!("{}", lines.iter().sum::<i64>() as i64);


}