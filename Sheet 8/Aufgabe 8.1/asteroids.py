from dataclasses import dataclass
from math import sqrt
import pygame


@dataclass
class Vec2:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def abs(self) -> float:
        return sqrt((self.x) ** 2 + (self.y) ** 2)


@dataclass
class GameObject:
    position: Vec2
    radius: int
    alive: bool
    color: tuple[int, int, int]

    def update(self, width: int, height: int, delta: float):
        if not (0 <= self.position.x < width and 0 <= self.position.y < height):
            self.alive = False

    def is_colliding(self, other: 'GameObject') -> bool:
        pos = Vec2(self.position.x - other.position.x, self.position.y - other.position.y)
        distance = pos.abs()
        combined_radius = self.radius + other.radius
        return distance <= combined_radius

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)


@dataclass
class Projectile(GameObject):
    speed: float

    def update(self, width: int, height: int, delta: float):
        super().update(width, height, delta)
        self.position.y -= delta * self.speed

    def on_collision(self, other: 'GameObject'):
        if not isinstance(other, Ship):
            self.alive = False


@dataclass
class StaticObject(GameObject):
    rotation: float

    def update(self, width: int, height: int, delta: float):
        self.position.y += delta
        self.rotation += delta / self.radius
        super().update(width, height, delta)

    def on_collision(self, other: 'GameObject'):
        self.alive = False


@dataclass
class Item(StaticObject):
    amount: int


@dataclass
class Ammunition(Item):
    pass


@dataclass
class Health(Item):
    pass


@dataclass
class Ship(GameObject):
    shots: int
    hp: int

    def update(self, width: int, height: int, delta: float):
        super().update(width, height, delta)
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def on_collision(self, other: 'GameObject'):
        if isinstance(other, Asteroid):
            self.hp -= other.radius
        elif isinstance(other, Health):
            self.hp += other.amount
        elif isinstance(other, Ammunition):
            self.shots += other.amount

    def shoot(self) -> Projectile:
        if self.shots > 0:
            self.shots -= 1
            projectile_position = Vec2(self.position.x, self.position.y)
            return Projectile(projectile_position, 5.0, True, (255, 0, 0), 3.0)
        else:
            return Projectile(Vec2(0, 0), 5.0, False, (255, 0, 0), 3.0)


@dataclass
class Asteroid(StaticObject):
    special: bool

    def on_collision(self, other: 'GameObject'):
        if not isinstance(other, Asteroid):
            self.alive = False
