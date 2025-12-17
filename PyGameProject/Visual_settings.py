import pygame

def run_pygame_window(game):
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Osiris Laboratory")


    font = pygame.font.SysFont("arial", 26)
    big_font = pygame.font.SysFont("arial", 42)
    clock = pygame.time.Clock()

    play_button = pygame.Rect(300, 300, 200, 60)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game.start_game()

        window.fill((20, 5, 35))

        if game.state == "menu":
            title = big_font.render("Osiris Laboratory", True, (220, 200, 255))
            window.blit(title, (200, 150))

            pygame.draw.rect(window, (120, 90, 180), play_button)
            play_text = font.render("PLAY", True, (255, 255, 255))
            window.blit(play_text, (play_button.x + 70, play_button.y + 15))

        elif game.state == "playing":
            info = font.render("Gameplay started! (logic connected)", True, (200, 255, 200))
            window.blit(info, (180, 300))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
