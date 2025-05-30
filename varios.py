import pygame

# ====================================================================================
#   varios.py (modulo de varias clases pequeñas que requieren poca logica)
#   class --> Textos
#
# ------------------------------------------------------------------------------------
class Textos(pygame.sprite.Sprite):
    def __init__(self, game, texto, size, x, y, color, fondo=None, negrita=False, centrado=True, tipo=None):
        super().__init__()
        self.game = game
        self.texto = texto
        self.size = size
        self.color = color
        self.fondo = fondo
        self.centrado = centrado
        self.tipo = tipo
        self.font = pygame.font.SysFont('verdana', self.size)
        self.font.set_bold(negrita)
        self.image = self.font.render(self.texto, True, self.color, self.fondo)

        if self.centrado:
            self.rect = self.image.get_rect(center=(x, y))
        else:
            self.rect = self.image.get_rect(topleft=(x, y))
        
        # Identificar si se trata de un texto dinámico (puntos o nivel)
        #self.render_nivel = self.texto = str(self.game.nivel)
    

    
    def update(self):
        if self.tipo == "dinamico-puntos":
            self.image = self.font.render(f'{self.game.puntos}', True, self.color, self.fondo)
        if self.tipo == "dinamico-nivel":
            self.image = self.font.render(f'{self.game.nivel}', True, self.color, self.fondo)

        if self.tipo != None:
            if self.tipo.startswith("show-bonus"):
                self.rect.y -= 1

