from colorama import Fore, init
import os, webbrowser
init()

#  Imprime a capa do programa
f = open('assets/fancyart.txt', 'r')
show = ''.join(f.readlines())
print(Fore.RED, show)

#   Impede que o usuário deixe o campo de url vazio
url = ''
while url == '':
    url = str(input('>>> URL: ')).strip()

#   Verifica se a url é válida
while url[:24] != 'https://www.youtube.com/':
    print('url inválida!')
    url = str(input('>>> URL: ')).strip()

#  Fatia a string para adcionar o 'ss'
url_slice1 = url[:12]
url_slice2 = url[12:]

#   Concatena as duas fatias, sendo que na primeira foi adcionado ss
new_url = url_slice1 + 'ss' + url_slice2
#   Abre uma nova aba do navegador, dierecionando o usuário para a página de download...
webbrowser.open_new_tab(new_url)



