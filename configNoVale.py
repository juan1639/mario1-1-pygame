import configparser

config = configparser.ConfigParser()
config.read("config.ini")

# Ejemplos de acceso:
nivel = int(config["general"]["nivel_inicial"])
res_x = int(config["video"]["resolucion_x"])
ruta_img = config["rutas"]["imagenes"]
volumen_fx = float(config["sonido"]["volumen_efectos"])
