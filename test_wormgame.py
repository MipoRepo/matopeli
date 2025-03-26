import pytest
from wormgame import Snake, Apple, WIDTH, HEIGHT, CELL_SIZE  # Muista, että pääkoodin tiedoston nimi on "wormgame.py"

# Testaa Snake-luokan alustus
def test_snake_initialization():
    snake = Snake()
    assert snake.body == [(100, 100), (80, 100), (60, 100)]
    assert snake.direction == (CELL_SIZE, 0)

# Testaa Snake-luokan liikkuminen
def test_snake_move():
    snake = Snake()
    snake.move()
    assert snake.body[0] == (120, 100)  # Pään tulisi liikkua oikealle
    assert snake.body[-1] == (80, 100)  # Hännän viimeinen segmentti katoaa

# Testaa Snake-luokan kasvaminen
def test_snake_grow():
    snake = Snake()
    initial_length = len(snake.body)
    snake.grow()
    assert len(snake.body) == initial_length + 1
    assert snake.body[-1] == snake.body[-2]  # Viimeinen segmentti on kopio toiseksi viimeisestä

# Testaa Snake-luokan törmäystarkistus
def test_snake_collision():
    snake = Snake()
    # Simuloidaan törmäys itseen
    snake.body = [(100, 100), (80, 100), (100, 100)]
    assert snake.check_collision() is True

    # Simuloidaan törmäys pelialueen ulkopuolelle
    snake.body = [(WIDTH, 0)]
    assert snake.check_collision() is True

    # Ei törmäystä
    snake.body = [(100, 100), (80, 100), (60, 100)]
    assert snake.check_collision() is False

# Testaa Apple-luokan sijainti
def test_apple_spawn():
    apple = Apple()
    x, y = apple.position
    assert 0 <= x < WIDTH
    assert 0 <= y < HEIGHT
    assert x % CELL_SIZE == 0
    assert y % CELL_SIZE == 0

# Testaa Apple-luokan uudelleensyntyminen
def test_apple_respawn():
    apple = Apple()
    initial_position = apple.position
    apple.respawn()
    assert apple.position != initial_position  # Omenan sijainnin tulisi muuttua
