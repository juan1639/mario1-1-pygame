import pygame

# ====================================================================================
#	settings.py (modulo de configuraciones)
# 
# ------------------------------------------------------------------------------------
class Colores:
    AMARILLO = (220, 190, 0)
    AMARILLENTO = (250, 245, 130)
    NARANJA = (250, 142, 12)
    NARANJA_ROJIZO = (255, 100, 12)
    NARANJA_ROJIZO_2 = (255, 45, 12)
    BLANCO = (240, 240, 240)
    GRIS_FONDO = (59, 59, 59)
    BG_GRIS_OSCURO = (49, 49, 50)
    ROJO = (230, 30, 20)
    VERDE_FONDO = (20, 240, 30)
    AZUL_CELESTE_FONDO = (100, 170, 180)




class Constantes:
    # 256 x 240 px --> 16 x 15 tiles --> 16 x 16 px (1 tile = 1 sprite)
    ESCALA = 3
    TILE_X, TILE_Y = 16 * ESCALA, 16 * ESCALA   # Tamano de los Tiles (x Escala)
    FILAS, COLUMNAS = 15, 24                    # Filas x Columnas (15, 16)
    ESCENARIO_FILAS, ESCENARIO_COLUMNAS = 15, 212 # Total Pantalla (212 ancho x 15 alto)
    MARIO_INI_POS = (5, 9)
    INVULNERABLE = False
    RESOLUCION = (TILE_X * COLUMNAS, TILE_Y * FILAS) # Calculo de la pantalla 256x240px(* escala))
    RUTA_ASSETS_IMG = 'assets/img/'
    RUTA_ASSETS_AUDIO = 'assets/audio/'
    FPS = 100





class Sonidos:
    def __init__(self):
        pygame.mixer.init()

        self.ruta_audio = Constantes.RUTA_ASSETS_AUDIO
        self.sonidos = self.cargar_sonidos()
    


    def cargar_sonidos(self):
        """Cargar todos los sonidos en un diccionario."""

        return {
            "bricks_fall": self.cargar_sonido(f"{self.ruta_audio}bricks-fall.mp3"),
            "fireworks": self.cargar_sonido(f"{self.ruta_audio}fireworks.mp3"),
            "gameover": self.cargar_sonido(f"{self.ruta_audio}gameover_mario.mp3"),
            "salto": self.cargar_sonido(f"{self.ruta_audio}jumpbros.ogg"),
            "musica-secundaria-tuberias": self.cargar_sonido(f"{self.ruta_audio}mario-tuberias.mp3"),
            "musica-principal": self.cargar_sonido(f"{self.ruta_audio}musica-mario-bros.mp3"),
            "oh_no": self.cargar_sonido(f"{self.ruta_audio}oh-no.mp3"),
            "ough": self.cargar_sonido(f"{self.ruta_audio}ough.mp3"),
            "moneda": self.cargar_sonido(f"{self.ruta_audio}p-ping.mp3"),
            "wall": self.cargar_sonido(f"{self.ruta_audio}wall.wav")
        }

    """ def cargar_sonido(self, ruta, volumen=1.0):
        sonido = pygame.mixer.Sound(ruta)
        sonido.set_volume(volumen)
        return sonido """
    

    
    def cargar_sonido(self, ruta, volumen=1.0):
        try:
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(volumen)
            return sonido
        
        except pygame.error as e:
            print(f"[ERROR] No se pudo cargar el sonido '{ruta}': {e}")
            return None
    

    
    def reproducir(self, nombre, duracion=None):
        """Reproduce un sonido si está en el diccionario."""
        if nombre in self.sonidos and nombre == "musica-principal":
            self.sonidos[nombre].play(loops=-1)
        
        elif nombre in self.sonidos:
            if duracion == None:
                self.sonidos[nombre].play()
            else:
                self.sonidos[nombre].play(maxtime=duracion)

