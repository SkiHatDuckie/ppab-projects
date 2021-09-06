// JavaSE v16.0.2

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.IOException;
import java.lang.Math;
import javax.imageio.ImageIO;

class Imaging {
    public static BufferedImage resizeImage(BufferedImage img, int w, int h) {
        BufferedImage new_img = new BufferedImage(w, h, img.getType());

        // Balance the input img to the output new_img
        Graphics2D g = new_img.createGraphics();
        g.drawImage(img, 0, 0, w, h, null);
        g.dispose();

        return new_img;
    }
}

// Main function
public class Main {
    // Load an image and store its pixel data as a matrix (2D array)
    static int[][] load_img() {
        // Load image to a buffer
        BufferedImage img = null;
        try { img = ImageIO.read(new File("resources/ascii-pineapple.jpg")); } 
            catch (IOException e) {}

        // Resize so that it can fit on screen
        BufferedImage new_img = Imaging.resizeImage(img, img.getWidth() / 6, img.getHeight() / 6);
        int width = new_img.getWidth();
        int height = new_img.getHeight();

        // Convert buffer to byte array
        byte[] pixels = ((DataBufferByte) new_img.getRaster().getDataBuffer()).getData();

        // Convert byte array to 2D array of ints
        int[][] rgb_matrix = new int[height][width];
        int pixel_length = 3;
        for (int pixel = 0, row = 0, col = 0; pixel < pixels.length; pixel += pixel_length) {
            int argb = 0;
            argb += -16777216;                                // 255 alpha
            argb += ((int) pixels[pixel] & 0xff);             // blue
            argb += (((int) pixels[pixel + 1] & 0xff) << 8);  // green
            argb += (((int) pixels[pixel + 2] & 0xff) << 16); // red
            rgb_matrix[row][col] = argb;
            col++;                      
            if (col == width) {
                col = 0;
                row++;
            }
        }
        // Important note: This stores each pixel color as a packed int instead of an array 
        // (TODO: Should this be changed?)

        System.out.printf("Matrix size: %d x %d%n", width, height);
        return rgb_matrix;
    }

    // Convert RGB packed int to brightness numbers
    static int[][] get_brightness(int[][] rgb_matrix) {
        int[][] brightness_matrix = new int[rgb_matrix.length][rgb_matrix[1].length];
        for (int row = 0, col = 0; row < rgb_matrix.length; col++) {
            int r = (rgb_matrix[row][col] >>> 16) & 0xFF;  // Extract color info from packed int
            int g = (rgb_matrix[row][col] >>>  8) & 0xFF;
            int b = (rgb_matrix[row][col] >>>  0) & 0xFF;
            brightness_matrix[row][col] = (r + g + b) / 3;
            if (col == rgb_matrix[1].length - 1) {
                col = 0;
                row++;
            }
        }

        return brightness_matrix;
    }

    // Convert brightness matrix to ASCII art
    static String asciify(int[][] matrix) {
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
        int[][] rgb_matrix = load_img();
        int[][] brightness_matrix = get_brightness(rgb_matrix);
        String ascii_art = asciify(brightness_matrix);
        System.out.println(ascii_art);
    }
}
