# Script de controle Mouse/Teclado
import pyautogui
# Biblioteca Grafica
from tkinter import *
# Biblioteca para Converter RGB em HEX
import webcolors
# Biblioteca para Manipulação de imagem
from PIL import ImageGrab
# Biblioteca de captura de tecla
from keyboard import is_pressed

from tkinter import messagebox

from tkinter import Tk


# Tela inicial
root = Tk()
# Comando para deixar a janela em cima das outras.
root.wm_attributes('-topmost', 'true')
# Comando que retira as bordas da janela
root.overrideredirect(True)
# Variavel para condicionar as teclas para transformar a janela
a = 0



# Função para Sair do Programa
def Exit():
    root.destroy()

# Botão que Sairá do programa
Exit_Button = Button(root, text='Sair', command=Exit)
Exit_Button.place(x=5, y=25, )


# Função utilizada para pegar a posição do mouse
def Position():
    # Captura da Posição
    global a,n,p
    x, y = pyautogui.position()

    Info_Label = Label(root, text="{} | {} ".format(x, y), fg="Red")
    Info_Label.place(x=15, y=0)
# ====================  PIXEL  ======================================
    # Captura da tela
    Pixel = ImageGrab.grab()
    # Captura do pixel, com a interação do mouse
    Pixel = Pixel.getpixel((x,y))
    # Colocando as os valores em cada variavel destinda
    r,g,b = Pixel
    # Conversão para Hexadecimal
    hex = webcolors.rgb_to_hex((r,g,b))
    #Texto do Hexadecimal
    Pixel_Label= Label(root,text="{}".format(hex))
    Pixel_Label.place(x=20,y=20)
    # Lugar de Visualização da Cor
    Pixel_View = Label(root, width=1, height=0, bg="{}".format(hex))
    Pixel_View.place(x=4,y=20)
# ====================  PIXEL  ======================================

# ====================  Mouse  ======================================

    # Condições para Redimencionar a Tela
    if is_pressed('ctrl+c'):
        a = 1
    elif is_pressed('ctrl+x'):
        a = 0

    if a == 1:
        # Mudança de visualização
        if x <= 1200:
            root.geometry("%dx%d+%d+%d" % (80, 50, x + 15, y + 15))
            Exit_Button.place_forget()

        else:
            root.geometry("%dx%d+%d+%d" % (80, 50, x - 185, y + 15))
            Exit_Button.place_forget()
    elif a == 0:
        root.geometry("%dx%d+%d+%d" % (80,75, 600, 400))
        Exit_Button.place(x=25, y=50)
    if is_pressed('n'):

        n = x,y

        root.clipboard_clear()
        root.clipboard_append(n)
        messagebox._show("Real Time", "Cordenadas copiadas")

        print(n)
    if is_pressed('i'):
        i = hex

        root.clipboard_clear()
        root.clipboard_append(i)
        messagebox._show("Real Time", "Cor Copiada")

        print(i)
    if is_pressed('esc'):
        Exit()

    root.after(1, Position)
    # Usado para Fazer o Loop.
    # 1° Tempo, sem usar Float
    # 2° Função ou variavel que vai se repetir
    # Função ou variavel que vai se repetir

root.after(1, Position)

# Saida do loop da tela
root.mainloop()
