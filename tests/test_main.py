import pytest
import pygame as pg

# Inicializa o Pygame antes de tudo
pg.init()
pg.display.set_mode((800, 600))


def test_pygame_init():
    """Verifica se o Pygame inicializa corretamente"""
    assert pg.get_init() is True


def test_window_creation():
    """Verifica se a janela do jogo é criada"""
    window = pg.display.set_mode((800, 600))
    assert window is not None


def test_load_images():
    """Verifica se as imagens carregam corretamente"""
    try:
        bg_surf = pg.image.load('./images/montanha.jpg').convert_alpha()
        player1_surf = pg.image.load('./images/Ship1.png').convert_alpha()
        assert bg_surf is not None
        assert player1_surf is not None
    except pg.error:
        pytest.fail("Erro ao carregar as imagens")


def test_player_movement():
    """Verifica se o player se move corretamente"""
    player_rect = pg.Rect(100, 100, 50, 50)  # Simula um retângulo do player

    # Simula teclas pressionadas
    keys = {pg.K_w: True, pg.K_s: False, pg.K_a: False, pg.K_d: True}

    # Aplica o movimento com base nas teclas pressionadas
    if keys[pg.K_w]:
        player_rect.y -= 2  # Move para cima
    if keys[pg.K_s]:
        player_rect.y += 1  # Move para baixo
    if keys[pg.K_a]:
        player_rect.x -= 1  # Move para a esquerda
    if keys[pg.K_d]:
        player_rect.x += 1  # Move para a direita

    assert player_rect.x == 101  # Moveu para a direita corretamente
    assert player_rect.y == 99   # Moveu para cima corretamente


def test_quit_event():
    """Verifica se o evento QUIT é processado corretamente"""
    quit_event = pg.event.Event(pg.QUIT)
    pg.event.post(quit_event)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            assert event.type == pg.QUIT
            return

    pytest.fail("Evento QUIT não foi capturado")


if __name__ == "__main__":
    pytest.main()
