#/// script
# dependencies = [
# "images",
# "boxes",
# "textboxes",
# "pyautogui",
# ]
# ///

import asyncio
import pygame
import sys
import pyautogui as pg
import threading
import webbrowser

from boxes import *
from images import *


class Program:
    def __init__(self):
        pygame.init()

        self.scrw = 600
        self.scrh = 800

        self.screen = pygame.display.set_mode((self.scrw,self.scrh))
        pygame.display.set_caption("")
        self.clock = pygame.time.Clock()

        self.input = ""
        self.scene = "terms"
        self.scroll = 0
        self.relative_scroll = 0
        self.ad_id = 0
        self.last_ad_change = 0
        self.premium_tries = 0

        for item in boxes:
            item.screen = self.screen
            item.pressable = True

        for item in tncs:
            item.screen = self.screen

        continuebox.pressable = True

    def draw_buttons(self):
        pygame.draw.rect(self.screen, (5, 5, 80), (45, 45, self.scrw - 90, 170))
        pygame.draw.rect(self.screen,(5,5,50),(50,50,self.scrw-100,150))
        pygame.draw.rect(self.screen,(5,5,50),(500,500,90,290))

        box_output.set_message(self.input)
        for item in boxes:
            item.display()

    def handle_input(self):
        for item in boxes:
            if item.is_pressed():
                if item is box_equals:
                    self.premium_tries += 1
                    t = threading.Thread(target=
                    pg.confirm,args=("Equals button is a premium feature",))
                    t.start()
                else:
                    self.input = self.input + item.message

    def run_tncs(self):
        for item in tncs:
            new = (item.pos[0],item.pos[1] + self.relative_scroll)
            item.move_to(new)
            item.display()

        if continuebox.is_pressed():
            self.scene = "calc"

    def run_adverts(self):
        if self.now() - self.last_ad_change > 5000:
            self.last_ad_change = self.now()
            self.ad_id += 1
            if self.ad_id > len(ads)-1:
                self.ad_id = 0

        if self.scene == "calc":
            self.screen.blit(ads[self.ad_id],(50,280))

    def handle_premium(self):
        if self.premium_tries == 3:
            self.premium_tries = 0
            ans = pg.prompt("You have exceeded the free trial\n"
                      "Please enter your bank details to\n"
                      "continue to the premium version")
            if ans in ["","cancel","CANCEL"]:
                #import BSOD
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D")

    def now(self):
        return pygame.time.get_ticks()

    def handle_events(self):
        self.relative_scroll = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            elif event.type == pygame.MOUSEWHEEL:
                if (event.y < 0 and self.scroll > -5000) or (event.y > 0 > self.scroll):
                    self.relative_scroll = event.y / 0.5
                    self.scroll += self.relative_scroll

    def quit(self):
        pygame.quit()
        sys.exit(0)

    async def start(self):
        while True:
            await asyncio.sleep(0)
            self.clock.tick(20)
            pygame.display.flip()
            self.screen.fill((0,0,0))

            self.handle_events()
            self.run_adverts()

            self.handle_premium()

            if self.scene == "calc":
                self.draw_buttons()
                self.handle_input()

            elif self.scene == "terms":
                self.run_tncs()

prog = Program()
asyncio.run(prog.start())