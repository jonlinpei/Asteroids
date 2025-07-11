from circleshape import CircleShape
import pygame
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius, rotation=0):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.timer = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #     self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    #     pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        # screen.blit(self.image, (self.position.x - self.radius, self.position.y - self.radius))

    # def update(self, dt):
    #     # Player-specific update logic can be added here
    #     pass
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                print(f"Shot on cooldown; cooldown remaining: {self.timer:.2f} seconds")
            else:
                shot = self.shoot()
                if shot:
                    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
                    shot.position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
                    self.timer = PLAYER_SHOOT_COOLDOWN
                    return shot
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        return Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)