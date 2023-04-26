import tkinter as tk
from faker import Faker
import numpy as np
import pandas as pd
import random

faker = Faker()
# Gera 50 nomes sem repeticao usando o faker
nomes = np.array([])
while len(nomes) < 50:
    nome = faker.name()
    if nome not in nomes:
        nomes = np.append(nomes, nome)

# Array com estilos de musica

estilos_musica = ["Rock", "Pop", "Hip Hop", "Sertanejo", "Eletrônica", ]

# Array com artistas/bandas de rock

artistas_rock = [
    "Led Zeppelin", "The Rolling Stones", "Queen", "AC/DC", "Pink Floyd",
    "Guns N' Roses", "Nirvana", "The Who", "Black Sabbath", "Metallica",
    "Deep Purple", "Foo Fighters", "Red Hot Chili Peppers", "Linkin Park",
    "Pearl Jam", "U2", "Bon Jovi", "The Beatles", "Green Day", "The Doors",
    "Oasis", "Radiohead", "R.E.M.", "Foo Fighters", "System of a Down",
    "Arctic Monkeys", "Coldplay", "Muse", "The Strokes", "Iron Maiden"
]

# Array com artistas/bandas de pop

artistas_pop = [
    'Taylor Swift', 'Ariana Grande', 'Ed Sheeran', 'Dua Lipa', 'Justin Bieber',
    'Billie Eilish', 'Shawn Mendes', 'Camila Cabello', 'The Weeknd', 'Katy Perry',
    'Maroon 5', 'Bruno Mars', 'Rihanna', 'Selena Gomez', 'Charlie Puth', 'Lady Gaga', 'Post Malone',
    'Zara Larsson', 'Harry Styles', 'Sia', 'Miley Cyrus', 'Justin Timberlake', 'Lizzo', 'Jason Derulo',
    'Halsey', 'Sam Smith', 'Jonas Brothers', 'Jessie J', 'Niall Horan', 'Lauv'
]

# Array com artistas/bandas de hip hop

artistas_hip_hop = [
    "Eminem", "Jay-Z", "Kanye West", "Drake", "Kendrick Lamar",
    "Nas", "Notorious B.I.G.", "Tupac Shakur", "Snoop Dogg", "Lil Wayne",
    "J. Cole", "Outkast", "Lauryn Hill", "Wu-Tang Clan", "A Tribe Called Quest",
    "Ice Cube", "MF DOOM", "Run-D.M.C.", "Public Enemy", "KRS-One",
    "Big Daddy Kane", "Lil Kim", "Gang Starr", "Mos Def", "Common", "Rakim",
    "Big L", "A$AP Rocky", "Tyler, The Creator", "Chance the Rapper", "Logic"
]

# Array com artistas de sertanejo

artistas_sertanejo = [
    "Chitãozinho & Xororó", "Maiara & Maraisa", "Jorge & Mateus", "Gusttavo Lima", "Marília Mendonça",
    "Zé Neto & Cristiano", "Henrique & Juliano", "Michel Teló", "César Menotti & Fabiano", "Fernando & Sorocaba",
    "Gino & Geno", "Luan Santana", "Paula Fernandes", "Cristiano Araújo", "Zezé Di Camargo & Luciano", "Daniel",
    "Munhoz & Mariano", "Jads & Jadson", "Matheus & Kauan", "Guilherme & Santiago", "João Neto & Frederico",
    "Gian & Giovani", "Gustavo Mioto", "Bruno & Marrone", "Rick & Renner", "Eduardo Costa",
    "Marcos & Belutti", "Léo Magalhães", "Zezé di Camargo", "Loubet"
]

# Array com artistas de eletronica

artistas_eletronica = [
    "Daft Punk", "Avicii", "Calvin Harris", "David Guetta", "Martin Garrix",
    "The Chainsmokers", "Zedd", "Marshmello", "Skrillex", "Tiesto", "Deadmau5",
    "Disclosure", "Kygo", "Flume", "Major Lazer", "Kaskade", "Steve Aoki",
    "Armin van Buuren", "Alesso", "Axwell", "Above & Beyond", "Hardwell", "R3hab", "Nicky Romero",
    "Diplo", "Porter Robinson", "Eric Prydz", "Nervo", "Alan Walker", "Galantis"
]

# cria a tabela vazia
tabela = []

for i in range(50):
    nome = nomes[i]
    estilo = random.choice(estilos_musica)
    artista = ""
    if estilo == 'Rock':
        artista = random.choice(artistas_rock)
    if estilo == 'Pop':
        artista = random.choice(artistas_pop)
    if estilo == 'Hip Hop':
        artista = random.choice(artistas_hip_hop)
    if estilo == 'Sertanejo':
        artista = random.choice(artistas_sertanejo)
    if estilo == 'Eletrônica':
        artista = random.choice(artistas_eletronica)

    tabela.append([nome, estilo, artista])


# A tabela usuarios vai ser o nosso dataframe base para trablharmos em cima do grafo
usuarios = pd.DataFrame(tabela, columns=['nome', 'estilo', 'artista favorito'])


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

        # Fazer a busca no grafo das pessoas que escutam aquele mesmo artista e retornar em um for dando insert
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
