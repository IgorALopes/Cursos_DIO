import ctypes

#pasta = input('Digite o caminho da pasta a ser ocultada. ex. (c:/pasta)')

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)
#Para ocultar uma pasta, substutuir o 'ocultar.txt' pela variável pasta.

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')