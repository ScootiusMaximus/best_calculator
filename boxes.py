import textbox as t
import pygame
import random
import textwrap

pygame.init()

comicsans = "fonts/Ldfcomicsans-jj7l.ttf"

minsize = 70
maxsize = 100
random_amount = 20
backgroundCol = (5,5,50)

def make_pos(x,y):
    return (x+random.randint(-random_amount,random_amount),
           y+random.randint(-random_amount,random_amount))

box1 = t.NiceTextbox(None,"1",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(100,700),center=True,bgcol=backgroundCol)
box2 = t.NiceTextbox(None,"2",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(200,700),center=True,bgcol=backgroundCol)
box3 = t.NiceTextbox(None,"3",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(300,700),center=True,bgcol=backgroundCol)
box4 = t.NiceTextbox(None,"4",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(100,600),center=True,bgcol=backgroundCol)
box5 = t.NiceTextbox(None,"5",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(200,600),center=True,bgcol=backgroundCol)
box6 = t.NiceTextbox(None,"6",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(300,600),center=True,bgcol=backgroundCol)
box7 = t.NiceTextbox(None,"7",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(100,500),center=True,bgcol=backgroundCol)
box8 = t.NiceTextbox(None,"8",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(200,500),center=True,bgcol=backgroundCol)
box9 = t.NiceTextbox(None,"9",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(300,500),center=True,bgcol=backgroundCol)
box0 = t.NiceTextbox(None,"0",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(50,750),center=True,bgcol=backgroundCol)
box_plus = t.NiceTextbox(None,"+",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(450,650),center=True,bgcol=backgroundCol)
box_minus = t.NiceTextbox(None,"-",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(450,750),center=True,bgcol=backgroundCol)
box_mul = t.NiceTextbox(None,"x",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(450,550),center=True,bgcol=backgroundCol)
box_div = t.NiceTextbox(None,"/",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),make_pos(450,450),center=True,bgcol=backgroundCol)
box_output = t.NiceTextbox(None,"",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),(50,70),center=False,bgcol=backgroundCol)
box_equals = t.NiceTextbox(None,"=",pygame.font.Font(comicsans,random.randint(minsize,maxsize)),(550,700),bgcol=None)

boxes = [box0,box1,box2,box3,box4,box5,box6,box7,box8,box9,box_plus,box_minus,box_output,box_mul,box_div,box_equals]
tncs = []
with open("terms of service.txt","r") as file:
    raw = file.readlines()

y = 50
size = 20
max_len = 600 // (size *0.6)
for line in raw:
    if line == "\n":
        y += 70

    lines = textwrap.wrap(line,max_len)
    for bit in lines:
        f = pygame.font.Font(comicsans,size)
        if "*" in bit:
            f.set_bold(True)
            bit = bit.replace("*","")
        tncs.append(t.NiceTextbox(None,bit,f,(300,y)))
        y += size*1.5

y += 50
continuebox = t.NiceTextbox(None,"Continue",pygame.font.Font(comicsans,50),(300,y),center=True,bgcol=None)
tncs.append(continuebox)