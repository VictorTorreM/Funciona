import pygame
import random
import math
from pygame import mixer

# inicializar pygame
pygame.init()

# Crear la pantalla 
pantalla = pygame.display.set_mode((800,600))


# Titurlo e icono
pygame.display.set_caption("Nos invaden los chinos")

icono = pygame.image.load("chino.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("fondo.jpg")


#agregar musica 

mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)


# Variables jugador
img_jugador = pygame.image.load("cohete.png")

jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8


for e in range(cantidad_enemigos):
    # Variables enemigo
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)

# Variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.6
bala_visible = False

# Puntuacion

puntuacion = 0
fuente= pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10


# Texto final 

fuente_final = pygame.font.Font("freesansbold.ttf",40)
def texto_final():
    mi_fuente_final= fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))

#funcion mostrar puntuacion

def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntos: {puntuacion}",True,(255,255,255))
    pantalla.blit(texto,(x,y))
# Jugador 


def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# Enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

# Disparar bala

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16 ,y + 10 ))

# Detectar colisiones

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt( math.pow( x_2 - x_1, 2 ) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop jugable
se_ejecuta = True


while se_ejecuta == True:
    
    # Imagen de fondo
    pantalla.blit(fondo,(0,0))
    
    
    # Iterar eventos
    for evento in pygame.event.get():
        
        
        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        #Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
                
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                
                if not bala_visible:
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)
        #Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                
    #Modificar posicion jugador
    jugador_x += jugador_x_cambio
    
    # mantener dentro de pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    
    
    #Modificar posicion ememigo
    
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]= 10000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    
    # mantener enemigo dentro de pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        #colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            sonido_colision= mixer.Sound("golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntuacion += 1
            
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
            
        enemigo(enemigo_x[e],enemigo_y[e],e)
        
    #movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    
    
    
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio
    
    
    
    
    
    
    jugador(jugador_x,jugador_y)
    
    
    
    mostrar_puntaje(texto_x,texto_y)
    
    # actualizar
    pygame.display.update()





