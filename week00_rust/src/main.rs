// week00_rust/src/main.rs
// Setup verification - not actual course content

fn main() {
    println!("Hello from Rust!");
    println!("If this compiles, your Rust toolchain is working!");
}

#[allow(dead_code)]
fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_numbers() {
        assert_eq!(add_numbers(2, 3), 5);
        assert_eq!(add_numbers(0, 0), 0);
        assert_eq!(add_numbers(-1, 1), 0);
    }

    #[test]
    fn test_basic_rust() {
        // Just verify Rust syntax works
        let message = "Hello, IS4010!";
        assert_eq!(message.len(), 14);
    }
}
