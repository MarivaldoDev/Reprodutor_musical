import pygame
import os
import re
import pysnooper
from customtkinter import *
from random import randint
from tkinter import Menu
from PIL import Image
from CTkTable import CTkTable


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
        self.row = 1
        self.item_selecionado = self.frame1.select_row(row=self.row)  # Obtém o item selecionado
        self.valor = self.frame1.get_selected_row()

        print('musica atual: ', self.valor['values'][1])

        pygame.mixer.music.load(self.valor['values'][1])
        pygame.mixer.music.play()

        self.texto = self.regex(self.valor['values'][1])
        
        self.tocando = CTkLabel(self.tela, text=self.texto, text_color='black',
        font=('hervetica', 14),
        fg_color='#3CB371',
        bg_color='#3CB371')

        
        self.tocando.place(x=80, y=320)
                     

    def pausar(self):
        self.play_butao.configure(image=self.play_oficial, command=self.despause)
        pygame.mixer.music.pause()


    def despause(self):
        self.play_butao.configure(image=self.pause_oficial, command=self.pausar)
        pygame.mixer.music.unpause()


    # @pysnooper.snoop(r'C:\Users\mariv\OneDrive\Documentos\reprodutor\saida.log') 
    def proxima(self):
        try:
            if self.row == self.n - 1:
                print('Final das músicas!')
            else:
                self.frame1.deselect_row(self.row)
                self.row += 1
                self.selecionada = self.frame1.select_row(row=self.row)  # Obtém o item selecionado
                self.passou = self.frame1.get_selected_row()
               
                self.new_musics = self.passou['values'][1]       
                

                pygame.mixer.music.load(self.new_musics)
                pygame.mixer.music.play()

                self.texto = self.regex(self.new_musics)

                self.tocando.configure(text=self.texto)
               
                print('_'*50)
                print('musica atual: ', self.new_musics)
                print('_'*50)
        except:
            pass


    def voltar(self):
        try:
            if self.row == 1:
                print('Não pode voltar mais!')
            else:
                self.frame1.deselect_row(self.row)
                self.row -= 1
                self.selecionada = self.frame1.select_row(row=self.row)  # Obtém o item selecionado
                self.voltou = self.frame1.get_selected_row()
               
                self.new_musics = self.voltou['values'][1]
                
                pygame.mixer.music.load(self.new_musics)
                pygame.mixer.music.play()
               
                self.texto = self.regex(self.new_musics)
                self.tocando.configure(text=self.texto)

                print('_'*50)
                print('musica atual: ', self.new_musics)
                print('_'*50)
        except:
            pass


    def aleatoria(self):
        self.frame1.deselect_row(self.row)
        self.row = randint(1, self.n - 1)
        
        self.selecionada = self.frame1.select_row(row=self.row)  # Obtém o item selecionado
        self.escolhida = self.frame1.get_selected_row()
        self.new_musics =  self.escolhida['values'][1]


        pygame.mixer.music.load(self.new_musics)
        pygame.mixer.music.play()
        
        self.texto = self.regex(self.new_musics)
        self.tocando.configure(text=self.texto)

        print('_'*50)
        print(f'{self.row} - musica atual: {self.new_musics}')
        print('_'*50)


    def repetir(self):
        pygame.mixer.music.load(self.new_musics)
        pygame.mixer.music.play()      
         
        self.texto = self.regex(self.new_musics)
        self.tocando.configure(text=self.texto)
    

    def frame(self):
        self.principal = CTkFrame(
            master=self.tela,
            width=300,
            height=280)
        
        self.principal.propagate(0)

        self.principal.place(x=53, y=20)


    def tabela(self):
        self.cabecalho = (['Nº', 'Nome'])
        self.tabela_musicas = self.mostrar()
        
        self.tabela_musicas.insert(0, self.cabecalho)
        
        
        self.rolinho = CTkScrollableFrame(master=self.principal, fg_color='transparent', height=20)
        self.rolinho.pack(expand=True, fill='both')

        self.frame1 = CTkTable(master=self.rolinho, 
        values=self.tabela_musicas,
        wraplength=380,
        header_color='#008080',
        text_color='#F0FFFF',
        font=('Verdana', 12),
        command=self.play)
       
        self.frame1.edit_row(row=0)
        self.frame1.pack(expand=True)
        

    def mostrar(self):
        self.n =  1
        self.musicas = os.listdir(self.pasta_selecionada)
        self.lista = []

        for i in self.musicas:
            self.lista.append([self.n, i]) 
            self.n += 1
       
        return self.lista
       

    def procurar_pasta(self):
        self.pasta_selecionada = filedialog.askdirectory()
        self.tabela()


    def menu(self):
        pastas = Menu(self.tela)
        self.tela.config(menu=pastas)
    
        pastas.add_command(label="Procurar pasta", command=self.procurar_pasta)


    def regex(self, texto):
        nome_do_arquivo = texto
        # Definindo o padrão regex para extrair o nome da música
        padrao = r"\d+-(.*?)-\d+\.mp3"
        # Aplicando o padrão regex à string
        correspondencia = re.search(padrao, nome_do_arquivo)
        # Verificando se houve uma correspondência e extraindo o nome da música
        if correspondencia:
            nome_da_musica = correspondencia.group(1)
            print(nome_da_musica)
            return nome_da_musica
        else:
            padrao = r"-(.*?)-\w+\.mp3"
            correspondencia = re.search(padrao, nome_do_arquivo)
            if correspondencia:
                nome_da_musica = correspondencia.group(1)
                print(nome_da_musica)
                return nome_da_musica


    def main(self):
        self.tela = CTk()
        self.tela.title('Mini Spotify')
        self.tela.geometry('410x460')
        self.tela.iconbitmap('imgs/logo2.ico')
        self.tela.config(background='#3CB371')

        
        
        self.img_play = Image.open('imgs\play.png')
        self.play_oficial = CTkImage(dark_image=self.img_play, light_image=self.img_play,size=(110, 70))
        self.play_butao = CTkButton(self.tela, text='', image=self.play_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#3CB371',
        hover_color='#3CB371', 
        command=self.play)
        self.play_butao.place(x=137, y=365)


        self.img_passar = Image.open('imgs\passar.png')
        self.passar_oficial = CTkImage(dark_image=self.img_passar, light_image=self.img_passar,size=(90, 50))
        self.passar = CTkButton(self.tela, text='', image=self.passar_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#3CB371',
        hover_color='#3CB371', 
        command=self.proxima)
        self.passar.place(x=242, y=360)


        self.img_voltar = Image.open(r'imgs\voltar2.png')
        self.voltar_oficial = CTkImage(dark_image=self.img_voltar, light_image=self.img_voltar,size=(70,50))
        self.voltar_musica = CTkButton(self.tela, text='', image=self.voltar_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#3CB371',
        hover_color='#3CB371',  
        command=self.voltar)
        self.voltar_musica.place(x=58, y=360)

        
        self.img_aleatoria = Image.open(r'imgs\aleatoria.png')
        self.aleatoria_oficial = CTkImage(dark_image=self.img_aleatoria, light_image=self.img_aleatoria,size=(30,40))
        self.musica_aleatoria = CTkButton(self.tela, text='', image=self.aleatoria_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#3CB371',
        hover_color='#3CB371',  
        command=self.aleatoria)
        self.musica_aleatoria.place(x=-20, y=385)


        self.img_repetir = Image.open(r'imgs\repetir.png')
        self.repetir_oficial = CTkImage(dark_image=self.img_repetir, light_image=self.img_repetir,size=(40,30))
        self.repetir_musica = CTkButton(self.tela, text='', image=self.repetir_oficial,
        width=100, 
        fg_color='transparent',
        bg_color='#3CB371',
        hover_color='#3CB371',  
        command=self.repetir)
        self.repetir_musica.place(x=330, y=393)



Spotify()