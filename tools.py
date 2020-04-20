import os
from settings import *

def load_all_gfx(directory,pg,accept=(".png",".jpg",".bmp"),width=None,height=None):
    graphics = []
    for pic in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, pic)):
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                img = pg.image.load(os.path.join(directory,pic))
                if width!=None:
                    img= pg.transform.scale(img, (width, height)).convert_alpha()
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


