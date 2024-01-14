import pygame

from typing import Optional
from snake import *


def update(game: 'Game', snake_input: int, SPEED: int, SPAWN_RATE: int) -> 'Game':
    snake = turn_snake(game.snake, snake_input)
    items = game.items

    if game.frame % SPEED == 0:
        snake = move_snake(snake)

    if game.frame % SPAWN_RATE == 0:
        new_item = generate_item(game)
        for i in items:
            if i.position == new_item.position:
                break
        else:
            items = items + [new_item]

    items, energy = pick_item(items, snake.positions[0])

    alive = snake.alive and not collision(snake, game.width, game.height)

    return Game(
        Snake(snake.positions, snake.direction, alive, snake.grow + energy),
        game.width, game.height, game.frame + 1, items
    )


def draw(screen: pygame.Surface, game: 'Game'):
    tile_width = screen.get_width() / game.width
    tile_height = (screen.get_height() - 30) / game.height

    for x in range(game.width):
        for y in range(game.height):
            if x % 2 != y % 2:
                pygame.draw.rect(screen, (0, 40, 0),
                                 (x * tile_width, y * tile_height,
                                  tile_width, tile_height))

    color = (255, 255, 0)
    for pos in game.snake.positions:
        pygame.draw.rect(screen, color if game.snake.alive else (0, 0, 0),
                         (pos.x * tile_width, pos.y * tile_height,
                          tile_width, tile_height))
        color = (255, color[1] // 2, 0)
        pygame.draw.rect(screen, color if game.snake.alive else (0, 0, 0),
                         (pos.x * tile_width, pos.y * tile_height,
                          tile_width, tile_height), 4)

    for item in game.items:
        pos = item.position
        pygame.draw.circle(screen, (255, 255 - item.energy * 50, 255 - item.energy * 50),
                           ((pos.x + 0.5) * tile_width, (pos.y + 0.5) * tile_height),
                           (tile_width / 2.5))


def main(game: Optional['Game'], resolution: tuple[int, int], fps: int,
         SPEED: int, SPAWN_RATE: float):
    pygame.display.init()
    pygame.display.set_caption("Snake")
    pygame.font.init()
    font = pygame.font.SysFont('', 40)
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((resolution[0], resolution[1] + 30))

    while True:
        screen.fill((0, 20, 0))
        snake_input = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake_input = -1

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake_input = 1

                elif event.key == pygame.K_SPACE:
                    snake_input = 42

        if game:
            if game.snake.alive:
                game = update(game, snake_input, int(fps / SPEED), int(SPAWN_RATE * fps))

            elif snake_input == 42:
                game = Game(Snake([Vec2(1, 1)], Vec2(1, 0), True, 5), 40, 40, 0, [])

            draw(screen, game)
            pygame.draw.rect(screen, (0, 0, 0), (0, resolution[1], resolution[0], 30))
            score = font.render(f'time: {game.frame // fps}s - score: {len(game.snake.positions)} - speed: {SPEED} - spawn rate: {SPAWN_RATE}s', False, (255, 100, 100))
            screen.blit(score, (0, resolution[1]))

            if not game.snake.alive:
                game_over = font.render('- GAME OVER -', False, (255, 100, 100))
                restart = font.render("press SPACE to restart", False, (255, 100, 100))
                c_game_over = game_over.get_rect(center=(resolution[0] / 2, resolution[1] / 2))
                c_restart = restart.get_rect(center=(resolution[0] / 2, resolution[1] / 2 + resolution[1] // 10))
                screen.blit(game_over, c_game_over)

                if pygame.time.get_ticks() % 1000 > 500:
                    screen.blit(restart, c_restart)

        pygame.display.flip()
        fpsClock.tick(fps)


def new_game() -> Optional['Game']:
    return (Game(
        Snake([Vec2(1, 1)], Vec2(1, 0), True, 5),
        40, 40, 0, []
        ) if 'Game' in dir() else None
    )


if __name__ == '__main__':

    # ---------------- Settings you can change ---------------- #
    SPEED = 10      # speed of the snake in tiles per second
    SPAWN_RATE = 4  # spawn rate of items (every X seconds)
    # --------------------------------------------------------- #

    game = (Game(
        Snake([Vec2(1, 1)], Vec2(1, 0), True, 5),
        40, 40, 0, []
        ) if 'Game' in dir() else None
    )
    main(game, resolution=(680, 680), fps=60, SPEED=SPEED, SPAWN_RATE=SPAWN_RATE)
