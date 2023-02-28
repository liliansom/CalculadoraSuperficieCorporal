# Calculadora de superfície corporal (Fórmula de Mosteller)
from math import sqrt
import tkinter as tk

def mosteller():
    entry3.delete(0, 4)
    peso = float(entry1.get())
    altura = float(entry2.get())
    mosteller = float(altura*peso/3600)
    sc = sqrt(mosteller)
    entry3.insert(0, '{:.2f}'.format(sc))

#INTERFACE
janela = tk.Tk()
janela.title('Calculadora Mosteller')
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

# TÍTULO
mensagem = tk.Label(text='Superfície Corporal',
                   fg='black',
                   width=40,
                   height=5)
mensagem.pack()

# PESO
mensagem1 = tk.Label(text='Peso em Kilos\n EX: 68.9',
                   fg='black')
mensagem1.pack()
entry1 = tk.Entry()
entry1.pack()

# ALTURA
mensagem2 = tk.Label(text='Altura em Centímetros\n EX: 169',
                   fg='black')
mensagem2.pack()

entry2 = tk.Entry()
entry2.pack()

# BOTÃO CALCULAR
botao = tk.Button(text='CALCULAR',
                   bg='grey', command=mosteller)
botao.pack()


# SUPERFÍCIE CORPORAL
superficie = tk.Label(text='A Superfície Corporal (em M²)\n corresponde a:',
                   fg='black')

superficie.pack()

entry3 = tk.Entry()
entry3.pack()

# CRÉDITOS
mensagem4 = tk.Label(text='',
                   fg='black')
mensagem4.pack()

mensagem5 = tk.Label(text='Desenvolvido por @liliansom (Github)',
                   fg='black')
mensagem5.pack()

janela.mainloop()

