import tkinter as tk
from functools import partial

class JanelaPadrão():
    def __init__(self):
        pass

    def _make_window(self, titulo = "Padrão", largura = 300, altura = 300):
        self.__temp_window = tk.Tk()
        self.__temp_window.geometry(f'{largura}x{altura}')
        self.__temp_window.resizable(width=0, height=0)
        self.__temp_window.title(titulo)
        return self.__temp_window
    
    def _make_button(self, pai=None, texto="Padrão", largura=20, altura=1, comando=None, local_x=0, local_y=0):
        self.__temp_button = tk.Button(pai, width=largura, height=altura, text=texto)
        self.__temp_button["command"] = partial(comando, self.__temp_button)
        self.__temp_button.place(x=local_x, y=local_y)
        return self.__temp_button
    
    def _make_entry(self, pai=None, largura=22, altura=1, local_x=0, local_y=0):
        self.__temp_entry = tk.Entry(pai, width=largura)
        self.__temp_entry.place(x=local_x, y=local_y)
        return self.__temp_entry

    
    
    def _make_label(self, pai=None, texto="", local_x=0, local_y=0):
        self.__temp_label = tk.Label(pai, text=texto)
        self.__temp_label.place(x=local_x, y=local_y)
        return self.__temp_label


class JanelaLogin(JanelaPadrão):
    def __init__(self):
        pass
    
    def bt_click(self, btn):
        pass

    def run(self):
        self.root = self._make_window("Sistema Escola - Login", 408, 537)
        
        #Titulo
        self.label_titulo = self._make_label(self.root, 'Acessar Sistema Escola', local_x=125, local_y=150)
        
        #Entrada usuário
        self.label_usuario = self._make_label(self.root, 'Usuário', 57, 180)
        self.entry_usuario = self._make_entry(self.root, 23, 1, 115, 180)

        #Entrada senha
        self.label_senha = self._make_label(self.root, 'Senha', 66, 210)
        self.entry_senha = self._make_entry(self.root, 23, 1, 115, 210)
        self.entry_senha['show'] = '*'

        #Botão acessar
        self.button_entrar = self._make_button(self.root, 'Entrar', 20, 1, self.bt_click, 105, 270)
        
        #Botões Cadastrar e Recuperar
        self.button_cadastrar = self._make_button(self.root, 'Cadastrar', 15, 1, self.bt_click, 30, 450)
        self.button_recuperar = self._make_button(self.root, 'Recuperar', 15, 1, self.bt_click, 215, 450)
        
        #Versão
        self.label_titulo = self._make_label(self.root, 'v0.01', local_x=350, local_y=515)
        
        self.root.mainloop()
        