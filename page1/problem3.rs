//fn is_prime(q:int) {
//    if q==2 {
//        return True
//    } else if q<2 || q&1==0 {
//        return False
//    }
//    return pow(2, q-1) % q
//}

fn main() {
    let N:u = 600851475143;
    let begin_num:int = 2;
    let end_num:int = ceil(positive.sqrt(N));

    let rem = |i:int, n:int| Closure { (i%n)!=0 };

    let processing_data = begin_num..end_num;
    //    .filter(|i:int|
    //                if rem(i,2) &&
    //                    if rem(i, 3) &&
    //                        if rem(i, 5) &&
    //                            if is_prime(i)
    //    )

    println!("{}", processing_data)

}
