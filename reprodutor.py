import pygame
import os
from customtkinter import *
from random import randint
from tkinter import ttk, Menu
from PIL import Image



pygame.mixer.init()


class Spotify():
    def __init__(self):
        self.main()
        self.frame()
        self.menu()
        self.tela.mainloop()



    def play(self, event):
        self.img_pause = Image.open('imgs\pause.png')
        self.pause_oficial = CTkImage(dark_image=self.img_pause, light_image=self.img_pause,size=(110, 70))
        self.play_butao.configure(image=self.pause_oficial, command=self.pausar)

        os.chdir(self.pasta_selecionada)
        self.item_selecionado = self.lista.focus()  # Obtém o item selecionado
        self.valores = self.lista.item(self.item_selecionado, "values")
        print(f'musica atual: {self.valores}') # Obtém os valores associados ao item
        pygame.mixer.music.load(self.valores[1])
        pygame.mixer.music.play()

        self.tocando = CTkLabel(self.tela, text=self.valores[1].replace('.mp3', ''), text_color='black',
        font=('hervetica', 14) ,
        fg_color='#2E8B57',
        bg_color='#2E8B57')
        self.tocando.place(x=40, y=300)


    def pausar(self):
        self.play_butao.configure(image=self.play_oficial, command=self.despause)
        pygame.mixer.music.pause()


    def despause(self):
        self.play_butao.configure(image=self.pause_oficial, command=self.pausar)
        pygame.mixer.music.unpause()


    def proxima(self):
        try:
            print(f'valor inicial: {self.valores}')
            self.index = self.valores[0]
            novo_index = int(self.index) + 1
            print(f'index: {self.index}')
            print(f'novo index: {novo_index}')
            self.new_musics = ''
            
            for item in self.lista.get_children():
                valores = self.lista.item(item, 'values')
                # print(valores)
                if int(valores[0]) == novo_index:
                    self.new_musics = valores[1]
                    break
                    
            pygame.mixer.music.load(self.new_musics)
            pygame.mixer.music.play()
            self.tocando.configure(text=self.new_musics.replace('.mp3', ''))
            self.valores = valores
            # print(self.valores)
            print(f'musica atual: {self.valores}')
            print('_'*50)
        except:
            pass


    def voltar(self):
        try:
            print(f'valor inicial: {self.valores}')
            index = self.valores[0]
            novo_index = int(index) - 1
            #self.comeca = self.valores[novo_index]
            print(f'index: {index}')
            print(f'novo index: {novo_index}')
            self.new_musics = ''
            for item in self.lista.get_children():
                valores = self.lista.item(item, 'values')
                # print(valores)
                if int(valores[0]) == novo_index:
                    self.new_musics = valores[1]
                    break
                    
            pygame.mixer.music.load(self.new_musics)
            pygame.mixer.music.play()
            self.tocando.configure(text=self.new_musics.replace('.mp3', ''))
            self.valores = valores
            # print(self.valores)
            print(f'musica atual: {self.valores}')
            print('_'*50)
        except:
            pass


    def aleatoria(self):
        valor = randint(0, self.n)
        self.index = valor
        self.new_musics = ''

        for item in self.lista.get_children():
            valores = self.lista.item(item, 'values')
            # print(valores)
            if int(valores[0]) == self.index:
                self.new_musics = valores[1]
                break

        pygame.mixer.music.load(self.new_musics)
        pygame.mixer.music.play()
        self.tocando.configure(text=self.new_musics.replace('.mp3', ''))
        self.valores = valores
        # print(self.valores)
        print(f'musica atual: {self.valores}')
        print('_'*50)


    def main(self):
        self.tela = CTk()
        self.tela.title('Mini Spotify')
        self.tela.geometry('342x450')
        self.tela.iconbitmap('imgs/logo2.ico')
        self.tela.config(background='#2E8B57')
        
        self.img_play = Image.open('imgs\play.png')
        self.play_oficial = CTkImage(dark_image=self.img_play, light_image=self.img_play,size=(110, 70))
        self.play_butao = CTkButton(self.tela, text='', image=self.play_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#2E8B57',
        hover_color='#2E8B57', 
        command=self.play)
        self.play_butao.place(x=105, y=350)


        self.img_passar = Image.open('imgs\passar.png')
        self.passar_oficial = CTkImage(dark_image=self.img_passar, light_image=self.img_passar,size=(120, 80))
        self.passar = CTkButton(self.tela, text='', image=self.passar_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#2E8B57',
        hover_color='#2E8B57', 
        command=self.proxima)
        self.passar.place(x=215, y=335)


        self.img_voltar = Image.open(r'imgs\voltar2.png')
        self.voltar_oficial = CTkImage(dark_image=self.img_voltar, light_image=self.img_voltar,size=(100,80))
        self.voltar = CTkButton(self.tela, text='', image=self.voltar_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#2E8B57',
        hover_color='#2E8B57',  
        command=self.voltar)
        self.voltar.place(x=0, y=335)


    def frame(self):
        self.frame1 = CTkFrame(self.tela, width=280, height=280)
        self.frame1.place(x=30, y=10)


        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 20, "bold"))
        style.theme_use('clam')

        self.lista = ttk.Treeview(self.frame1, height=3, columns=("col1", "col2"))
        self.lista.heading("#0", text="")
        self.lista.heading("#1", text="Nº")
        self.lista.heading("#2", text="NOME")

        self.lista.bind("<Double-1>", self.play)

        self.lista.column("#0", width=0)
        self.lista.column("#1", width=23)
        self.lista.column("#2", width=300)
        self.lista.place(x=5, y=5, width=340, height=340)
    

    def mostrar(self):
        self.n =  0
        self.musicas = os.listdir(r'C:\Users\mariv\OneDrive\Área de Trabalho\songs')
        for i in self.musicas:
           self.lista.insert('', END, values=(self.n, i)) 
           self.n += 1
       

    def procurar_pasta(self):
        self.pasta_selecionada = filedialog.askdirectory()
        self.mostrar()


    def menu(self):
        pastas = Menu(self.tela, bg='black')
        self.tela.config(menu=pastas)
    
        pastas.add_command(label="Procurar pasta", command=self.procurar_pasta)
        pastas.add_command(label='Música Aleatória', command=self.aleatoria)




Spotify()
