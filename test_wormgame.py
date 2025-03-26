# test_wormgame.py
# Yksikkötestit matopelin tärkeimmille törmäystarkistuksille
import pytest
# Tarkistaa osuuko mato ruudun ulkopuolelle (seinään)
def tormaako_seinaan(x, y, leveys, korkeus):
    return x < 0 or x >= leveys or y < 0 or y >= korkeus

# Tarkistaa osuuko mato itseensä
def tormaako_itseensa(mato_lista):
    pää = mato_lista[-1] # pään koordinaatit
    return pää in mato_lista[:-1] # Onko pää osa muuta matoa

# Testaa seinään törmäämistä:
def test_tormaako_seinaan():
    # Pitäisi törmätä: vasemmalta ulos, oikealta ulos, ylhäältä ulos, alhaalta ulos
    assert tormaako_seinaan(-10, 50, 600, 400)
    assert tormaako_seinaan(600, 100, 600, 400)
    assert not tormaako_seinaan(100, 100, 600, 400)

# Testaa itseensä törmäämistä:
def test_tormaako_itseensa():
    mato = [[100, 100], [110, 100], [120, 100], [130, 100], [120, 100]]
    # Pitäisi törmätä: mato on törmännyt itseensä
    mato2 = [[100, 100], [110, 100], [120, 100], [130, 100], [140, 100]]
    #
    assert tormaako_itseensa(mato)
    assert not tormaako_itseensa(mato2)
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or self.body[0] in self.body[1:]:
        return True
    return False

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] and new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Omenaluokka
class Apple:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    
    def respawn(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Pelisilmukka
snake = Snake()
apple = Apple()
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    snake.move()
    
    if snake.body[0] == apple.position:
        snake.grow()
        apple.respawn()

    if snake.check_collision():
        running = False

    snake.draw(screen)
    apple.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
