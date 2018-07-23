from PIL import Image
from argparse import ArgumentParser
from colorama import Fore

chars = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. ')


def to_gray_value(red, green, blue):
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def to_char(red, green, blue, alpha=256):
    global chars
    return ' ' if alpha == 0 else chars[int(to_gray_value(red, green, blue) / (257.0 / len(chars)))]


def main(img, width, height, output):
    output = output if output else 'output2.txt'
    image = Image.open(img).resize((width, height), Image.NEAREST)
    with open(output, 'wt') as output_file:
        line = ''
        for x in range(height):
            line = ''
            for y in range(width):
                line += to_char(*image.getpixel((y, x)))
            print(line, file=output_file)
    print(Fore.LIGHTGREEN_EX, '$ Echo: the data is saved in the', output)


def init():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-o', '--output')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--height', type=int, default=80)
    args = parser.parse_args()
    return args.file, args.width, args.height, args.output


if __name__ == '__main__':
    main(*init())