// Rust v1.53.0

extern crate image;

use image::{
    imageops, RgbImage, GenericImageView,
};

// Load an image and store its pixel data as a matrix (2D array)
fn load_img() -> RgbImage {
    // Load image to a buffer
    let img = image::open("../../resources/ascii-pineapple.jpg").unwrap();
    // Resize so that it can fit on screen
    let rgb_matrix = img.resize(
        img.dimensions().0 / 6, 
        img.dimensions().1 / 6, 
        imageops::Lanczos3
    ).into_rgb8();
    let width = rgb_matrix.dimensions().0;
    let height = rgb_matrix.dimensions().1;

    println!("Matrix size: {} x {}", width, height);
    rgb_matrix
}

// Convert RGB arrays to brightness numbers
fn get_brightness(rgb_matrix: RgbImage) -> Vec<Vec<u8>> {
    let mut brightness_matrix = vec![vec![0u8; rgb_matrix.width() as usize]; rgb_matrix.height() as usize];
    let mut col: usize = 0;
    let mut row: usize = 0;
    for px in rgb_matrix.pixels() {
        brightness_matrix[row][col] = ((u16::from(px[0]) + u16::from(px[1]) + u16::from(px[2])) / 3) as u8;
        col += 1;
        if col == rgb_matrix.width() as usize { 
            col = 0;
            row += 1;
        }
    }

    brightness_matrix
}

// Convert brightness matrix to ASCII art
fn asciify(matrix: Vec<Vec<u8>>) -> String {
    let mut ascii_art = String::new();
    let ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";
    for row in matrix.iter() {
        for px in row.iter() {
            let i = (f32::from(*px) / (255.0 / ascii_chars.len() as f32)) as usize;
            ascii_art.push_str(((ascii_chars.as_bytes()[i] as char).to_string()).repeat(2).as_str());
        }
        ascii_art.push('\n');
    }

    ascii_art
}

// Main function
fn main() {
    let rgb_matrix = load_img();
    let brightness_matrix = get_brightness(rgb_matrix);
    let ascii_art = asciify(brightness_matrix);
    println!("{}", ascii_art);
}
