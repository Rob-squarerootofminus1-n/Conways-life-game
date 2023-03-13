import time
import pygame
import numpy as np

from pygame.locals import *

couleur_fond = (10,10,10)
couleur_grille = (45,45,45)
couleur_mort_après = (170, 170, 170)
couleur_vie_après = (255, 255, 255) #les couleurs


pygame.display.set_caption('jeu de la vie')
img = pygame.image.load('nice.jpg')
pygame.display.set_icon(img)


def update(screen, cells, size, progrès=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2])- cells[row, col]
        color= couleur_fond if cells [row, col] == 0 else couleur_vie_après
        
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if progrès:
                    color= couleur_mort_après
                    
            elif 2<=alive<=3 :
                updated_cells[row, col] = 1
                if progrès:
                    color=couleur_vie_après
                    
        else:
            if alive==3:
                updated_cells[row, col]=1
                if progrès:
                    color=couleur_vie_après
                    
        pygame.draw.rect(screen, color, (col*size, row*size, size - 1, size - 1))
        #on a juste définit les règles, trivial
        
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((1275, 650), pygame.RESIZABLE)
    
    cells = np.zeros((65, 127))
    screen.fill(couleur_grille) 
    
    update(screen, cells, 10)
    #on remplit le fond avec la couleur sauf si pour des cellules on a des bonnes raisons de ne pas le faire
    
    pygame.display.flip()
    pygame.display.update()
    
    running =False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running #python et moi on partage le même neurone
                    update(screen, cells, 10) 
                    #avec une pause, on a l'image figée de l'écran qui a fait une update
                    pygame.display.update()
                    
                    
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()
                
        screen.fill(couleur_grille)
        
        if running:
            cells = update(screen, cells, 10, progrès=True)
            pygame.display.update()
            
        time.sleep(0.000001)
        
if __name__ == '__main__':
    main()
    
pygame.quit()