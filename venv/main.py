import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
        # init() -> (numpass, numfail)
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        for drawable_object in drawable:
            drawable_object.draw(screen)
            # print(f"Object position: {drawable_object.position}")
        dt = game_clock.tick(60)  # Limit to 60 FPS
        dt = dt / 1000.0
        updatable.update(dt)
        # count = 0
        for rock in asteroid:
            # count += 1
            # print(f"Player: {player.position}, Rock {count}: {rock.position}, Rock radius: {rock.radius}")
            if player.detect_collision(rock):
                print("Game over!")
                pygame.quit()
                return
                # Handle collision (e.g., end game, reduce health, etc.)
            for shot in shots:
                if rock.detect_collision(shot):
                    print("Rock destroyed!")
                    rock.split()
                    shot.kill()
                    # Handle rock destruction (e.g., spawn smaller rocks, increase score, etc.)
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
