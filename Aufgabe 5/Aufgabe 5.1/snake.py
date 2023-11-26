from dataclasses import dataclass
from random import randint


@dataclass
class Vec2:
    x: int
    y: int


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


def add_vecs(v1: Vec2, v2: Vec2) -> Vec2:
    x = v1.x + v2.x
    y = v1.y + v2.y
    return Vec2(x, y)


def turn_direction(direction: Vec2, turn: int) -> Vec2:
    if turn != -1 and turn != 1:
        return direction
    if turn == 1:
        if direction.x == 1 and direction.y == 0:
            return Vec2(0, 1)
        if direction.x == 0 and direction.y == 1:
            return Vec2(-1, 0)
        if direction.x == -1 and direction.y == 0:
            return Vec2(0, -1)
        if direction.x == 0 and direction.y == -1:
            return Vec2(1, 0)
    if turn == -1:
        if direction.x == 1 and direction.y == 0:
            return Vec2(0, -1)
        if direction.x == 0 and direction.y == -1:
            return Vec2(-1, 0)
        if direction.x == -1 and direction.y == 0:
            return Vec2(0, 1)
        if direction.x == 0 and direction.y == 1:
            return Vec2(1, 0)


def turn_snake(snake: Snake, turn: int) -> Snake:
    if not snake.alive:
        return snake

    snake.direction = turn_direction(snake.direction, turn)
    return snake


def grow_positions(positions: list[Vec2], direction: Vec2) -> list[Vec2]:
    newVec2 = add_vecs(positions[0], direction)
    positions.insert(0, newVec2)
    return positions


def move_snake(snake: Snake) -> Snake:
    if not snake.alive:
        return snake
    newPositions = grow_positions(snake.positions, snake.direction)
    if snake.grow == 0:
        snake.positions = newPositions[:-1]
    elif snake.grow > 0:
        snake.positions = newPositions
        snake.grow = snake.grow - 1
    return snake


def collision(snake: Snake, width: int, height: int) -> bool:

    if snake.positions[0].x > width or snake.positions[0].x < 0:
        return True

    if snake.positions[0].y > height or snake.positions[0].y < 0:
        return True

    prevPositions = {}
    for position in snake.positions:
        key = str(position.x) + "/" + str(position.y)
        found = prevPositions.get(key)

        if found:
            return True
        else:
            prevPositions[key] = True
    return False


def generate_item(game: Game) -> Item:
    energy = randint(1, 5)
    x = randint(0, game.width)
    y = randint(0, game.height)
    position = Vec2(x, y)

    return Item(position, energy)


def pick_item(items: list[Item], position: Vec2) -> tuple[list[Item], int]:
    sum = 0
    for item in items:
        if item.position.x == position.x and item.position.y == position.y:
            sum += item.energy
            items.remove(item)

    return (items, sum)
