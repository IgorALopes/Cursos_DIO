import os #Importa o módulo ou biblioteca os (integra os programas e recursos do S.O)

print('#' * 60) #Imprimindo o # 60 vezes
#criamos uma variável que vai receber do usuário um ip
ip_ou_host = input('Digite o IP ou host a ser verificado: ')
print('-' * 60) #Imprimindo o - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) ##chamando o system da biblioteca os - comando ping -n -num de pacotes que serão 6 {}
print('-' * 60) #Imprimindo o - 60 vezes