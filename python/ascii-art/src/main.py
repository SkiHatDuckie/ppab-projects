# Python v3.9.7

from PIL import Image


# Load an image and store its pixel data as a matrix (2D array)
def load_img():
    with Image.open("resources/ascii-pineapple.jpg") as img:
        # Resize so that it can fit on screen
        new_img = img.resize((int(img.width / 6), int(img.height / 6)))
        # Get pixel data as list
        pixels = list(new_img.getdata())

        # Unflatten the list
        rgb_matrix = []
        for row in range(new_img.height):
            rgb_matrix.append(list(pixels[new_img.width * row : new_img.width * (row + 1)]))
    
    print("Matrix size: {} x {}".format(len(rgb_matrix[0]), len(rgb_matrix)))
    return rgb_matrix


# Convert RGB tuples to brightness numbers
def get_brightness(rgb_matrix):
    brightness_matrix = []
    for row in range(len(rgb_matrix)):
        brightness_matrix.append(list([(r + g + b) / 3 for r, g, b in rgb_matrix[row]]))
    
    return brightness_matrix


# Convert brightness matrix to ASCII art
def asciify(matrix):
    ascii_art = []
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for row in range(len(matrix)):
        ascii_art.append(
            "".join([ascii_chars[round(x / (255 / len(ascii_chars)))] * 2 for x in matrix[row]]) + "\n"
        )

    return "".join(ascii_art)


# Main function
if __name__ == "__main__":
    rgb_matrix = load_img()
    brightness_matrix = get_brightness(rgb_matrix)
    ascii_art = asciify(brightness_matrix)
    print(ascii_art)
