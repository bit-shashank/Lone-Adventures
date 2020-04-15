
from settings import *
from tools import *
from sprites import *
import pygame as pg

class Map:
    def __init__(self,game):
        self.data=[]
        self.game=game
        rows=HEIGHT//TILESIZE
        cols=WIDTH//TILESIZE
        for i in range(rows):
            self.data.append([0]*cols)

        self.images=load_all_gfx('Assets//Voxel Isometric enviroment//',pg,accept=('.png'))
        self.groundTile=self.images[15]
        self.groundTile = pg.transform.scale(self.groundTile, (TILESIZE, TILESIZE)).convert_alpha()
        self.show()

    def show(self):
        for row,tiles in enumerate(self.data):
            for col,tile in enumerate(tiles):
                Ground(self.game,self,col,row)