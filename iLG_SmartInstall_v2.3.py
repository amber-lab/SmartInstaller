# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:31:06 2019

@author: L.A.B
"""
import subprocess
from time import sleep
from os import getcwd, listdir, remove, mkdir
import tkinter as tk
from PIL import Image, ImageTk
import requests

from platform import architecture
import zipfile
from threading import Thread

#   Main Classe
class MainApp(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.CWD = getcwd()
        self.geometry("+{}+20".format(int(self.winfo_screenwidth() / 2) - 125))
        self.title("Smart Install")
        self.resizable(False,False)
        self.iconbitmap('icons\\1icon.ico')
        mainframe = tk.Frame(self, background = "grey")
        mainframe.pack()
        if 'temp' not in listdir():
            mkdir('temp')
        ilg_label = tk.Label(mainframe, text = "Smart Install\nInformática LG", font = ("Verdana", 15), bg = "grey", fg = "black")
        ilg_label.grid(row = 0, column = 0)
        
        ccleaner = {'nomes' : ['ccsetup.exe'],
                    'comandos' : '.\\temp\\ccsetup.exe /S', 
                    'links' : {'url_dl_both' : ['https://download.ccleaner.com/ccsetup{vp}.exe'], 'url_ud' : 'https://www.ccleaner.com/pt-br'},
                    'tipo' : 'versao',
                    'procura' : 'CCleaner v',
                    'comp' : 4,
                    'dir' : 'CCleaner'}
        ccleaner_ln= Linha(mainframe, texto = "Ccleaner", imagem = "icons\\ccleaner.png")
        ccleaner_ln.grid(row = 1, column = 0)
        self.ccleaner_sw = Software(ccleaner, ccleaner_ln)
        
        cdburner = {'nomes' : ['cdburner.exe'],
                    'comandos' :'.\\temp\\cdburner.exe /VERYSILENT',
                    'links' : {'url_dl_both' : ['https://download.cdburnerxp.se/cdbxp_setup_{vp}.exe'], 'url_ud' : 'https://cdburnerxp.se/en/home'},
                    'tipo' : 'versao',
                    'procura' : 'Version ',
                    'comp' : 10,
                    'dir' : 'CDBurnerXP.lnk'}
        cdburner_ln = Linha(mainframe, texto = "CD Burner XP", imagem = "icons\\cdburnerxp.png")
        cdburner_ln.grid(row = 2, column = 0)
        self.cdburner_sw = Software(cdburner, cdburner_ln)
        
        
        chrome = {'nomes' : ['chrome.exe'],
                  'comandos' : '.\\temp\\chrome.exe /silent /install',
                  'links' : {'url_dl_both' : ['https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BE19FF4D0-E186-D791-E19C-F0EE7162EF22%7D%26lang%3Dpt-PT%26browser%3D5%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe']},
                  'tipo' : 'online',
                  'dir' : 'Google Chrome.lnk'}
        chrome_ln = Linha(mainframe, texto = "Chrome", imagem = "icons\\chrome.png" )
        chrome_ln.grid(row = 3, column = 0)
        self.chrome_sw = Software(chrome, chrome_ln)
        
        java = {'nomes' : ['java.exe'],
                'comandos' : '.\\temp\\java.exe /s',
                'links' : {'url_dl_both' : ['{vp}'], 'url_ud' : 'https://www.java.com/pt_BR/download/manual.jsp'},
                'tipo' : 'versao',
                'procura' : 'Windows On-line" href="',
                'comp' : 111,
                'dir' : 'Java'}
        java_ln = Linha(mainframe, texto = "Java", imagem = "icons\\java.png")
        java_ln.grid(row = 4, column = 0)
        self.java_sw = Software(java, java_ln)
        
        k_lite = {'nomes' : ['klitecodec.exe'],
                  'comandos' : '.\\temp\\klitecodec.exe /verysilent',
                  'links' : {'url_dl_both' : ['http://files2.codecguide.com/K-Lite_Codec_Pack_{vp}_Mega.exe'], 'url_ud' : 'https://www.codecguide.com/download_k-lite_codec_pack_mega.htm'},
                  'tipo' : 'versao',
                  'procura' : 'K-Lite_Codec_Pack_',
                  'comp' : 4,
                  'dir' : 'K-Lite Codec Pack'}
        k_lite_ln = Linha(mainframe, texto = "K Lite Codec", imagem = "icons\\k_lite_codec.png")
        k_lite_ln.grid(row = 5, column = 0)
        self.k_lite_sw = Software(k_lite, k_lite_ln)
        
        winrar = {'nomes' : ['winrar.exe'],
                  'comandos' : '.\\temp\\winrar.exe /S',
                  'links' : {'url_dl_64' : ['https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-{vp}br.exe'], 'url_dl_32' : ['https://www.win-rar.com/fileadmin/winrar-versions/winrar/wrar{vp}br.exe'], 'url_ud' : 'https://www.win-rar.com/download.html'} ,
                  'tipo' : 'versao',
                  'procura' : 'class="download-link" >WinRAR ',
                  'comp' : 4,
                  'dir' : 'WinRAR'}
        winrar_ln = Linha(mainframe, texto = "WinRar", imagem = "icons\\winrar.png")
        winrar_ln.grid(row = 6, column = 0)
        self.winrar_sw = Software(winrar, winrar_ln)
        
        self.f_butoes_inst = F_butao(mainframe)
        self.f_butoes_inst.grid(row = 7, column = 0)
        self.f_butoes_inst.func_button.bind('<ButtonRelease-1>', self.buttonThread)

        lab_label = tk.Label(mainframe, text = "Desenvolvido por L.A.B", bg = "grey", fg = "black", font = ('Verdana', 12))
        lab_label.grid(row = 8, column = 0)
        self.inst_l = [self.ccleaner_sw, self.cdburner_sw, self.chrome_sw, self.java_sw, self.k_lite_sw, self.winrar_sw]

    
    def mainFunction(self):
        for inst in self.inst_l:
            if inst.linha.linha_int_var.get():
                inst_t = Thread(target=inst.install)
                inst_t.start()
                sleep(0.2)
    
    def buttonThread(self, event):
        try:
            if self.but_thread.isalive():
                pass
        except:
            self.but_thread = Thread(target = self.mainFunction)
            self.but_thread.start()

#Definiçao de Objetos
class F_butao(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=250, height = 75, bg = 'grey')
        self.func_button = tk.Button(self, text = "Instalar", font = ('Verdana', 12), bg = 'white', fg = 'black')
        self.func_button.place(relx = 0.2, rely = 0.15, width = 150, height = 50)

#Classe de Linha de programas
class Linha(tk.Frame):
    def __init__(self, parent, texto, imagem):
        tk.Frame.__init__(self, parent, width=300, height = 55)

        linha_image_f = ImageTk.PhotoImage(Image.open(imagem))
        linha_l = tk.Label(self, image = linha_image_f)
        linha_l.photo = linha_image_f
        linha_l.place(relx = 0.05)
        
        self.linha_int_var = tk.IntVar()
        self.linha_cb_inst = tk.Checkbutton(self, text = texto, variable = self.linha_int_var, bg = 'white', fg = 'black', selectcolor = 'white')
        self.linha_cb_inst.place(relx = 0.3, rely = 0.2)
        
        self.status_l = tk.Label(self)
        
    def setText(self, texto):
        self.status_l = tk.Label(self, text= texto)
        self.status_l.place(relx = 0.7, rely = 0.2)
# CLASSE DE UPDATE, DOWNLOAD, INSTALATION     
class Software():
    def __init__(self, info, linha):
        #DICT   info(nome, valor, comandos, links{}, paths[], tipo, procura, comp, diferenca) 
        self.__dict__ = info
        self.linha = linha
        self.bit = architecture()[0][0:2]
        self.versao = 0
        self.ready = 0
        self.check()

    def check(self):
        path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'
        if self.dir in listdir(path):
            print('{n} INSTALADO!'.format(n=self.nomes[0]))
            self.linha.setText('Instalado!\t\t')
            self.ready = 1
        else:
            self.linha.setText('Não Instalado!\t\t')
            print('{n} NÃO INSTALADO!'.format(n=self.nomes[0]))

    def get_version(self):
        if self.tipo == 'versao':
            if 'procura' in self.__dict__.keys():
                data = requests.get(self.links['url_ud']).content.decode('utf-8')
                l1 = data.find(self.procura)+len(self.procura)
                l2 = l1 + self.comp
                versao = data[l1:l2]
                if 'ccsetup.exe' in self.nomes or 'winrar.exe' in self.nomes:
                    self.versao = int(float(data[l1:l2]) * 100)
                    print('{n} ATUALIZADO! para versao {v}'.format(n =self.nomes[0], v = self.versao))
                elif 'java.exe' in self.nomes:
                    self.versao = versao.split('">')[0]
                    print('{n} ATUALIZADO! para versao {v}'.format(n =self.nomes[0], v = self.versao))
                else:
                    self.versao = versao
                    print('{n} ATUALIZADO! para versao {v}'.format(n =self.nomes[0], v = self.versao))
                self.linha.setText('A atualizar\t\t')

    def format_path(self, bit, index, url):
        key = 'url_dl_{b}'.format(b=bit)
        if '{vp}' in self.links[key][index]:
            url = url.format(vp = self.versao)
        elif self.tipo == 'online':
            print("ONLINE")
        else:
            print('DEAD END FORMATPATH')
        return url

    def bit_download(self,bit):
        key = 'url_dl_{b}'.format(b=bit)
        for index, url in enumerate(self.links[key]):
            path = self.format_path(bit, index, url)
            print(path)
            conn = requests.get(path)
            data = conn.content
            conn.close()
            open('.\\temp\\'+self.nomes[index], 'wb').write(data)
        return True

    def download(self):
        if self.bit == '32' and 'url_dl_32' in self.links.keys():
            self.bit_download('32')
            print('{n} DESCARREGADO!'.format(n = self.nomes[0]))
            return True
        elif self.bit == '64' and 'url_dl_64' in self.links.keys():
            self.bit_download('64')
            print('{n} DESCARREGADO!'.format(n = self.nomes[0]))
            return True
        elif 'url_dl_both' in self.links.keys():
            self.bit_download('both')
            print('{n} DESCARREGADO!'.format(n = self.nomes[0]))
            return True
        else:
            print("DEAD END DOWNLOAD HTTPS")
            return False

    def extract(self):  
        if 'zip' in self.__dict__.keys():
            bit = 'zip_{b}'.format(b=self.bit)
            if bit in self.zip.keys():
                self.linha.setText('A extrair...\t\t')
                zip_f = zipfile.ZipFile('.\\temp\\{n}'.format(n = self.nomes[0]))
                name = self.nomes[0].split('.')[0]
                ext = self.zip[bit].split('.')[-1]
                file = open('.\\temp\\{n}.{e}'.format(n = name, e = ext), 'wb')
                file.write(zip_f.read(self.zip[bit]))
                sleep(15)
                
    def clean(self):
        if self.ready == 1:
            for n in self.nomes:
                remove('.\\temp\\{nm}'.format(nm = n))
            self.linha.setText('Pronto!\t\t')
                
    def install(self):
        self.linha.setText('A atualizar...\t\t')
        sleep(2)
        self.get_version()
        self.linha.setText('Atualizado!\t\t')
        sleep(2)
        self.linha.setText('A descarregar...\t\t')
        sleep(2)
        self.download()
        self.linha.setText('Descarregado!\t\t')
        sleep(2)
        self.extract()
        self.linha.setText('A Instalar...\t\t')
        sleep(2)
        print(self.comandos)
        subprocess.Popen(self.comandos, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("{n} A INSTALAR!".format(n = self.nomes[0]))
        sleep(60)
        self.check()
        self.clean()

app = MainApp()
app.mainloop()