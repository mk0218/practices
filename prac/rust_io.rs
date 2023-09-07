use std::io::{ self, BufRead, Write };

fn main() {
    let mut stdout = io::stdout();
    print!("Read a single line: ");
    if let Ok(_) = stdout.flush() {
        println!("> {}", read_single_line().expect("Err while reading a single line!"));
    }
    println!("Read multiple lines: ");
    println!("> {}", read_multiple_lines().expect("Err while reading multiple lines!"));
}

fn read_single_line() -> io::Result<String> {
    let mut user_input = String::new();
    io::stdin().read_line(&mut user_input)?;
    Ok(user_input)
}

fn read_multiple_lines() -> io::Result<String> {
    let mut lines = io::stdin().lock().lines();
    let mut user_input = String::new();

    while let Some(line) = lines.next() {
        let last_input = line.unwrap();

        if last_input.len() == 0 {
            break;
        }

        if user_input.len() > 0 {
            user_input.push_str("\n");
        }

        user_input.push_str(&last_input);
    }

    Ok(user_input)
}