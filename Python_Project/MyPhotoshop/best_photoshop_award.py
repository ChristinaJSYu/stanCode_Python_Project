"""
File: best_photoshop_award.py
Name: Christina
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.2


def combine(fg, bg):
    """
    : param1 fg: SimpleImage, my figure image
    : param2 bg: SimpleImage, the background image
    : return me: SimpleImage, the white screen pixels are replaced by pixels of background image
    """
    for x in range(fg.width):
        for y in range(fg.height):
            fg_pixel = fg.get_pixel(x, y)
            if fg_pixel.green > 180:
                bg_pixel = bg.get_pixel(x, y)
                fg_pixel.red = bg_pixel.red
                fg_pixel.green = bg_pixel.green
                fg_pixel.blue = bg_pixel.blue
    return fg


def main():
    """
    創作理念：我愛五條悟
    """
    fg = SimpleImage('image_contest/ME.jpg')
    bg = SimpleImage('image_contest/Background.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(fg, bg)
    combined_img.show()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
