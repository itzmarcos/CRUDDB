from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser

from view import *

co8 = "#038cfc"
co9 = "#e9edf5"
co1 = "#feffff"
co3 = "#38576b"
co7 = "#3fbfb9"

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

frameCima = Frame(janela, width=1043, height=50, bg=co8, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co3, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#funçoes
global tree

def inserir():
    nome = e_nome.get()
    valor = e_valor.get()

    lista_inserir = [nome, valor]
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inserir_from(lista_inserir)

    messagebox.showerror('Sucesso','Os dados foram inserido com sucesso')

    e_nome.delete(0,'end')
    e_valor.delete(0,'end')

    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0,'end')
        e_valor.delete(0,'end')

        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_valor.insert(0,treev_lista[2])

        def update():

            nome = e_nome.get()
            valor = e_valor.get()

            lista_atualizar = [nome, valor]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            att_(lista_atualizar)
            messagebox.showerror('Sucesso','Os dados foram atualizado com sucesso')

            e_nome.delete(0,'end')
            e_valor.delete(0,'end')

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados')


def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_from([valor])
        messagebox.showinfo('Sucesso','Os dados foram deletado com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na tabela')



    mostrar()
     


#entradas
l_nome = Label(frameMeio, text='   Nome   ', height=1, anchor=NW, font=('Ivy 12 bold'), bg=co1, fg=co7)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_valor = Label(frameMeio, text='   Valor    ', height=1, anchor=NW, font=('Ivy 12 bold'), bg=co1, fg=co7)
l_valor.place(x=10, y=40)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=41)



b_inserir = Button(frameMeio,command=inserir, text='Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE)
b_inserir.place(x=330, y=10)

b_atulizar = Button(frameMeio, command=atualizar, text='Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE)
b_atulizar.place(x=330, y=50)

b_delete = Button(frameMeio,command=deletar, text='Delete'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE)
b_delete.place(x=330, y=90)


l_total = Label(frameMeio, text='', width=15, height=3, anchor=CENTER,font=('Ivy 17 bold'), bg=co8 ,fg=co1)
l_total.place(x=450, y=17)

l_total_ = Label(frameMeio, text=' Valor total               ', height=1, anchor=NW,font=('Ivy 17 bold'), bg=co8 ,fg=co1)
l_total_.place(x=450, y=12)

l_qtd = Label(frameMeio, text='', width=15, height=3,anchor=CENTER,font=('Ivy 17 bold'), bg=co8 ,fg=co1)
l_qtd.place(x=450, y=90)

l_qtd_ = Label(frameMeio, text='Quantidade Total',height=1, anchor=NW, font=('Ivy 17 bold'), bg=co8, fg=co1)
l_qtd_.place(x=450, y=92)





def mostrar():
        
    global tree

    tabela_head = ['#Item','Nome', 'Valor']
    lista_itens = ver_from()



    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")


    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center"]
    h=[294,294,294]
    n=0

    for col in tabela_head:

        tree.heading(col, text=col.title(), anchor=CENTER)
                    
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

# inserindo itens
    for item in lista_itens:
        tree.insert('', 'end', values=item)

        quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[0])

    Total_valor=sum(quantidade)
    Total_itens=len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

    

mostrar()



janela.mainloop()