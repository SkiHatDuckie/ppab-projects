// JavaSE v16.0.2

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.IOException;
import java.lang.Math;
import javax.imageio.ImageIO;

// Main function
public class Main {
    // Resize an image
    public static BufferedImage resizeImage(BufferedImage img, int w, int h) {
        BufferedImage new_img = new BufferedImage(w, h, img.getType());

        // Balance the input img to the output new_img
        Graphics2D g = new_img.createGraphics();
        g.drawImage(img, 0, 0, w, h, null);
        g.dispose();

        return new_img;
    }

    // Load an image and store its pixel data as a matrix (2D array)
    public static int[][][] load_img() {
        // Load image to a buffer
        BufferedImage img = null;
        try { img = ImageIO.read(new File("resources/ascii-pineapple.jpg")); } 
            catch (IOException e) {}

        // Resize so that it can fit on screen
        BufferedImage new_img = resizeImage(img, img.getWidth() / 6, img.getHeight() / 6);
        int width = new_img.getWidth();
        int height = new_img.getHeight();

        // Convert buffer to byte array
        byte[] pixels = ((DataBufferByte) new_img.getRaster().getDataBuffer()).getData();

        // Convert byte array to RGB matrix
        int[][][] rgb_matrix = new int[height][width][3];
        int pixel_length = 3;
        for (int pixel = 0, row = 0, col = 0; pixel < pixels.length; pixel += pixel_length) {
            rgb_matrix[row][col][2] += Byte.toUnsignedInt(pixels[pixel]);      // blue
            rgb_matrix[row][col][1] += Byte.toUnsignedInt(pixels[pixel + 1]);  // green
            rgb_matrix[row][col][0] += Byte.toUnsignedInt(pixels[pixel + 2]);  // red
            col++;                      
            if (col == width) {
                col = 0;
                row++;
            }
        }

        System.out.printf("Matrix size: %d x %d%n", width, height);
        return rgb_matrix;
    }

    // Convert RGB matrix to brightness numbers
    public static int[][] get_brightness(int[][][] rgb_matrix) {
        int[][] brightness_matrix = new int[rgb_matrix.length][rgb_matrix[1].length];
        for (int row = 0, col = 0; row < rgb_matrix.length; col++) {
            int r = rgb_matrix[row][col][0];
            int g = rgb_matrix[row][col][1];
            int b = rgb_matrix[row][col][2];
            brightness_matrix[row][col] = (r + g + b) / 3;
            if (col == rgb_matrix[1].length - 1) {
                col = 0;
                row++;
            }
        }

        return brightness_matrix;
    }

    // Convert brightness matrix to ASCII art
    public static String asciify(int[][] matrix) {
        String ascii_art = new String();
        String ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";
        for (int row = 0, col = 0; row < matrix.length; col++) {
            int i = (int) Math.round((double) matrix[row][col] / (255.0 / (double)ascii_chars.length()));
            ascii_art += ascii_chars.substring(i, i + 1).repeat(2);
            if (col == matrix[1].length - 1) {
                ascii_art += "\n";
                col = 0;
                row++;
            }
        }
        
        return ascii_art;
    }

    public static void main(String[] args) {
        int[][][] rgb_matrix = load_img();
        int[][] brightness_matrix = get_brightness(rgb_matrix);
        String ascii_art = asciify(brightness_matrix);
        System.out.println(ascii_art);
    }
}
