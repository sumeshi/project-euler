/*
Project-Euler
---
https://projecteuler.net/
*/
use std::env;

mod p1to10;

fn main() {
    let args:Vec<String> = env::args().skip(1).collect();
    match &*args[0].to_string() {
        "p1" => p1to10::p1to10::p1(),
        "p2" => p1to10::p1to10::p2(),
        _ => println!("hogeee"),
    };
}