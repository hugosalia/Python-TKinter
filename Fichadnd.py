# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import math

root = Tk()
#tamanho da janela.
root.geometry('320x415')
#se consegue alterar o tamnanho na direção x e y.
#root.resizable(False, False)
root.title("Ficha D&D")

seu_nome = Entry(root, width = 33, borderwidth=5, font=('Helvetica',12))
seu_nome.grid(row=0, column=0, columnspan= 2, padx=5, pady=5, sticky=W)
seu_nome.insert(0, "Seu nome")
pers_nome= Entry(root, width=33, borderwidth=5, font=('Helvetica',12))
pers_nome.grid(row=1, column=0,  columnspan= 2, padx=5, pady=5, sticky=W)
pers_nome.insert(0, "Nome do seu personagem")

racas = ['Anão','Draconato','Elfo','Humano','Meio-elfo','Meio-orc','Tiferino']
classes = ['Bárbaro','Bruxo','Clérigo','Druida','Feiticeiro','Mago','Monge','Paladino','Patrulheiro']
antec = ['Acólito', 'Artesão de Guilda', 'Artista', 'Charlatão', 'Criança de Rua', 'Criminoso', 'Eremita',
 'Forasteiro', 'Herói do Povo','Marinheiro', 'Nobre', 'Sábio', 'Soldado', 'Customizado']
alinha = ['Ordeiro Bom', 'Ordeiro Neutro', 'Ordeiro Mau', 'Neutro Bom', 'Neutro', 'Neutro Mau',
 'Caótico Bom', 'Caótico Neutro', 'Caótico Mau']

lista_tudo = [racas, classes, antec, alinha]

lista_txt_tudo = ['sua raça','sua classe','seu antecendente', 'seu alinhamento']

var=['Anão','Bárbaro','Acólito','Ordeiro Bom']

matriz = [(0,0), (0,1), (1,0), (1,1)]
for i in range(len(lista_tudo)):
	txt = Label (root, text="Escolha "+lista_txt_tudo[i]+": ")
	txt.grid(row=2+2*matriz[i][0], column=matriz[i][1], padx=5, sticky=W)
	#var[i] = StringVar(root, lista_tudo[i][0])
	#sel = OptionMenu(root, var[i], *lista_tudo[i])
	var[i] = ttk.Combobox(root, values = lista_tudo[i])
	var[i].config(width=15, font=('Helvetica',10))
	var[i].grid(row=3+2*matriz[i][0], column=matriz[i][1], padx=5, sticky=W)


txt_atr = Label (root, text="Informe o valor de seus atributos:")

atributos = [
	['Força',0],
	['Destreza',0],
	['Constituição',0],
	['Inteligência',0],
	['Sabedoria',0],
	['Carisma',0]
]


#lista de widgets
atr=[]
# cont é o contador e i é o valor
for cont, i in enumerate(atributos):
	atr.append(Entry(root, width=5, borderwidth=5))
	txt_atr_i = Label (root, text=i[0]+": ",  font=('Helvetica',12))
	txt_atr_i.grid (row=8+cont, column=0, padx=5, pady=5)
	atr[cont].grid(row=8+cont, column=1, padx=5,pady=5, sticky=W)
	atr[cont].insert(0, i[1])


