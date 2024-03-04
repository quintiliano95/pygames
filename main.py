import pygame as pg

pg.init()

# Cria janela do game
window = pg.display.set_mode(size=(800, 600))

# Carrega a imagem de fundo
bg_surf = pg.image.load('./images/montanha.jpg').convert_alpha()
player1_surf = pg.image.load('./images/Ship1.png').convert_alpha()

# Obter o retângulo a partir da superfície
bg_rect = bg_surf.get_rect(left=0, top=0)
player1_rect = player1_surf.get_rect(left=100, top=100)

# Desenha na janela
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pg.display.flip()

# Colocar relógio
clock = pg.time.Clock()

while True:
    clock.tick(240)
    print(f'{clock.get_fps() :.0f}')
    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('ACABOUUU')
            pg.quit()
            quit()

    # Pega a tecla pressionada
    pressed_key = pg.key.get_pressed()

    if pressed_key[pg.K_p]:
        pg.mixer_music.load('./sounds/french.mp3')
        pg.mixer_music.play()

    if pressed_key[pg.K_w]:
        player1_rect.centery -= 1

    if pressed_key[pg.K_s]:
        player1_rect.centery += 1

    if pressed_key[pg.K_a]:
        player1_rect.centerx -= 1

    if pressed_key[pg.K_d]:
        player1_rect.centerx += 1
