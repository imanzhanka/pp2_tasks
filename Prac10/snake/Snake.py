import pygame
import random

pygame.init()

# --- Constants ---
WIDTH = 600
HEIGHT = 600
CELL = 30                    # Size of each grid cell in pixels
FPS_BASE = 5                 # Starting frames per second (snake speed)
FPS_INCREMENT = 2            # Extra FPS added per level
FOOD_PER_LEVEL = 3           # How many foods collected to advance a level

# --- Colors ---
colorBLACK  = (0, 0, 0)
colorWHITE  = (255, 255, 255)
colorGRAY   = (50, 50, 50)
colorRED    = (220, 50, 50)
colorYELLOW = (240, 200, 50)
colorGREEN  = (50, 200, 80)
colorBLUE   = (50, 120, 220)
colorORANGE = (255, 140, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font_big   = pygame.font.SysFont("monospace", 32, bold=True)
font_small = pygame.font.SysFont("monospace", 20)


# --- Helper: draw the background grid ---
def draw_grid():
    """Draw thin gray grid lines over the black background."""
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY,
                             (i * CELL, j * CELL, CELL, CELL), 1)


# --- Point: simple 2-D grid coordinate ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"{self.x}, {self.y}"


# --- Snake ---
class Snake:
    def __init__(self):
        # Initial body: three segments moving right
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1   # horizontal velocity (grid cells per tick)
        self.dy = 0   # vertical velocity

    def move(self):
        """Shift every segment one step, then update the head."""
        # Move each segment to the position of the one ahead of it
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Advance the head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def is_out_of_bounds(self):
        """
        Return True if the snake's head has left the playing area.
        (Wall collision → game over instead of wrapping.)
        """
        head = self.body[0]
        return (head.x < 0 or head.x >= WIDTH  // CELL or
                head.y < 0 or head.y >= HEIGHT // CELL)

    def is_self_collision(self):
        """Return True if the head overlaps any body segment."""
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def occupies(self, x, y):
        """Return True if any snake segment sits at (x, y)."""
        return any(s.x == x and s.y == y for s in self.body)

    def grow(self):
        """Append a new segment at the tail position."""
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def check_food_collision(self, food):
        """
        Return True if the head touched the food.
        Growing and repositioning the food is handled outside.
        """
        head = self.body[0]
        return head.x == food.pos.x and head.y == food.pos.y

    def draw(self):
        """Draw the snake: red head, yellow body segments."""
        head = self.body[0]
        pygame.draw.rect(screen, colorRED,
                         (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW,
                             (segment.x * CELL, segment.y * CELL, CELL, CELL))


# --- Food ---
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def generate_random_pos(self, snake):
        """
        Place food at a random cell that is NOT occupied by the snake.
        Keeps retrying until a free cell is found.
        """
        while True:
            x = random.randint(0, WIDTH  // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if not snake.occupies(x, y):   # avoid spawning on the snake
                self.pos.x = x
                self.pos.y = y
                break

    def draw(self):
        """Draw the food as a green square."""
        pygame.draw.rect(screen, colorGREEN,
                         (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


# --- HUD: score, level, speed ---
def draw_hud(score, level, fps):
    """Render score, level, and speed in the top-left corner."""
    score_surf = font_small.render(f"Score: {score}", True, colorWHITE)
    level_surf = font_small.render(f"Level: {level}", True, colorORANGE)
    speed_surf = font_small.render(f"Speed: {fps} FPS", True, colorBLUE)
    screen.blit(score_surf, (8, 6))
    screen.blit(level_surf, (8, 28))
    screen.blit(speed_surf, (8, 50))


# --- Game-over / level-up overlay ---
def draw_message(title, subtitle=""):
    """Draw a centered message box (game over or level up)."""
    title_surf = font_big.render(title, True, colorRED)
    sub_surf   = font_small.render(subtitle, True, colorWHITE)
    tw = title_surf.get_width()
    sw = sub_surf.get_width()
    screen.blit(title_surf, ((WIDTH - tw) // 2, HEIGHT // 2 - 40))
    screen.blit(sub_surf,   ((WIDTH - sw) // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(2000)   # pause 2 s so the player can read it


# ============================================================
# Main game loop
# ============================================================
def main():
    clock = pygame.time.Clock()

    # --- Game state ---
    score         = 0       # total foods eaten
    level         = 1       # current level
    food_in_level = 0       # foods eaten in the current level
    fps           = FPS_BASE  # current tick rate = snake speed

    snake = Snake()
    food  = Food()
    food.generate_random_pos(snake)   # ensure food does not start on the snake

    running = True
    game_over = False

    while running:
        # ---- Event handling ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if not game_over:
                    # Prevent 180-degree turns (can't reverse directly)
                    if event.key == pygame.K_RIGHT and snake.dx == 0:
                        snake.dx, snake.dy = 1, 0
                    elif event.key == pygame.K_LEFT and snake.dx == 0:
                        snake.dx, snake.dy = -1, 0
                    elif event.key == pygame.K_DOWN and snake.dy == 0:
                        snake.dx, snake.dy = 0, 1
                    elif event.key == pygame.K_UP and snake.dy == 0:
                        snake.dx, snake.dy = 0, -1
                else:
                    # Any key restarts after game over
                    main()
                    return

        if not game_over:
            # ---- Update ----
            snake.move()

            # Wall collision → game over
            if snake.is_out_of_bounds():
                draw_message("GAME OVER", f"Score: {score}  |  Press any key")
                game_over = True
                continue

            # Self collision → game over
            if snake.is_self_collision():
                draw_message("GAME OVER", f"Score: {score}  |  Press any key")
                game_over = True
                continue

            # Food collision
            if snake.check_food_collision(food):
                score         += 1
                food_in_level += 1
                snake.grow()
                food.generate_random_pos(snake)   # safe spawn

                # --- Level-up check ---
                if food_in_level >= FOOD_PER_LEVEL:
                    level         += 1
                    food_in_level  = 0
                    fps           += FPS_INCREMENT  # increase snake speed
                    draw_message(f"LEVEL {level}!", f"Speed up!  FPS → {fps}")

            # ---- Draw ----
            screen.fill(colorBLACK)
            draw_grid()
            food.draw()
            snake.draw()
            draw_hud(score, level, fps)
            pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()