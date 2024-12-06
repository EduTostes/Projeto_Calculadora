# Importando bilbiotecas Tkinter, para criação de interface
from tkinter import *
import tkinter as tk
from tkinter import ttk
from operacoes import Calculadora

# Cores
co0 = "#ffffff"  # Branco
co1 = "#262624"  # Preto
co2 = "#ff843d"  # Laranja
co3 = "blue"  # Azul
co4 = "#808080"  # cinza

# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.configure(bg=co0)

style = ttk.Style(janela)
style.theme_use('clam')

ttk.Separator(janela, orient="horizontal").grid(row=0, columnspan=1, ipadx=280)

frame_calculo = Frame(janela, width=300, height=56, bg=co1, pady=0, padx=0)
frame_calculo.grid(row=1, column=0, sticky=NW)

frame_b = Frame(janela, width=300, height=340, bg=co0, pady=0, padx=0)
frame_b.grid(row=2, column=0, sticky=NW)

# Variaveis globais
primeiro_numero = None
operador = None
valor_Texto = StringVar()

# Funções
def entrar_valor(numero):
    atual = valor_Texto.get()
    valor_Texto.set(atual + str(numero))

def limpar_Tela():
    global primeiro_numero, operador
    primeiro_numero = None
    operador = None
    valor_Texto.set("")

def definir_operador(op):
    global primeiro_numero, operador
    if valor_Texto.get():
        primeiro_numero = float(valor_Texto.get())
        operador = op
        valor_Texto.set("")

def calcular():
    global primeiro_numero, operador
    try:
        segundo_numero = float(valor_Texto.get())
        resultado = 0

        if operador == "+":
            resultado = Calculadora.add(primeiro_numero, segundo_numero)
        elif operador == "-":
            resultado = Calculadora.sub(primeiro_numero, segundo_numero)
        elif operador == "*":
            resultado = Calculadora.mult(primeiro_numero, segundo_numero)
        elif operador == "/":
            resultado = Calculadora.div(primeiro_numero, segundo_numero)
        elif operador == "√":
            resultado = Calculadora.raiz(primeiro_numero)
            """
            Instruções para utilização de raiz quadrada
            Quando iniciar calculadora, selecionar o número que quer saber a raiz
            em seguida clicar na raiz, e após isso selecionar o número novamente
            e clicar em igual.
            """
            
        
        valor_Texto.set(str(resultado))
        primeiro_numero = None
        operador = None
    except Exception:
        valor_Texto.set("Erro")


# Tela de exibição
app_screen = Label(frame_calculo, width=16, height=2, textvariable=valor_Texto, padx=7,
                   anchor='e', bd=0, justify=RIGHT, font=('ivy 18'), bg=co1, fg=co0)
app_screen.place(x=0, y=0)

# Programando os botões
b_1 = Button(frame_b, text='C', command=lambda:limpar_Tela(), width=11, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_b, text='√', command=lambda:definir_operador("√"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_b, text='/', command=lambda:definir_operador("/"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_b, text='7', command=lambda:entrar_valor("7"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_b, text='8', command=lambda:entrar_valor("8"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_b, command=lambda:entrar_valor("9"), text='9', width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_b, text='4', command=lambda:entrar_valor("4"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=104)
b_8 = Button(frame_b, text='5', command=lambda:entrar_valor("5"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=104)
b_9 = Button(frame_b, text='6', command=lambda:entrar_valor("6"), width=5, height=2, bg=co4, fg=co0,
             font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=104)

b_10 = Button(frame_b, text='1', command=lambda:entrar_valor("1"), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=156)
b_11 = Button(frame_b, text='2', command=lambda:entrar_valor("2"), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=59, y=156)
b_12 = Button(frame_b, text='3', command=lambda:entrar_valor("3"), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=118, y=156)

b_13 = Button(frame_b, text='0', command=lambda:entrar_valor("0"), width=11, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=208)
b_14 = Button(frame_b, text='.', command=lambda:entrar_valor("."), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=208)
b_15 = Button(frame_b, text='X', command=lambda:definir_operador("*"),  width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=52)

b_16 = Button(frame_b, text='-', command=lambda:definir_operador("-"), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=177, y=104)
b_17 = Button(frame_b, text='+', command=lambda:definir_operador("+"), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=177, y=156)
b_18 = Button(frame_b, text='=', command = lambda:calcular(), width=5, height=2, bg=co4, fg=co0,
              font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()
