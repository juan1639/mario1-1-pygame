import pygame
import os
import configparser


# ====================================================================================
#	settings.py (modulo de configuraciones)
# 
# ------------------------------------------------------------------------------------
class ConfigIni:
    @staticmethod
    def crear_ini_si_no_existe():
        # Ruta del archivo config
        config_file = 'config.ini'

        # Configuración por defecto
        default_config = """
        [general]
        titulo = Primera pantalla Mario Python
        nivel_inicial = 1
        vidas_iniciales = 3
        invulnerable = false

        [video]
        fps = 60
        escala = 3
        tile_x = 16
        tile_y = 16
        filas = 15
        columnas = 16
        escenario_filas = 15
        escenario_columnas = 212
        resolucion_x = 256
        resolucion_y = 240

        [sonido]
        volumen_musica = 0.6
        volumen_efectos = 0.6

        [rutas]
        imagenes = assets/img/
        audio = assets/audio/
        """

        # Si el archivo no existe, crearlo con los valores por defecto
        if not os.path.exists(config_file):
            with open(config_file, 'w') as f:
                f.write(default_config.strip())
            
            print(f"Archivo '{config_file}' creado con configuración predeterminada.")
        else:
            print(f"Archivo '{config_file}' ya existe.")






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
    ConfigIni.crear_ini_si_no_existe()
    
    CONFIG = configparser.ConfigParser()
    CONFIG.read("config.ini")

    ESCALA = int(CONFIG["video"]["escala"])
    TILE_X, TILE_Y = 16 * ESCALA, 16 * ESCALA   # Tamano de los Tiles (x Escala)
    FILAS, COLUMNAS = 15, 24                    # Filas x Columnas (15, 16)
    ESCENARIO_FILAS, ESCENARIO_COLUMNAS = 15, 212 # Total Pantalla (212 ancho x 15 alto)
    MARIO_INI_POS = (COLUMNAS // 2, 12)
    NIVEL_INICIAL = int(CONFIG["general"]["nivel_inicial"])
    VIDAS_INICIALES = int(CONFIG["general"]["vidas_iniciales"])
    RESOLUCION = (TILE_X * COLUMNAS, TILE_Y * FILAS) # Calculo de la pantalla 256x240px(* escala))
    INVULNERABLE = CONFIG.getboolean('general', 'invulnerable')
    RUTA_ASSETS_IMG = CONFIG['rutas']['imagenes']
    RUTA_ASSETS_AUDIO = CONFIG['rutas']['audio']
    FPS = int(CONFIG['video']['fps'])








class Sonidos:
    def __init__(self):
        pygame.mixer.init()

        self.ruta_audio = Constantes.RUTA_ASSETS_AUDIO
        self.sonidos = self.cargar_sonidos()
    


    def cargar_sonidos(self):
        """Cargar todos los sonidos en un diccionario."""

        return {
            "bricks_fall": self.cargar_sonido(f"{self.ruta_audio}bricks-fall.mp3", 0.8),
            "fireworks": self.cargar_sonido(f"{self.ruta_audio}fireworks.mp3", 0.9),
            "gameover": self.cargar_sonido(f"{self.ruta_audio}gameover_mario.mp3", 0.7),
            "salto": self.cargar_sonido(f"{self.ruta_audio}jumpbros.ogg", 0.5),
            "musica-secundaria-tuberias": self.cargar_sonido(f"{self.ruta_audio}mario-tuberias.mp3", 0.7),
            "musica-principal": self.cargar_sonido(f"{self.ruta_audio}musica-mario-bros.mp3", 0.8),
            "oh_no": self.cargar_sonido(f"{self.ruta_audio}oh-no.mp3", 0.8),
            "ough": self.cargar_sonido(f"{self.ruta_audio}ough.mp3", 0.9),
            "moneda": self.cargar_sonido(f"{self.ruta_audio}p-ping.mp3", 0.7),
            "wall": self.cargar_sonido(f"{self.ruta_audio}wall.wav", 0.8)
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

