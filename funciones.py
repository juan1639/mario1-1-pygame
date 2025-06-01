import pygame
import sys
from varios import Textos

# ========================================================================
#   Modulo de funciones (que no pertenecen a ninguna class)
#   
#   (La mayoria estaban ubicadas en el modulo main.py y han sido...
#    ... trasladadas aqui para reducir código en main.py)
# ------------------------------------------------------------------------
""" def colision_en_tile(self, x, y):
    if 0 <= y < len(TILE_MAP) and 0 <= x < len(TILE_MAP[0]):
        return TILE_MAP[y][x] != 0
    return False """




def asociar_tiles_a_imagenes(game):
    return {
        1: None,
        2: game.obtener_grafico("smb-nube-2.png"),
        3: game.obtener_grafico("smb-nube-3.png"),
        4: game.obtener_grafico("smb-nube-4.png"),
        5: game.obtener_grafico("smb-mastil-bola.png"),
        6: game.obtener_grafico("smb-nube-6.png"),
        7: game.obtener_grafico("smb-nube-7.png"),
        8: game.obtener_grafico("smb-nube-8.png"),
        9: game.obtener_grafico("smb-mastil-bandera2.png"),
        10: game.obtener_grafico("smb-mastil-bandera1.png"),
        11: None,
        12: None,
        13: game.obtener_grafico("smb-mastil-1.png"),
        14: game.obtener_grafico("smb-interrogacion.png"),
        15: game.obtener_grafico("smb-block-ladrillo.png"),
        16: game.obtener_grafico("smb-block-piramide.png"),
        17: game.obtener_grafico("smb-mastil-2.png"),
        18: None,
        19: None,
        20: game.obtener_grafico("smb-castillo-20.png"),
        21: game.obtener_grafico("smb-tuberia-arriba-iz.png"),
        22: game.obtener_grafico("smb-tuberia-arriba-de.png"),
        23: game.obtener_grafico("smb-castillo-ventana-de.png"),
        24: game.obtener_grafico("smb-castillo-block-ladrillos.png"),
        25: game.obtener_grafico("smb-castillo-ventana-iz.png"),
        26: game.obtener_grafico("smb-hierba-26.png"),
        27: game.obtener_grafico("smb-tuberia-abajo-iz.png"),
        28: game.obtener_grafico("smb-tuberia-abajo-de.png"),
        29: game.obtener_grafico("smb-castillo-29.png"),
        30: game.obtener_grafico("smb-monticulo-iz.png"),
        31: game.obtener_grafico("smb-monticulo-centro.png"),
        32: game.obtener_grafico("smb-monticulo-de.png"),
        33: game.obtener_grafico("smb-castillo-33.png"),
        34: game.obtener_grafico("smb-monticulo-34.png"),
        35: game.obtener_grafico("smb-monticulo-35.png"),
        36: game.obtener_grafico("smb-hierba-36.png"),
        37: game.obtener_grafico("smb-hierba-37.png"),
        38: game.obtener_grafico("smb-hierba-38.png"),
        39: game.obtener_grafico("smb-castillo-39.png"),
        40: game.obtener_grafico("smb-suelo.png"),
    }






def instanciar_textos(self):
    MARGEN = 9

    self.instanciar_texto("Puntos", 48, self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES + MARGEN,
        self.CO.TY, self.COL.AMARILLENTO, negrita=True, centrado=False)
    self.instanciar_texto("Nivel", 48, self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES + MARGEN,
        self.CO.TY * 4, self.COL.AMARILLENTO, negrita=True, centrado=False)
    self.instanciar_texto("0", 48, self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES + MARGEN,
        self.CO.TY * 2, self.COL.BLANCO, negrita=True, centrado=False, tipo="dinamico-puntos")
    self.instanciar_texto(str(self.nivel), 48, self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES + MARGEN,
        self.CO.TY * 5, self.COL.BLANCO, negrita=True, centrado=False, tipo="dinamico-nivel")




def updates_segun_estado(self):
    """Updates condicionales (presentacion/preparado/en_juego...)"""

    #checkNivelSuperado(self)
    #checkDelayNextLevel(self)

    if self.estado_juego["menu_presentacion"]:
        self.listas_sprites["textos"].update()
    else:
        self.listas_sprites["all_sprites"].update()
        self.listas_sprites["textos"].update()





""" def checkNivelSuperado(self):
    if self.estado_juego["nivel_superado"]:
        return
     
    if len(self.listas_sprites["puntitos"]) <= 0 and self.estado_juego["en_juego"]:
        self.sonidos.sonidos["fantasmas_azules"].stop()
        self.estado_juego["en_juego"] = False
        self.estado_juego["nivel_superado"] = True
        self.ultimo_update["nivel_superado_delay"] = pygame.time.get_ticks()
        self.sonidos.reproducir("intermision")
        print("nivel superado!") """



""" def checkDelayNextLevel(self):
    if not self.estado_juego["nivel_superado"]:
        return
    
    calculo = pygame.time.get_ticks()
    if calculo - self.ultimo_update["nivel_superado_delay"] > self.CO.DELAY_NEXT_LEVEL:
        self.nivel += 1
        self.resetear_estados_juego()
        self.estado_juego["preparado"] = True
        self.ultimo_update["preparado"] = pygame.time.get_ticks()
        self.new_game() """





def draw_listas_sprites(self):
    """Renderizar las listas-sprites"""
    self.listas_sprites["all_sprites"].draw(self.pantalla)
    self.listas_sprites["textos"].draw(self.pantalla)





def eventos_comenzar_quit_etc(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.program_running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.program_running = False
                pygame.quit()
                sys.exit()
            
            if (event.key == pygame.K_RETURN and self.estado_juego["menu_presentacion"]) or (event.key == pygame.K_RETURN and self.estado_juego["game_over"]):
                pygame.mixer.music.stop()
                self.resetear_estados_juego()
                self.estado_juego["preparado"] = True
                self.estado_juego["en_juego"] = True
                self.ultimo_update["preparado"] = pygame.time.get_ticks()

                if self.vidas <= 0:
                    self.vidas = 3
                    self.puntos = 0
                    self.nivel = 1
                
                # ************** Comenzar partida (Pulsando ENTER) ***********************
                self.new_game()

            if event.key == pygame.K_TAB:
                for clave in self.estado_juego:
                    print(clave, self.estado_juego[clave])






def eliminar_elemento_de_lista(self, lista, elemento):
    for sprite in self.listas_sprites[lista]:
        if isinstance(sprite, Textos) and sprite.tipo == elemento:
            self.listas_sprites["textos"].remove(sprite)
            break

