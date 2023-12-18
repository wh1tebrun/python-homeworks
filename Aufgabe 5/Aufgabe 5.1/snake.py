from dataclasses import dataclass
from random import randint


@dataclass
class Vec2:
    x: int
    y: int


def add_vecs(v1: Vec2, v2: Vec2) -> Vec2:
    return Vec2(v1.x + v2.x, v1.y + v2.y)


@dataclass
class Item:
    position: Vec2
    energy: int


@dataclass
class Snake:
    positions: list[Vec2]
    direction: Vec2
    alive: bool
    grow: int


@dataclass
class Game:
    snake: Snake
    width: int
    height: int
    frame: int
    items: list[Item]


def turn_direction(direction: Vec2, turn: int) -> Vec2:
    if turn == 1:
        return Vec2(-direction.y, direction.x)
    elif turn == -1:
        return Vec2(direction.y, -direction.x)
    else:
        return Vec2(direction.x, direction.y)


def turn_snake(snake: Snake, turn: int) -> Snake:
    if not snake.alive:
        return snake
    return Snake(snake.positions,
                 turn_direction(snake.direction, turn),
                 snake.alive, snake.grow)


def grow_positions(positions: list[Vec2], direction: Vec2) -> list[Vec2]:
    head = positions[0]
    return [add_vecs(head, direction)] + positions


def move_snake(snake: Snake) -> Snake:
    if not snake.alive:
        return snake
    new_positions = grow_positions(snake.positions, snake.direction)
    if snake.grow == 0:
        return Snake(new_positions[:-1], snake.direction, snake.alive,
                     snake.grow)
    else:
        return Snake(new_positions, snake.direction, snake.alive,
                     snake.grow - 1)


def collision(snake: Snake, width: int, height: int) -> bool:
    head = snake.positions[0]
    if head in snake.positions[1:]:
        return True
    if (head.x < 0 or head.x >= width or head.y < 0 or head.y >= height):
        return True
    return False


def generate_item(game: Game) -> Item:
    return Item(Vec2(randint(0, game.width - 1), randint(0, game.height - 1)),
                randint(1, 5))


def pick_item(items: list[Item], position: Vec2) -> tuple[list[Item], int]:
    new_items = []
    energy = 0
    for item in items:
        if position != item.position:
            new_items = new_items + [item]
        else:
            energy += item.energy
    return new_items, energy
