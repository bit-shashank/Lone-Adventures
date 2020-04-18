import os


def load_all_gfx(directory, pg, accept=(".png", ".jpg", ".bmp")):
    graphics = []
    for pic in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, pic)):
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                img = pg.image.load(os.path.join(directory, pic))
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
