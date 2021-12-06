# Python v3.9.7

from PIL import Image


# Unflatten a list
# ls: List to be unflattened
# height: Number of rows needed from list
# width: Width of each row
# RETURN: A list of lists (matrix)
def unflatten(ls, height, width):
    new_matrix = []
    for row in height:
        new_matrix.append(list(ls[width * row : width * (row + 1)]))

    return new_matrix


# Load an image and store its pixel data as a matrix (2D array)
# RETURN: Matrix of RGB values
def load_img():
    with Image.open("resources/ascii-pineapple.jpg") as img:
        # Resize so that it can fit on screen
        new_img = img.resize((int(img.width / 6), int(img.height / 6)))

    pixels = list(new_img.getdata())
    rgb_matrix = unflatten(pixels, new_img.height, new_img.width)
    
    print("Matrix size: {} x {}".format(len(rgb_matrix[0]), len(rgb_matrix)))
    return rgb_matrix


# Convert RGB tuples to brightness numbers
# rgb_matrix: Matrix of RGB values
# RETURN: Matrix of integers representing brightness
def get_brightness(rgb_matrix):
    brightness_matrix = []
    for row in range(len(rgb_matrix)):
        brightness_matrix.append(list([(r + g + b) / 3 for r, g, b in rgb_matrix[row]]))
    
    return brightness_matrix


# Convert brightness matrix to ASCII art
# matrix: Brightness matrix
# RETURN: String of ascii character
def asciify(matrix):
    ascii_art = []
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for row in range(len(matrix)):
        ascii_art.append(
            "".join([ascii_chars[round(x / (255 / len(ascii_chars)))] * 2 for x in matrix[row]]) + "\n"
        )

    return "".join(ascii_art)


# Main
if __name__ == "__main__":
    rgb_matrix = load_img()
    brightness_matrix = get_brightness(rgb_matrix)
    ascii_art = asciify(brightness_matrix)
    print(ascii_art)
