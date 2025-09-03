import pygame
def main():
    pygame.init()
    sc_w, sc_h = 500, 500
    screen = pygame.display.set_mode((sc_w, sc_h))
    pygame.display.set_caption("Colour Changing Sprite")

    colours = {'red':pygame.Color('red'), 'green':pygame.Color('green'), 'blue':pygame.Color('blue'), 'yellow':pygame.Color('yellow'), 'white':pygame.Color('white')}

    current_colour = colours['white']
    x, y = 30,30
    s_w, s_h = 60,60
    clock = pygame.time.Clock()
    done = False            
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 15
        elif pressed[pygame.K_RIGHT]: x += 15
        elif pressed[pygame.K_UP]: y -= 15
        elif pressed[pygame.K_DOWN]: y += 15
        x = min(max(0,x), sc_w - s_w)
        y = min(max(0,y), sc_h - s_h)

        if x ==0: current_colour = colours['blue']
        elif x == sc_w - s_w: current_colour = colours['yellow']
        elif y == 0: current_colour = colours['red']
        elif y == sc_h - s_h: current_colour = colours['green']
        else: current_colour = colours['white']

        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_colour, (x,y,s_w,s_h))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()
