import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def detect_collision(self, other):
        # Check if this circle collides with another circle
        distance = self.position.distance_to(other.position)
        # print(f"Distance: {distance}, Self Radius: {self.radius}, Other Radius: {other.radius}")
        return distance < (self.radius + other.radius)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass