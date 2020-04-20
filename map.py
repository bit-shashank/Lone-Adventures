
from settings import *
from tools import *
from sprites import *
import pygame as pg

class Map:
    def __init__(self,game):
        self.data=[]
        self.game=game
        rows=50
        cols=50
        self.offX=0
        self.offY=0
        for i in range(rows):
            self.data.append([0]*cols)
        
        self.data[5][5]=1
        self.data[10][5]=1

        self.images=load_all_gfx('Assets//Voxel Isometric enviroment//',pg,accept=('.png'))
        self.groundTile=self.images[15]
        self.groundTile = pg.transform.scale(self.groundTile, (TILESIZE, TILESIZE)).convert_alpha()
        self.tree=self.images[4]
        self.tree = pg.transform.scale(self.tree, (TILESIZE*3, TILESIZE*3)).convert_alpha()
        self.show()

    def show(self):
        for row,tiles in enumerate(self.data):
            for col,tile in enumerate(tiles):
                if tile==0:
                    Obstacle(self.game,self.groundTile,self,col,row)
                if tile==1:
                    Obstacle(self.game,self.tree,self,col,row)

    def update(self):
        self.offX=0
        self.offY=0
        keys=pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.offX=5
        if keys[pg.K_RIGHT]:
            self.offX=-5
        if keys[pg.K_UP]:
            self.offY=5
        if keys[pg.K_DOWN]:
            self.offY=-5