def botao_ir_click():
	global seu_nome
	seu_nome = seu_nome.get()
	global pers_nome
	pers_nome = pers_nome.get()
	global pers_raca
	pers_raca = var[0].get()
	global pers_classe
	pers_classe = var[1].get()
	global pers_antec
	pers_antec = var[2].get()
	global pers_alinha
	pers_alinha = var[3].get()
	global atributos
	for i in range(len(atributos)):
		atributos[i][1] = int(atr[i].get())
	for widget in root.winfo_children():
		widget.destroy()

	root.geometry('600x600')

	def modif(valor):
		return math.floor((valor-10)/2)

	for i in atributos:
		txt_modif = Label (root, text=modif(i[1]))

	global modificadores
	modificadores = [
		modif(atributos[0][1]),
		modif(atributos[1][1]),
		modif(atributos[2][1]),
		modif(atributos[3][1]),
		modif(atributos[4][1]),
		modif(atributos[5][1])
	]
	global pericias
	pericias = [
		['Acrobacia (Des)', modificadores[1]],
		['Arcanismo (Int)', modificadores[3]],
		['Atletismo (For)', modificadores[0]],
		['Atuação (Car)', modificadores[5]],
		['Enganação (Car)', modificadores[5]],
		['Furtividade (Des)', modificadores[1]],
		['História (Int)', modificadores[3]],
		['Intimidação (Car)', modificadores[5]],
		['Intuição (Sab)', modificadores[4]],
		['Lidar com Animais (Sab)', modificadores[4]],
		['Medicina (Sab)', modificadores[4]],
		['Natureza (Int)', modificadores[3]],
		['Percepção (Sab)', modificadores[4]],
		['Persuasão (Car)', modificadores[5]],
		['Prestidigitação (Des)', modificadores[1]],
		['Religião (Int)', modificadores[3]],
		['Sobrevivência (Sab)', modificadores[4]],
	]
	global level
	level = 1;
	global bonus_profic
	bonus_profic = math.floor(0.25*level+1.75)
	plot_level = Label(root, text="Level 1", padx=5)
	plot_level.grid(row=0, column=0, sticky=W)
	plot_bonus_profic = Label(root, text="Bônus de Proficiência = +2", padx=5)
	plot_bonus_profic.grid(row=1, column=0, sticky=W)

	frame_per = LabelFrame(root, text="Perícias", padx=10, pady=10)
	frame_per.grid(row=2, column=0, padx=10,pady=10)

	frame_salvag = LabelFrame(root, text="Salvaguardas", padx=10, pady=10)
	frame_salvag.grid(row=2, column=1, padx=10,pady=10, sticky=W+N)


	def ver_sinal (value):
		if value >= 0:
			return "+"+str(value)
		else:
			return str(value)

	global plot_mod_p
	global plot_mod_s
	plot_salvag =[]
	plot_per=[]
	plot_mod_p=[]
	plot_mod_s=[]
	var_s=[]
	var_p=[]

	def click_salvag(value):
		global modificadores
		global plot_mod_s
		if var_s[value].get() == 1:
			plot_mod_s[value]= Label(frame_salvag, text=ver_sinal(modificadores[value]+bonus_profic), padx=5, fg='red')
		else:
			plot_mod_s[value]= Label(frame_salvag, text=ver_sinal(modificadores[value]-bonus_profic), padx=5)
		plot_mod_s[value].grid(row=value, column=2, sticky=W)

	def click_profic(value):
		global pericias
		global plot_mod_p
		if var_p[value].get() == 1:
			pericias[value][1] = pericias[value][1]+bonus_profic
			plot_mod_p[value]= Label(frame_per, text=ver_sinal(pericias[value][1]), padx=5, fg='red')
		else:
			pericias[value][1] = pericias[value][1]-bonus_profic
			plot_mod_p[value]= Label(frame_per, text=ver_sinal(pericias[value][1]), padx=5)
		plot_mod_p[value].grid(row=value, column=2, sticky=W)

	for i in range(len(atributos)):
		var_s.append(IntVar())
		#Precisa colocar c=i pra ele pegar o valor correto na função. Se não ele pega o útlimo i apenas.
		plot_salvag.append(Checkbutton(frame_salvag, text=atributos[i][0],padx=5,variable=var_s[i], onvalue=1 , offvalue=0, command=lambda c=i: click_salvag(c)))
		plot_mod_s.append(Label(frame_salvag, text=ver_sinal(modificadores[i]), padx=5))
		plot_igual = Label(frame_salvag, text='=')
		plot_salvag[i].grid(row=i, column=0,sticky=W)
		plot_igual.grid(row=i, column=1)
		plot_mod_s[i].grid(row=i, column=2, sticky=W)

	for i in range(len(pericias)):
		var_p.append(IntVar())
		plot_per.append(Checkbutton(frame_per, text=pericias[i][0],padx=5,variable=var_p[i], onvalue=1 , offvalue=0, command=lambda c=i: click_profic(c)))
		plot_mod_p.append(Label(frame_per, text=ver_sinal(pericias[i][1]), padx=5))
		plot_igual = Label(frame_per, text='=')
		plot_per[i].grid(row=i, column=0,sticky=W)
		plot_igual.grid(row=i, column=1)
		plot_mod_p[i].grid(row=i, column=2, sticky=W)





	#label1 = Label (root, text=seu_nome).pack()
	#label2 = Label (root, text=pers_nome).pack()
	#label3 = Label (root, text=pers_raca).pack()
	#label4 = Label (root, text=pers_classe).pack()
	#label5 = Label (root, text=pers_antec).pack()
	#label6 = Label (root, text=pers_alinha).pack()
	#for i in range(5):
	#	labelresto=Label (root, text=atributos[i][1]).pack()


botao_ir = Button(root, text=">>", padx=10, pady=0.1, command=botao_ir_click)
botao_ir.grid(row=15, column=0, columnspan=2, sticky=E)

def botao_voltar_click():
	for widget in root.winfo_children():
		widget.destroy()

botao_ir = Button(root, text="<<", padx=10, pady=0.1, command= botao_ir_click, state=DISABLED)
botao_ir.grid(row=15, column=0, columnspan=2, sticky=W)

#resumo = LabelFrame(root, text="Sua Ficha", padx=10, pady=10)
#def botao_click():

#	global resumo
#	resumo.destroy()
#	resumo = LabelFrame(root, text="Sua Ficha", padx=10, pady=10)
#	resumo.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

#	txt_seu_nome = Label(resumo, text=str(seu_nome.get()),font=('Helvetica', 12),fg='red')
#	txt_seu_nome.grid(row=0, column=0)
#	txt_pers_nome = Label(resumo, text=str(pers_nome.get()),font=('Helvetica', 12),fg='red')
#	txt_pers_nome.grid(row=0, column=1)
#	txt_raca = Label(resumo, text=str(var_r.get()),font=('Helvetica', 12),fg='red')
#	txt_raca.grid(row=1, column=0)
#	txt_classe = Label(resumo, text=str(var_c.get()),font=('Helvetica', 12),fg='red')
#	txt_classe.grid(row=1, column=1)

#botao_resumo = Button(root, text="Resumo", padx=20, pady=10, command=botao_click)
#botao_resumo.grid(row=1, column=2)

root.mainloop()
