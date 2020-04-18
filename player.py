import random
import tools
import os
import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    walk_frames = []
    attack_frames = []
    death_frames = []
    idle_frames = []
    jump_frames = []
    run_frames = []
    directions = {'S': 0, 'SE': 1, 'E': 2, 'NE': 3, 'N': 4, 'NW': 5, 'W': 6, 'SW': 7}
    facing = directions['S']
    count = 0

    def __init__(self, game, x, y):
        self.loadAssets()
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.last_update = 0
        self.currentFrame = 0
        self.image = self.idle_frames[0].convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.walking = False
        self.idle = True
        self.attacking = False
        self.running = False

    def show(self):
        (isoX, isoY) = tools.cartToiso(self.x, self.y)
        self.animate()
        self.rect.x = isoX
        self.rect.y = isoY

    def animate(self):
        now = pg.time.get_ticks()

        # Attack animation
        if now - self.last_update > 40:
            if self.attacking:
                self.last_update = now
                if self.count + 1 == 18:
                    self.attacking = False
                    self.count = 0
                self.count = (self.count + 1) % 18
                loc = self.facing * 18 + self.count
                self.image = self.attack_frames[loc]

        # Walking animation
        if now - self.last_update > 50:
            if self.walking and not self.attacking:
                self.last_update = now
                self.count = (self.count + 1) % 15
                loc = self.facing * 15 + self.count
                self.image = self.walk_frames[loc]

        # idle animation
        if now - self.last_update > 40:
            if self.idle and not self.attacking:
                self.last_update = now
                self.count = (self.count + 1) % 16
                loc = self.facing * 16 + self.count
                self.image = self.idle_frames[loc]

    '''
        All input events related to player are handelled here
        Sets the value of player states variable based on the key pressed
    '''

    def update(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.dx = -1
        if keys[pg.K_RIGHT]:
            self.dx = 1
        if keys[pg.K_UP]:
            self.dy = -1
        if keys[pg.K_DOWN]:
            self.dy = 1
        if keys[pg.K_SPACE]:
            self.attacking = True

        self.x += self.dx
        self.y += self.dy

        if self.dx == 0 and self.dy == 0:
            self.idle = True
            self.walking = False
        else:
            self.walking = True
            self.idle = False

        self.setFacing()
        self.show()

        self.dx = 0
        self.dy = 0

    '''
        This function sets the value of facing based upon the value of
        dx and dy variables.
        Currently hardcoded, i think its better this way.
    '''

    def setFacing(self):
        if self.dx == 0 and self.dy == -1:
            self.facing = self.directions['N']
        elif self.dx == 1 and self.dy == -1:
            self.facing = self.directions['NE']
        elif self.dx == 1 and self.dy == 0:
            self.facing = self.directions['E']
        elif self.dx == 1 and self.dy == 1:
            self.facing = self.directions['SE']
        elif self.dx == 0 and self.dy == 1:
            self.facing = self.directions['S']
        elif self.dx == -1 and self.dy == 1:
            self.facing = self.directions['SW']
        elif self.dx == -1 and self.dy == 0:
            self.facing = self.directions['W']
        elif self.dx == -1 and self.dy == -1:
            self.facing = self.directions['NW']

    '''
        Function to load all the assets related to player
    '''

    def loadAssets(self):
        path = 'Assets/isometric_Mini-Crusader/walk/'
        self.walk_frames = tools.load_all_gfx(path, pg, accept=('.png'))

        path = 'Assets/isometric_Mini-Crusader/idle/'
        self.idle_frames = tools.load_all_gfx(path, pg, accept=('.png'))

        path = 'Assets/isometric_Mini-Crusader/attack/'
        self.attack_frames = tools.load_all_gfx(path, pg, accept=('.png'))

        path = 'Assets/isometric_Mini-Crusader/jump/'
        self.jump_frames = tools.load_all_gfx(path, pg, accept=('.png'))
