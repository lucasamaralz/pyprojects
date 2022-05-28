import time
import os
from modulos.PainelUsuario import Central_Usuario


t = 0.5
t1 = 1
print('Bem-Vindo ao Sistema de Login!! \n ')
nvarb=input('Digite seu Nome: ')
nome = nvarb.lstrip().lower().title()

os.system("cls")

class Sistema_login():

 def Menu():
    print(f'Escolha um dos Itens a Baixo {nome}: \n Login - Cadastro - Info - CTxt \n')
    Escolha = input('Digite: ')
    Ajuste_Escolha = Escolha.lstrip().lower().title().rstrip()

    if (Ajuste_Escolha=="Login"):
        time.sleep(t)
        Sistema_login.Login()

    if (Ajuste_Escolha=="Cadastro"):
        time.sleep(t)
        Sistema_login.Cadastro()


    if (Ajuste_Escolha=="Info"):
        time.sleep(t)
        Sistema_login.Info()

    else:
        print('Digite Novamente: ')
        Sistema_login.Menu()

 def Login():
     contas = open('contas.txt')
     print('Digite seu Usuário ')
     user_cadastro = input()
     print('Digite sua Senha: ')
     user_senha = input()
     contas = contas.readlines()
     if user_cadastro + '\n' in contas and user_senha + '\n' in contas:
         print('Você está logando!')
         time.sleep(t)
         print('Aguarde.')
         time.sleep(t1)
         print('Aguarde..')
         time.sleep(t1)
         print('Aguarde...')
         time.sleep(t1)
         print(f'Logado Com SUCESSO! {nome}')
         Sistema_login.Logado()
         contas.close()
     else:
         print('Sua senha está ERRADA!!\n Você será redirecionado ao MENU!')
         time.sleep(t)
         contas.close()
         Sistema_login.Menu()

 def Logado():
     print('Redirencionando!')
     Central_Usuario.Painel()

 def Cadastro():
     contas = open('contas.txt', 'a')
     print('Usuário ')
     user_cadastro = str(input('Digite o Usuário: '))
     contas.write('{}\n'.format(user_cadastro))
     user_senha = str(input('Digite o Senha: '))
     contas.write('{}\n'.format(user_senha))
     print(f'Cadastro Realizado com Sucesso {nome}!!! \n Você será redirecionado para o Menu!!')
     time.sleep(t1)
     contas.close()
     Sistema_login.Menu()

 def Info():
     print('Menu de Info')

Sistema_login.Menu()





