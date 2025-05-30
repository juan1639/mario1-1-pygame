import pygame
from settings import *
from funciones import *
from tilemaps import TILE_MAP
from marioniveles import NIVEL_1_1

# ====================================================================================
#   main.py (modulo principal) ... clase principal --> class Game
#
# ------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pygame.init()

        # Colores y constantes
        self.COL = Colores()
        self.CO = Constantes()

        # Marcadores: ptos, nivel, vidas...
        self.nivel = 1
        self.puntos = 0
        self.vidas = 3

        # Listas updates (tomas de tiempo/temporizadores)
        self.ultimo_update = {
            "estrella": pygame.time.get_ticks(),
        }

        # True= Se ejecuta el bucle Principal | False= no se ejecuta
        self.program_running = True

        # Estados del juego
        self.estado_juego = {
            "menu_presentacion": True,
            "preparado": False,
            "en_juego": False,
            "game_over": False,
            "nivel_superado": False
        }

        # Inicializar listas con sprites
        self.listas_sprites = {
            "all_sprites": pygame.sprite.Group(),
            "mario": pygame.sprite.Group(),
            "escenario": pygame.sprite.Group(),
            "textos": pygame.sprite.Group(),
        }

        # Instanciar textos en 'Menu-presentacion
        self.instanciar_texto("Clon Mario", 135, self.CO.RESOLUCION[0] // 2, 220, self.COL.NARANJA, negrita=True)
        self.instanciar_texto("Pulse ENTER para comenzar...", 32, self.CO.RESOLUCION[0] // 2, self.CO.RESOLUCION[1] - 80, 
            self.COL.AMARILLENTO)

        # Pantalla y reloj
        self.pantalla = pygame.display.set_mode(self.CO.RESOLUCION)
        self.reloj = pygame.time.Clock()

        # TILES (key=numero-tile : value=archivo.png)
        self.num_tile = {
            1: None,
            14: self.obtener_grafico("smb-interrogacion.png"),
            15: self.obtener_grafico("smb-block-ladrillo.png"),
            16: self.obtener_grafico("smb-block-piramide.png"),
            40: self.obtener_grafico("smb-suelo.png"),
        }

        # INICIALIZAR/RESETEAR el scroll
        self.scroll_x = 0

        # Cargar sonidos del modulo settings
        #self.sonidos = Sonidos()
    
    def obtener_indice(self, x, y):
        """Obtener índice en el laberinto 1D basado en coordenadas 2D."""
        return y * self.CO.COLUMNAS + x if 0 <= x < self.CO.COLUMNAS and 0 <= y < self.CO.FILAS else None
    
    def crear_pantalla_nivel(self):
        """Crear el laberinto y los tiles correspondientes."""
        #self.draw_tilemap()
        self.draw_tilemap()
    
    def vaciar_listas(self):
        """Vaciar todas las listas de sprites."""
        for grupo in self.listas_sprites.values():
            grupo.empty()
    
    def resetear_estados_juego(self):
        self.estado_juego = {clave: False for clave in self.estado_juego}
    
    def new_game(self):
        """Preparar un nuevo nivel o juego."""
        self.vaciar_listas()
        self.crear_pantalla_nivel()
        self.instanciar_objetos()
        self.instanciar_textos_iniciales()
        self.sonidos.reproducir("inicio_nivel")
    
    def obtener_grafico(self, nombrePng):
        """Devolver una imagen y un rectangulo."""
        img = pygame.image.load(f"{self.CO.RUTA_ASSETS_IMG}{nombrePng}").convert()
        escalaX = self.CO.TILE_X
        escalaY = self.CO.TILE_Y
        image = pygame.transform.scale(img, (escalaX, escalaY))
        image.set_colorkey((255, 255, 255))
        rect = image.get_rect()
        
        return (image, rect)
    
    """ def draw_tilemap(self):
        for y, row in enumerate(TILE_MAP):
            for x, tile in enumerate(row):
                if self.num_tile[tile]:
                    self.pantalla.blit(self.num_tile[tile], (x * self.CO.TILE_X, y * self.CO.TILE_Y)) """
    
    """ def draw_tilemap_mario1_1(self):
        for y in range(self.CO.ESCENARIO_FILAS):
            for x in range(self.CO.ESCENARIO_COLUMNAS):
                index = y * 212 + x
                tile = NIVEL_1_1[index]
                if 14 <= tile <= 16 or tile == 40:
                    self.pantalla.blit(self.num_tile[tile][0], (x * self.CO.TILE_X, y * self.CO.TILE_Y)) """
    
    def draw_tilemap(self):
        tiles_en_pantalla_x = self.pantalla.get_width() // self.CO.TILE_X
        start_tile_x = self.scroll_x // self.CO.TILE_X

        for y in range(self.CO.ESCENARIO_FILAS):
            for x in range(tiles_en_pantalla_x + 1):  # +1 para cubrir borde derecho
                tile_index = y * self.CO.ESCENARIO_COLUMNAS + (start_tile_x + x)

                if tile_index >= len(NIVEL_1_1):
                    continue  # fuera del mapa

                tile = NIVEL_1_1[tile_index]

                if 14 <= tile <= 16 or tile == 40:
                    # Calcula posición en pantalla relativa al scroll
                    pantalla_x = x * self.CO.TILE_X - (self.scroll_x % self.CO.TILE_X)
                    pantalla_y = y * self.CO.TILE_Y
                    self.pantalla.blit(self.num_tile[tile][0], (pantalla_x, pantalla_y))
    
    def instanciar_objetos(self):
        """Instanciar/re-instanciar Pacman, fantasmas, etc..."""

        if self.vidas < 0:
            self.ir_gameover()
            return
    
    def instanciar_mario_dies(self, x, y):
        pass

    def instanciar_textos_iniciales(self):
        """Instanciar textos marcadores, Preparado..."""
        #instanciar_textos(self)
    
    def instanciar_texto(self, txt, size, x, y, color, fondo=None, negrita=False, centrado=True, tipo=None):
        """Instanciar un texto y agregarlo a su lista correspondiente..."""
        #newTxt = Textos(self, txt, size, x, y, color, fondo, negrita, centrado, tipo)
        #self.listas_sprites["textos"].add(newTxt)
    
    """ def ir_gameover(self):
        print('game over')

        self.resetear_estados_juego()
        self.estado_juego["game_over"] = True

        self.instanciar_texto(' Game Over ', 120, (self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES) // 2,
            300, self.COL.NARANJA_ROJIZO_2, fondo=self.COL.BG_GRIS_OSCURO, negrita=True, tipo="gameover")

        self.instanciar_texto("  ENTER - Volver a jugar      ESC - Salir  ", 32, (self.CO.RESOLUCION[0] - self.CO.ZONA_SCORES) // 2,
            self.CO.RESOLUCION[1] // 1.5, self.COL.VERDE_FONDO, fondo=self.COL.BG_GRIS_OSCURO, negrita=True, centrado=True)

        self.sonidos.reproducir("gameover_retro") """

    def update(self):
        pygame.display.set_caption(str(int(self.reloj.get_fps())))

        #updates_segun_estado(self)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.scroll_x += 5
        if keys[pygame.K_LEFT] and self.scroll_x > 0:
            self.scroll_x -= 5
        
        pygame.display.flip()
        self.reloj.tick(self.CO.FPS)
    
    def draw(self):
        self.pantalla.fill(self.COL.AZUL_CELESTE_FONDO)

        self.draw_tilemap()
        #draw_listas_sprites(self)
    
    def check_event(self):
        """Eventos (Quit/Comenzar...)"""
        eventos_comenzar_quit_etc(self)
    
    def bucle_principal(self):
        """BUCLE PRINCIPAL del Juego"""
        while self.program_running:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.bucle_principal()

