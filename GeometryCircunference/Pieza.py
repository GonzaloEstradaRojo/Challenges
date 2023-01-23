import pygame, random, math, time

class Pieza():
    def __init__(self, pos, diameter, screen) -> None:
        self._pos = pos
        self._diameter = diameter
        self._radius = self._diameter/2
        self._border = 0
        self._cirThick = 10
        self._screen = screen
        self._background = pygame.Surface((self._diameter - self._border, self._diameter - self._border), pygame.SRCALPHA) 
        self._surface = pygame.Surface((self._diameter - self._border, self._diameter - self._border), pygame.SRCALPHA)
        self._angle = 0
        self._angleSpeed = 1
        self._seed = random.randint(0,1)

        self.CreateSurface()
        self.DrawCircle()

    def CreateSurface(self):
        self._background.fill((100,100,100,255))
        self._rect = self._surface.get_rect()
        self._rect.x, self._rect.y = self._pos[0] + self._border/2, self._pos[1] + self._border/2  
        self._screen.blit(self._background , self._rect)  
        self._screen.blit(self._surface , self._rect)  

    def DrawCircle(self):
        if(self._seed == 0):
            pygame.draw.circle(self._surface, (255,0,0),(self._diameter - self._cirThick/2, self._diameter - self._cirThick/2), self._radius, self._cirThick)
            pygame.draw.circle(self._surface, (255,0,0),(self._cirThick/2, self._cirThick/2), self._radius, self._cirThick)
        elif(self._seed == 1):
            pygame.draw.circle(self._surface, (255,0,0),(self._cirThick/2, self._diameter - self._cirThick/2), self._radius, self._cirThick)
            pygame.draw.circle(self._surface, (255,0,0),(self._diameter - self._cirThick/2 , self._cirThick/2), self._radius, self._cirThick)
        self._screen.blit(self._surface , self._rect)  

    def RotarPieza(self,dir):
        if(dir): #Girar
            self._angle = (self._angle + self._angleSpeed) % 360  

        old_center = self._rect.center         
        new_image = pygame.transform.rotate(self._surface , self._angle)         
        new_rect = new_image.get_rect()  
        new_rect.center = old_center  
        print(self._angle)
        self._screen.blit(self._background , self._rect)  
        self._screen.blit(new_image , new_rect)  

