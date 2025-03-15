import pygame

class NiceTextbox:
    def __init__(self,screen,message,font,pos,textcol=(255,255,255),bgcol=(0,0,0),center=True,tags=None):
        self.screen = screen
        self.message = message
        self.font = font
        self.pos = pos
        self.textcol = textcol
        self.bgcol = bgcol
        self.centered = center
        self.tags = tags

        self.pressable = False
        self.textrect = pygame.Rect(0,0,0,0)
        self.pressed = False
        self.wasPressed = False

    def move_to(self,pos):
        self.pos = pos

    def display(self):
        text = self.font.render(str(self.message), True, self.textcol, self.bgcol)
        self.textrect = text.get_rect()
        self.textrect.center = self.pos
        if self.centered:
            self.screen.blit(text, self.textrect)
        else:
            self.screen.blit(text, self.pos)

    def is_pressed(self):
        mpos = pygame.mouse.get_pos()
        #self.wasPressed = self.pressed
        self.pressed = False
        if pygame.Rect.colliderect(pygame.Rect(mpos[0],mpos[1],3,3),self.textrect) and self.pressable and pygame.mouse.get_pressed()[0]:
            if not self.wasPressed:
                self.pressed = True
            self.wasPressed = True
        else:
            self.wasPressed = False
        return self.pressed

    def set_message(self,message):
        self.message = message

    def set_textcol(self,col):
        self.textcol = col

    def set_bgcol(self,col):
        self.bgcol = col
