pub fn stretch_data(input_data: String) -> String {
    let reversed = input_data.chars().rev().collect::<String>(); 
    let mut inverted = String::new();
    for character in reversed.chars() {
        if character == '1' {
            inverted.push('0');
        }
            else {
            inverted.push('1');
        }
    }
    let output = String::from(input_data.to_string() + "0" + &inverted);
    output
}

pub fn produce_data_correct_length (input_data: String, disk_size: usize) -> String {
    let mut output_data = stretch_data(input_data);
    while output_data.len() < disk_size {
        output_data = stretch_data(output_data);
    }
    output_data[0..disk_size].to_string()
}

pub fn checksum (input_data: String) -> String {
    let input_data = input_data.chars().map(|x| x.to_digit(10).unwrap()).collect::<Vec<u32>>();
    let mut checksum = String::new();
    for chunk in input_data.chunks(2) {
        if chunk[0] == chunk[1] {
            checksum.push('1');
        }
        else {
            checksum.push('0');
        }
    }
    checksum
}

pub fn reduce_checksum (mut sum: String) -> String {
    sum = checksum(sum);
    if sum.len() % 2 == 0 {
        sum = reduce_checksum(sum);
    }
    sum
}

fn main () {
    let data = produce_data_correct_length("11101000110010100".to_string(), 272);
    let result = reduce_checksum(data);
    println!("Part 1: {}", result);
    let data_2 = produce_data_correct_length("11101000110010100".to_string(), 35651584);
    let result_2 = reduce_checksum(data_2);
    println!("Part 2: {}", result_2)
}

#[cfg(test)]
mod tests {
    use super::stretch_data;
    use super::produce_data_correct_length;
    use super::checksum;
    use super::reduce_checksum;

    #[test]
    fn test_stretch_data () {
        assert_eq!("100", stretch_data("1".to_string()))
    }
    
    #[test]
    fn test_get_data_long_enough () {
        assert_eq!(12, produce_data_correct_length("10".to_string(), 12).len())
    }

    #[test]
    fn test_checksum () {
        assert_eq!("110101".to_string(), checksum("110010110100".to_string()))
    }

    #[test]
    fn test_longer_checksum () {
        assert_eq!("0111110101".to_string(), checksum("10000011110010000111".to_string()))
    }

    #[test]
    fn test_reduce_checksum () {
        assert_eq!("01100".to_string(), reduce_checksum("10000011110010000111".to_string()))
    }

}
