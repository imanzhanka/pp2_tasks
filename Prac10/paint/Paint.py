import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    tool = 'brush'   # brush / rect / circle / eraser

    drawing = False
    start_pos = (0, 0)
    points = []

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # 🎨 COLOR SELECTION
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # 🛠 TOOLS
                elif event.key == pygame.K_1:
                    tool = 'rect'
                elif event.key == pygame.K_2:
                    tool = 'circle'
                elif event.key == pygame.K_3:
                    tool = 'eraser'
                elif event.key == pygame.K_4:
                    tool = 'brush'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'brush':
                        points.append(event.pos)
                        points = points[-256:]

                    elif tool == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)

        # background
        # (important: do NOT clear screen if you want persistent drawing)
        # screen.fill((0, 0, 0))

        # DRAW BRUSH
        if tool == 'brush':
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        # DRAW SHAPES (preview while dragging)
        if drawing:
            current_pos = pygame.mouse.get_pos()
            color = get_color(mode)

            if tool == 'rect':
                rect = pygame.Rect(start_pos, (current_pos[0] - start_pos[0],
                                               current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)

            elif tool == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                radius_circle = int((dx**2 + dy**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius_circle, 2)

        pygame.display.flip()
        clock.tick(60)


def get_color(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)


def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(color_mode)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations if iterations != 0 else 0
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)


main()