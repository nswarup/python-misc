__author__ = 'nishaswarup'

from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import urllib2

myFont = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100)

def find_char_counts(text):
    counts = {}
    for word in text:
        for c in word:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
    return counts


def count_pixels(char):
    """
    :param char: character for which we want to count pixels
    :return: number of pixels when char is drawn
    """
    img = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), char, font=myFont, fill='black')
    data = list(img.getdata())
    with open("{}1.png".format(char), 'w') as f:
        img.save(f, 'PNG')
    return len(filter(lambda rgb: sum(rgb) == 0, data))

if __name__ == '__main__':
    book_url = 'http://www.gutenberg.org/cache/epub/174/pg174.txt'
    txt = urllib2.urlopen(book_url).read()
    counts = find_char_counts(txt)
    total_pixels = 0
    for char in counts.keys():
        mult = counts[char]
        pixels = count_pixels(char)
        total_pixels += mult*pixels
    print total_pixels
