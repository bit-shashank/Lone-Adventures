import pygame as pg
import random
from settings import *
from sprites import *
from map import *


class Game:
    def __init__(self):
        #init the game window ,clock and starts the game
        pg.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock=pg.time.Clock()
        self.running=True


    def new(self):
        #Init all the sprits
        #and start a new game by calling run method
        self.all_sprits=pg.sprite.Group()
        self.player=Player(self,WIDTH//2,HEIGHT//2)
        self.map=Map(self)
        self.all_sprits.add(self.player)
        self.run()
        
    def run(self):
        #starts a new game loop 
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprits.update()
        self.map.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprits.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()