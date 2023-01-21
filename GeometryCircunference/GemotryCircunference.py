import pygame, math, random
import Pieza as p

pygame.init()
pygame.display.set_caption("Geometry")
clock = pygame.time.Clock()

fps_limit = 60
cols, rows = 5, 5
width, height = 800, 800
screen = pygame.display.set_mode((width,int(height)))
screen.fill((0,0,0))
diameter = width/cols
piezas = []

def DrawPiezas():
    global piezas
    for i in range(rows):
        for j in range(cols):
            ps = p.Pieza((i*diameter,j*diameter),diameter, screen)
            piezas.append(ps)
    pygame.display.update()


def GameLoop():
    run, pause = True, False
    angleRotation, last_pause = 0, 0
    rand = [random.uniform(0,1) < 0.75 for _ in range(cols*rows)]
    press = None
    try:
        DrawPiezas()
        while run:
            clock.tick(fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                         press = True 
            pause = (angleRotation != 0 and angleRotation % 90 == 0)
            # if press:
            if not pause:
                for i,pieza in enumerate(piezas):
                    pieza.RotarPieza(rand[i])
                    pygame.display.update()
                    last_pause = pygame.time.get_ticks()
                angleRotation += 1
            elif pygame.time.get_ticks() - last_pause >= 1000:
                    pause = False
                    angleRotation = 0
                    rand = [random.uniform(0,1) < 0.75 for _ in range(cols*rows)]
                    # press = False
    except Exception as error:
        raise(error)

    finally:
        pygame.quit

if __name__ == "__main__":
    GameLoop()






