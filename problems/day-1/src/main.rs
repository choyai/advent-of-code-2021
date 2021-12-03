use std::env;
use std::fs;

fn main() {
    let file_name = "input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("ya done goofed! reading file failed!");
    let arr:[i32;5] = [1,2,3,4,5];
    println!("ans = {}", num_increments( &arr ) );
}

fn num_increments( arr: &[i32] ) -> i32 {
    let mut count = 0;
    for item in arr.iter().enumerate() {
        let (i, x): (usize, &i32) = item;
        if i == 0 {
            continue;
        }
        if x - arr[i-1] > 0 {
            count = count + 1;
        }
    }
    count
}
