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

