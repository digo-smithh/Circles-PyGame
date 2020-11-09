# Made by Rodrigo Smith - 2020. See LICENSE for more information

import pygame as pg
from io import BytesIO
import requests
from PIL import Image
import os 

rsp = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSWXX1BiNgAehwo4etg3zLwsu884I1Ekj9odw&usqp=CAU')
pilimage = Image.open(BytesIO(rsp.content)).convert("RGBA")
pgimg = pg.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)
pg.display.set_icon(pgimg)

pg.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.display.set_caption('PyGame')
screen = pg.display.set_mode((400,400))

clock = pg.time.Clock()

done = False
is_blue = True
x1 = 100
y1 = 100
x2 = 280
y2 = 280

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    pressed1 = pg.key.get_pressed() 
    if pressed1[pg.K_UP] and y1 > 3: y1 -= 3 
    if pressed1[pg.K_DOWN] and y1 < 357: y1 +=3 
    if pressed1[pg.K_LEFT] and x1 > 3: x1 -= 3 
    if pressed1[pg.K_RIGHT] and x1 < 357: x1 +=3 

    pressed2 = pg.key.get_pressed() 
    if pressed2[pg.K_w] and y2 > 3: y2 -= 3 
    if pressed2[pg.K_s] and y2 < 357: y2 +=3 
    if pressed2[pg.K_a] and x2 > 3: x2 -= 3 
    if pressed2[pg.K_d] and x2 < 357: x2 +=3 

    if x1 > x2: color = (100,128,255) 
    else: color = (255,100,255) 

    screen.fill((0,0,0)) 
    pg.draw.circle(screen, color, (x1,y1), 25) 
    pg.draw.circle(screen,(255,150,0), (x2,y2), 25) 

    pg.display.flip()  

    clock.tick(60)      
