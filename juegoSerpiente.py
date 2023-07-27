import turtle
import time
import random

posponer = 0.1

# marcador

score = 0
highScore = 0

wn = turtle.Screen()
wn.title("Juego de la serpiente DGG")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# comida

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# cuerpo de la serpiente

segmentos = []

# texto 

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))


# funciones para mover la serpiente 

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# teclado 
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Bucle principal del juego

while True:
    wn.update()

    # coliciones bordes 

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)  
        cabeza.direction = "stop"

        # esconder los segmentos 
        for segmento in segmentos:
            segmento.goto(1000,1000)

        # limpiar lista de segmentos 

        segmentos.clear()

        # resetear marcador

        score = 0
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score, highScore),
                     align="center", font=("Courier", 24, "normal"))

    # coliciones comida 

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.color("gray")
        nuevoSegmento.penup()
        segmentos.append(nuevoSegmento)

        # aumentar marcador 
        score += 10
        if score > highScore:
            highScore = score

        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score, highScore),
                     align="center", font=("Courier", 24, "normal"))

    # mover el cuerpo de la serpiente 
    tatalSeg = len(segmentos)
    for index in range(tatalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if tatalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    # colicion cuerpo

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)
                segmento.clear()
            segmentos.clear()

            # resetear marcador

            score = 0
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(score, highScore),
                       align="center", font=("Courier", 24, "normal"))

    time.sleep(posponer)




