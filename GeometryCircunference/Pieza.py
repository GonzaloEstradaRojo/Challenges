import pygame, random, math, time

class Pieza():
    def __init__(self, pos, diameter, screen) -> None:
        self._pos = pos
        self._diameter = diameter
        self._radius = self._diameter/2
        self._border = 5
        self._cirThick = 5
        self._screen = screen
        self._surface = pygame.Surface((self._diameter - self._border, self._diameter - self._border), pygame.SRCALPHA)
        self._angle = 0
        self._angleSpeed = 1

        self.CreateSurface()
        self.DrawCircle()

    def CreateSurface(self):
        self._surface.fill((100,100,100,128))  

        self._rect = self._surface.get_rect()
        self._rect.x, self._rect.y = self._pos       
        # pygame.draw.rect(self._surface, (255, 0, 0),self._surface.get_rect(), 2)
   
    def DrawCircle(self):
        if(self._seed == 1):
            pygame.draw.arc(self._surface, (244,0,0), (-self._radius + self._cirThick/2,-self._radius + self._cirThick/2,self._diameter,self._diameter),math.pi,math.pi/2,self._cirThick)
            pygame.draw.arc(self._surface, (0,244,0), (self._radius - self._cirThick/2, self._radius - self._cirThick/2,self._diameter,self._diameter), math.pi*2,math.pi*3/2,self._cirThick)
        elif(self._seed == 2):
            pygame.draw.arc(self._surface, (0,0,244), (-self._radius + self._cirThick/2,self._radius - self._cirThick/2,self._diameter,self._diameter),math.pi*3/2,math.pi,self._cirThick)
            pygame.draw.arc(self._surface, (0,0,0), (self._radius - self._cirThick/2,-self._radius + self._cirThick/2,self._diameter,self._diameter), math.pi/2,math.pi*2,self._cirThick)
        self._screen.blit(self._surface , self._rect)  
    
    def RotarPieza90(self,dir):
        if(dir): #Girar
            self._angle = (self._angle + self._angleSpeed) % 360  

        old_center = self._rect.center  
       
        new_image = pygame.transform.rotate(self._surface , self._angle)         
        new_rect = new_image.get_rect()  
        new_rect.center = old_center  

        self._screen.blit(new_image , new_rect)  
