import pygame


def draw():
    for i in range(H_SIZE // SIZE):
        for j in range(W_SIZE // SIZE):
            if plocha[i][j] == 1:
                pygame.draw.rect(window, black, [j * SIZE, i * SIZE, SIZE, SIZE])
    window.blit(mravec, [mravec_pos[0] * SIZE, mravec_pos[1] * SIZE])


def move(start_dir, mravec_pos):
    # menenie bunky
    if plocha[mravec_pos[1]][mravec_pos[0]] == 1:
        plocha[mravec_pos[1]][mravec_pos[0]] = 0
    else:
        plocha[mravec_pos[1]][mravec_pos[0]] = 1
    # pohyb mravca
    if mravec_dir == 'r':
        mravec_pos[0] += 1
    elif mravec_dir == 'd':
        mravec_pos[1] += 1
    elif mravec_dir == 'l':
        mravec_pos[0] -= 1
    else:
        mravec_pos[1] -= 1
    # obidenie hranic
    if mravec_pos[0] < 0:
        mravec_pos[0] = W_SIZE // SIZE - 1
    elif mravec_pos[0] > W_SIZE // SIZE - 1:
        mravec_pos[0] = 0
    elif mravec_pos[1] < 0:
        mravec_pos[1] = H_SIZE // SIZE - 1
    elif mravec_pos[1] > H_SIZE // SIZE - 1:
        mravec_pos[1] = 0
    # zmena smeru
    if plocha[mravec_pos[1]][mravec_pos[0]] == 0:
        start_dir -= 1
        if start_dir < 0:
            start_dir = 3
    else:
        start_dir += 1
        if start_dir > 3:
            start_dir = 0
    return start_dir


white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
W_SIZE = 800
H_SIZE = 600
SIZE = 5
window = pygame.display.set_mode((W_SIZE, H_SIZE))
pygame.display.set_caption("Langtonov mravec")
done = False
plocha = []
start_dir = 3
directions = ['u', 'r', 'd', 'l']
mravec_dir = directions[start_dir]
mravec_pos = [(W_SIZE // SIZE) // 2, (H_SIZE // SIZE) // 2]
# zalozenie plochy
for i in range(H_SIZE // SIZE):
    riadok = []
    for j in range(W_SIZE // SIZE):
        riadok.append(0)
    plocha.append(riadok)

mravec = pygame.image.load("img/mravec.png")
clock = pygame.time.Clock()
# hlavny cyklus
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    window.fill(white)
    draw()
    start_dir = move(start_dir, mravec_pos)
    mravec_dir = directions[start_dir]
    pygame.display.flip()
    clock.tick(0)
