import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #CREATING GROUPS:
    update_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (update_group, drawable_group)
    Asteroid.containers = (asteroids, update_group, drawable_group)
    AsteroidField.containers = update_group
    Shot.containers = (shot_group, update_group, drawable_group)

    

    
    #Asteroid Field object:
    asteroid_field = AsteroidField()

    # player object:
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #converts fps to numerical value
    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        
        
        #PLAYER MOVEMENTS
        update_group.update(dt)

        #PLAYER SHOTS
        player.shoot(dt)

        #COLLISION CHECK:
        for asteroid in asteroids: 
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit() #This exits the program!

        #BULLET COLLISION CHECK
        for asteroid in asteroids:
            for shot in shot_group:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()

        #RENDER IN PLAYER
        for drawable in drawable_group: 
            drawable.draw(screen)

        

        pygame.display.flip()

        dt = clock.tick(60) / 1000



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()