from tkinter import *
import math

root = Tk()
#tamanho da janela.
root.geometry('1200x500')
#se consegue alterar o tamnanho na direção x e y.
#root.resizable(False, False)
root.title("Ficha D&D")

seu_nome = Entry(root, width=30, borderwidth=5, bg="blue", fg="white")
seu_nome.grid(row=0, column=0, padx=5,pady=5)
seu_nome.insert(0, "Seu nome")
pers_nome= Entry(root, width=30, borderwidth=5, bg="blue", fg="white")
pers_nome.grid(row=1, column=0,padx=5,pady=5)
pers_nome.insert(0, "Nome do seu personagem")

lista_tudo = ['racas', 'classes','antec']

racas = ['Anão','Draconato','Elfo','Humano','Meio-elfo','Meio-orc','Tiferino']
classes = ['Bárbaro','Bruxo','Clérigo','Druida','Feiticeiro','Mago','Monge','Paladino','Patrulheiro']
antec = ['Acólito', 'Artesão de Guilda', 'Artista', 'Charlatão', 'Criança de Rua', 'Criminoso', 'Eremita',
 'Forasteiro', 'Herói do Povo','Marinheiro', 'Nobre', 'Sábio', 'Soldado', 'Customizado']

lista_txt_tudo = ['sua raça','sua classe','seu antecendente']

for i in range(len(lista_tudo)):
	txt = Label (root, text="Escolha "+lista_txt_tudo[i]+": ")
	txt.grid(row=2+2*i, column=0)
	# exec consegue substituir uma string para fazer um mesmo comando varias vezes para varias listas
	exec ('var_%s = StringVar(root, %s[0])' %(lista_tudo[i], lista_tudo[i]))
	exec ('sel_%s = OptionMenu(root, var_%s, *%s)' %(lista_tudo[i], lista_tudo[i], lista_tudo[i]))
	exec ('sel_%s.config(width=10, font=("Helvetica",12))' %(lista_tudo[i]))
	exec ('sel_%s.grid(row=3+2*i, column=0)' %(lista_tudo[i]))

txt_atr = Label (root, text="Informe o valor de seus atributos:")
atributos = [
	('Força',0),
	('Destreza',0),
	('Constituição',0),
	('Inteligência',0),
	('Sabedoria',0),
	('Carisma',0)
]
# i é o contador e idx é o valor
for cont, i in enumerate(atributos):
	txt_atr_i = Label (root, text=i[0]+": ")
	txt_atr_i.grid (row=8+cont, column=0, padx=5, pady=5)
	atr = Entry(root, width=30, borderwidth=5, bg="blue", fg="white")
	atr.grid(row=8+cont, column=1, padx=5,pady=5)
	atr.insert(0, i[1])
pers_nome= Entry(root, width=30, borderwidth=5, bg="blue", fg="white")
pers_nome.grid(row=1, column=0,padx=5,pady=5)
pers_nome.insert(0, "Nome do seu personagem")

def mod(valor):
	return math.floor((valor-10)/2)
blabla = Label (root, text=mod(8))
blabla.grid(row=0,column=4)
resumo = LabelFrame(root, text="Sua Ficha", padx=10, pady=10)

def botao_click():
	
	global resumo
	resumo.destroy()
	resumo = LabelFrame(root, text="Sua Ficha", padx=10, pady=10)
	resumo.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

	txt_seu_nome = Label(resumo, text=str(seu_nome.get()),font=('Helvetica', 12),fg='red')
	txt_seu_nome.grid(row=0, column=0)
	txt_pers_nome = Label(resumo, text=str(pers_nome.get()),font=('Helvetica', 12),fg='red')
	txt_pers_nome.grid(row=0, column=1)
	txt_raca = Label(resumo, text=str(var_r.get()),font=('Helvetica', 12),fg='red')
	txt_raca.grid(row=1, column=0)
	txt_classe = Label(resumo, text=str(var_c.get()),font=('Helvetica', 12),fg='red')
	txt_classe.grid(row=1, column=1)


botao_resumo = Button(root, text="Resumo", padx=20, pady=10, command=botao_click)
botao_resumo.grid(row=1, column=2)





root.mainloop()