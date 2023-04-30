import tkinter as tk
from faker import Faker
import numpy as np
import pandas as pd
import random
from grafo_e_bfs import Grafo
import grafo_e_bfs as gr

usuarios_csv = pd.read_csv("src/usuarios.csv")
usuarios = pd.DataFrame(usuarios_csv)
grafo = Grafo(usuarios, direcionado=False)

for i in usuarios["estilo"]:
    grafo.adiciona_estilos([('Estilos', str(i))])

def pesquisa(usuarios, artista):
    df = usuarios.query(f'artista favorito == {artista}')
    tamanho = df.size
    return df, tamanho

class TelaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tela principal")

        self.label_artista_favorito = tk.Label(
            self.master, text="Artista favorito:")
        self.label_artista_favorito.grid(row=0, column=0, padx=5, pady=5)
        self.entry_artista_favorito = tk.Entry(self.master)
        self.entry_artista_favorito.grid(row=0, column=1, padx=5, pady=5)

        self.label_tamanho_lista = tk.Label(
            self.master, text="Tamanho da lista:")
        self.label_tamanho_lista.grid(row=1, column=0, padx=5, pady=5)
        self.entry_tamanho_lista = tk.Entry(self.master)
        self.entry_tamanho_lista.grid(row=1, column=1, padx=5, pady=5)

        self.button_tela_cadastro = tk.Button(
            self.master, text="Cadastrar", command=self.abrir_tela_cadastro)
        self.button_tela_cadastro.grid(row=3, column=0, padx=5, pady=5)

        self.button_tela_pesquisar = tk.Button(
            self.master, text="Pesquisar", command=self.abrir_tela_pesquisa)
        self.button_tela_pesquisar.grid(row=3, column=1, padx=5, pady=5)

    def abrir_tela_pesquisa(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPesquisa(nova_tela)

    def abrir_tela_cadastro(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaCadastro(nova_tela)


class TelaCadastro(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Cadastro de Usuário")

        self.label_nome = tk.Label(self.master, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_genero_musical = tk.Label(
            self.master, text="Gênero Musical:")
        self.label_genero_musical.grid(row=1, column=0, padx=5, pady=5)
        self.entry_genero_musical = tk.Entry(self.master)
        self.entry_genero_musical.grid(row=1, column=1, padx=5, pady=5)

        self.label_artista_favorito = tk.Label(
            self.master, text="Artista Favorito:")
        self.label_artista_favorito.grid(row=2, column=0, padx=5, pady=5)
        self.entry_artista_favorito = tk.Entry(self.master)
        self.entry_artista_favorito.grid(row=2, column=1, padx=5, pady=5)

        self.button_cadastrar = tk.Button(
            self.master, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.grid(row=3, column=0, padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=3, column=1, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)

    def cadastrar(self):
        nome = self.entry_nome.get()
        genero_musical = self.entry_genero_musical.get()
        artista_favorito = self.entry_artista_favorito.get()

        nova_linha = {'nome': nome, 'estilo': genero_musical,
                      'artista favorito': artista_favorito}
        usuarios.loc[len(usuarios)] = nova_linha

        print(usuarios)

        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


class TelaPesquisa(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pessoas Sugeridas")

        # criando a Listbox
        self.listbox_pessoas = tk.Listbox(self.master)
        self.listbox_pessoas.pack(padx=5, pady=5)

        # Fazer a busca no grafo das pessoas que escutam aquele mesmo artista ou artistas o mais parecido possivel e retornar em um for dando insert
        # Adicionar itens à Listbox (apenas como exemplo)
        self.listbox_pessoas.insert(tk.END, "Pessoa 1")
        self.listbox_pessoas.insert(tk.END, "Pessoa 2")
        self.listbox_pessoas.insert(tk.END, "Pessoa 3")

        # botao conectar
        self.button_conectar = tk.Button(
            self.master, text="Conectar", command=self.conectar)
        self.button_conectar.pack(padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="Voltar", command=self.voltar)
        self.button_voltar.pack(padx=5, pady=5)

    def conectar(self):
        # Função a ser executada ao clicar no botão "Conectar"
        selected_index = self.listbox_pessoas.curselection()
        if selected_index:
            selected_person = self.listbox_pessoas.get(selected_index)
            print(f"Conectando com: {selected_person}")
        else:
            print("Nenhuma pessoa selecionada!")

    # funcao de voltar
    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


root = tk.Tk()
TelaPrincipal(root)
root.mainloop()
