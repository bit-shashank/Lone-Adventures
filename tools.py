import os
from settings import *

<<<<<<< HEAD
def load_all_gfx(directory,pg,accept=(".png",".jpg",".bmp"),width=TILESIZE,height=TILESIZE):
=======

def load_all_gfx(directory, pg, accept=(".png", ".jpg", ".bmp")):
>>>>>>> a1f6305af4919579eda49c3cedf494f1d4e504db
    graphics = []
    for pic in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, pic)):
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
<<<<<<< HEAD
                img = pg.image.load(os.path.join(directory,pic))
                img= pg.transform.scale(img, (width, height)).convert_alpha()
=======
                img = pg.image.load(os.path.join(directory, pic))
>>>>>>> a1f6305af4919579eda49c3cedf494f1d4e504db
                graphics.append(img)
    return graphics


def isoTocart(isoX, isoY):
    cartX = (2 * isoY + isoX) // 2
    cartY = (2 * isoY - isoX) // 2
    return (cartX, cartY)


def cartToiso(cartX, cartY):
    isoX = cartX - cartY
    isoY = (cartX + cartY) // 2
    return (isoX, isoY)


class Animator:

    def __init__(self, frames, fps):
        self.frames = frames
        self.fps = fps
        self.frame = 0
