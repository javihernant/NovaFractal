import pygame
import random
import math

def main():

    D = 800 #800 maximo detalle. 200 para experiencia más fluida
    L = 3
    x0 = -1.5
    y0 = -1.5
    height = 800
    width = 800
    delta = L/D
    size_i = height / D
    size_j = width / D
    
    pygame.init()
    screen = pygame.display.set_mode([height, width])
    text = 'LOADING'
    font = pygame.font.SysFont(None, 50)
    text_img = font.render(text, True, (0,255,0))
    text_rect = text_img.get_rect()

    running = True
    while running:
        screen.fill((255, 255, 255))
        pygame.draw.rect(text_img, (255,255,255), text_rect, 1)
        screen.blit(text_img, (width/2 - text_rect.width/2, height/2 - text_rect.height/2))
        pygame.display.update()

        for i in range(D):
            for j in range(D):
                sq_props = (i*size_i,j*size_j, size_i, size_j)
                z=complex(x0+i*delta, y0+j*delta)
                drawNova4(screen, sq_props, z) #Utilizar la función drawNova2 para dibujar el conjunto de julia asociado a C=(0,0)

        print("done")
       
        pygame.display.flip()

        calcSiguiente = False
        while not calcSiguiente:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()

                click = pygame.mouse.get_pressed()
                if click != (0, 0, 0):
                    
                    
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    
                    L*=0.5
                   
                   
                    x0 += ((D/width * Mouse_x * delta) - (L/2))
                    y0 += ((D/height * Mouse_y * delta) - (L/2))
                    print(x0,y0)
                    delta = L/D
                    
                    calcSiguiente = True
                    break
                    
        

    # Done! Time to quit.
    pygame.quit()

def drawNova1(screen, sq_props, C):
    prec = 0.00000001
    max_it = 200
    Z = complex(1.0,0)
    R = complex(1,0)
    p = 3
    
    for i in range(max_it):
        
        Z_aux = Z
        Z-= R*((Z**p -1)/(3*Z**(p-1)))+C

        if (abs(Z-Z_aux)<prec):
            pygame.draw.rect(screen, ((i<<4) % 128,(i<<2) % 128,(i<<1) % 128), sq_props)
            return
    pygame.draw.rect(screen, (0,0,0), sq_props)


def drawNova2(screen, sq_props, Z):
    prec = 0.001
    max_it = 200
    C = complex(0,0)
    R = complex(1,0)
    p = 3
    
    roots = [complex(1,0),complex(-0.5,-math.sqrt(3)/2),complex(-0.5,math.sqrt(3)/2)]
    colors = [(255,0,0),(0,255,0),(0,0,255),(0,0,0)]
    if (Z == complex (0,0)):
        pygame.draw.rect(screen, colors[3], sq_props)
        return 
    for _ in range(max_it):
        Z-=R*((Z**3 -1)/(3*Z**2))+C
        for i in range(3):
            p = abs(Z-roots[i])
            if (p<prec):
                pygame.draw.rect(screen, colors[i], sq_props)
                return
    pygame.draw.rect(screen, colors[3], sq_props)

def drawNova3(screen, sq_props, Z):
    prec = 0.001
    max_it = 200
    C = complex(0,0)
    R = complex(1,0)
    roots = [complex(1,0),complex(-0.5,-math.sqrt(3)/2),complex(-0.5,math.sqrt(3)/2)]
    c0 = pygame.Color(255,0,0)
    c1 = pygame.Color(0,255,0)
    c2 = pygame.Color(0,0,255)
    c3 = pygame.Color(0,0,0) 
    colors = [c0,c1,c2,c3]
    if (Z == complex (0,0)):
        pygame.draw.rect(screen, colors[3], sq_props)
        return 
    for i in range(max_it):
        Z_aux = Z
        Z-=R*((Z**3 -1)/(3*Z**2))+C
        if (abs(Z_aux-Z)<prec):
            root = None
            diff = 99999
            for i_r in range(3):
                if abs(roots[i_r]-Z) < diff:
                    diff = abs(roots[i_r]-Z)
                    root = i_r
            if root is not None:
                sat = i/max_it * 100
                color = colors[root]
                color.hsva = (color.hsva[0],color.hsva[1],100-sat,color.hsva[3])
                pygame.draw.rect(screen, color, sq_props)
            return
        
            
    pygame.draw.rect(screen, colors[3], sq_props)

def drawNova4(screen, sq_props, C):
    prec = 0.0001
    max_it = 200
    Z = complex(1.0,0)
    R = complex(1,0)
    roots = [complex(1,0),complex(-0.5,-math.sqrt(3)/2),complex(-0.5,math.sqrt(3)/2)]
    c0 = pygame.Color(255,0,0)
    c1 = pygame.Color(0,255,0)
    c2 = pygame.Color(0,0,255)
    c3 = pygame.Color(0,0,0) 
    colors = [c0,c1,c2,c3]
    p = 3
    
    for i in range(max_it):
        
        Z_aux = Z
        Z-=R*((Z**p -1)/(3*Z**(p-1)))+C

        if (abs(Z_aux-Z)<prec):
            root = None
            diff = 99999
            for i_r in range(3):
                if abs(roots[i_r]-Z) < diff:
                    diff = abs(roots[i_r]-Z)
                    root = i_r
            if root is not None:
                sat = i/max_it * 100
                color = colors[root]
                color.hsva = (color.hsva[0],color.hsva[1],100-sat)
                pygame.draw.rect(screen, color, sq_props)
            return
        
            
    pygame.draw.rect(screen, (0,0,0), sq_props)

main()