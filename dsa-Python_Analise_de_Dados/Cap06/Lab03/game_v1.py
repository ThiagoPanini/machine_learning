# Game Ping-Pong

from tkinter import *
import random
import time

# Importação de bibliotecas necessárias para composição do game

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))  # Usuário insere o nível desejado
length = 500/level  # Comprimento da barra é proporcional ao nível selecionado


root = Tk()  # Função da biblioteca tkinter
root.title("Ping Pong")  # Título do game (método do objeto root)
root.resizable(0,0)  # Método do objeto root ocm os parâmetros mostrados
root.wm_attributes("-topmost", -1)  # Método do objeto root com os parâmetros mostrados

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)  # Configuração da bola?
canvas.pack()  # Função pack do objeto canvas

root.update()  # Atualiza root (?)

# Variável
count = 0
lost = False  # Perdeu = Falso

class Bola:  # Inicia a classe Bola
    def __init__(self, canvas, Barra, color):  # Chama função __init__ e atribui os respectivos parâmetros
        self.canvas = canvas  # Trabalho com função self
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)  # self (built-in?) método id = cria bola com a função
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]  # Lista com posição inicial da bola
        random.shuffle(starts_x)  # Biblioteca random, mistura

        self.x = starts_x[0]  # Bola inicia na posição inicial de index 0 da lista starts_x (-3)
        self.y = -3  # Coordenada y

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):  # Define OUTRA função dentro da class Bola
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()