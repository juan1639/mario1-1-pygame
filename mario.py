import pygame

class Mario(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game

        self.TX = self.game.CO.TILE_X
        self.TY = self.game.CO.TILE_Y

        # Sprite sheet
        self.spritesheet_img_rect = self.game.obtener_grafico("mario-ss1.png")
        self.image = self.spritesheet_img_rect[0]
        self.rect = self.spritesheet_img_rect[1]

        self.ancho_ssheet = self.image.get_width()
        self.alto_ssheet = self.image.get_height()
        self.numero_sprites_ssheet = self.ancho_ssheet // self.TX
        self.rango_animacion = (1, 4)

        # Recorte de sprites
        self.anim_index = 0
        self.lista_imagenes = []

        for i in range(self.numero_sprites_ssheet):
            img = pygame.Surface((self.TX, self.TY), pygame.SRCALPHA)
            img.blit(self.image, (0, 0), (i * self.TX, 0, self.TX, self.TY))
            # img.set_colorkey((255, 255, 255))
            self.lista_imagenes.append(img)
        
        self.image = self.lista_imagenes[self.anim_index]

        # Posición y velocidad
        self.rect = self.image.get_rect()
        self.rect.x = x * self.TX
        self.rect.y = y * self.TY

        # Dirección, aceleracion, limites y físicas:
        self.acc = 0    # Aceleracion (vel) del personaje
        self.flip = False
        self.VEL_MAX = 7.5
        self.ACELERACION = 0.1
        self.DECELERACION = 0.04

        # Velocidad de las animaciones:
        self.ultimo_update = pygame.time.get_ticks()
        self.VEL_FRAMES_ANIMA = 90
    
    
    
    
    
    
    
    def update(self):
        if not self.game.estado_juego["en_juego"]:
            return

        self.mover()
        self.actualizar_animacion()
        self.manejar_colisiones()
    
    

    
    
    
    
    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.gestionar_aceleracion(self.flip)
            self.flip = True
        
        elif teclas[pygame.K_RIGHT]:
            self.gestionar_aceleracion(self.flip)
            self.flip = False
        
        else:
            if self.acc > 0:
                self.acc -= self.DECELERACION
                self.acc = 0 if self.acc < 0 else self.acc
            else:
                self.acc += self.DECELERACION
                self.acc = 0 if self.acc > 0 else self.acc
        
        # Mover scroll (mario no se mueve realmente):
        self.game.scroll_x += self.acc
    







    def gestionar_aceleracion(self, flip):
        if flip:
            self.acc -= self.ACELERACION
            self.acc = -self.VEL_MAX if self.acc < -self.VEL_MAX else self.acc
        else:
            self.acc += self.ACELERACION
            self.acc = self.VEL_MAX if self.acc > self.VEL_MAX else self.acc
    

    
    





    def actualizar_animacion(self):
        ahora = pygame.time.get_ticks()

        if ahora - self.ultimo_update > self.VEL_FRAMES_ANIMA:
            self.ultimo_update = ahora
            self.anim_index += 1

            if self.anim_index >= self.rango_animacion[1]:
                self.anim_index = self.rango_animacion[0]
            
            # Si va muy lento (cerca de 0), entonces 'animacion parado'[0]:
            if -0.01 <= self.acc <= 0.01:
                self.image = self.lista_imagenes[0]
                self.image = pygame.transform.flip(self.image, self.flip, False)
            else:
                # Si no, cambia la secuencia de animacion de forma normal:
                self.image = self.lista_imagenes[self.anim_index]
                self.image = pygame.transform.flip(self.image, self.flip, False)
    

    


    
    
    
    
    def manejar_colisiones(self):
        # Placeholder para futuras colisiones con el entorno
        pass

