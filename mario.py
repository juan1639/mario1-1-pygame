import pygame


class Mario(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()

        self.game = game
        
        self.TX = self.game.CO.TILE_X
        self.TY = self.game.CO.TILE_Y

        # Sprite-sheet mario (pequeño):
        self.spritesheet_img_rect = self.game.obtener_grafico("mario-ss1.png")

        self.image = self.spritesheet_img_rect[0]
        self.rect = self.spritesheet_img_rect[1]

        self.ancho_ssheet = self.image.get_width()
        self.alto_ssheet = self.image.get_height()
        self.numero_sprites_ssheet = self.ancho_ssheet // self.TX
        self.rango_animacion = (1, 4)
        print(self.numero_sprites_ssheet)

        # Creamos una lista de imagenes (recortando el sprite_sheet):
        self.anim_index = 0
        self.lista_imagenes = []

        for i in range(self.numero_sprites_ssheet):
            img = pygame.Surface((self.TX, self.TY))
            img.blit(self.image, (0, 0), (i * self.TX, 0, self.TX, self.TY))
            img.set_colorkey((255, 255, 255))
            self.lista_imagenes.append(img)
        
        self.image = self.lista_imagenes[self.anim_index]


        # Rectángulo y posición
        self.rect = self.image.get_rect()
        self.rect.x = x * self.TX
        self.rect.y = y * self.TY

        # Radius (reducir el radio, para hacer mas permisiva la colision)...
        # self.radius = 20

        # Configuración adicional
        self.direccion_actual = 0
        self.velocidad = 2
        self.ultimo_update = pygame.time.get_ticks()
        self.VEL_FRAMES_ANIMA = 90 # Velocidad de la animación
        self.ultimo_sonido = pygame.time.get_ticks()
    






    def update(self):
        if not self.game.estado_juego["en_juego"]:
            return

        self.leer_teclado()
        self.actualizar_animacion()
        self.manejar_colisiones()
    


    



    def leer_teclado(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.direccion_actual = -1
        elif teclas[pygame.K_RIGHT]:
            self.direccion_actual = 1
        else:
            self.direccion_actual = 0
            self.anim_index = 0
        

        if teclas[pygame.K_SPACE]:
            print("gestionar salto")
    

    
    


    def manejar_colisiones(self):
        pass





    def colision_laberinto(self, direccion, x, y):
        pass





    
    def es_teletransporte(self, x, y, vel_x):
        """ if y == 11:  # Línea especial para teletransporte
            if x + vel_x > self.game.CO.COLUMNAS:
                self.rect.x = -self.TX
                return True
            elif x + vel_x < -1:
                self.rect.x = self.game.CO.COLUMNAS * self.TX
                return True
        return False """
    






    def actualizar_animacion(self):
        if pygame.time.get_ticks() - self.ultimo_update > self.VEL_FRAMES_ANIMA:
            self.ultimo_update = pygame.time.get_ticks()
            self.anim_index += 1

            if self.anim_index >= self.rango_animacion[1]:
                self.anim_index = self.rango_animacion[0]
            
            x = self.rect.x
            y = self.rect.y
            self.image = self.lista_imagenes[self.anim_index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

