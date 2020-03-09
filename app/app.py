from app.render import render
from app.world.tile import Tile
from os import system
def clear():
    system('clear')
def run():
    init()
    loop()
def init():
    print("Welcome!")
def rend(map):
    clear()
    render.render(map)

def logic(map):
    ans = input()
    if ans == 'seed':
        print(map[0][0])
def loop():
    l = 16;
    h = 16;
    map = [[Tile('\'',l,h)] * l for i in range(h)]
    while(True):
        rend(map)
        logic(map)
