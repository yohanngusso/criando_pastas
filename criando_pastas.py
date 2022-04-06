# https://acervolima.com/faca-varios-diretorios-com-base-em-uma-lista-usando-python/ 
import os
userhome = os.path.expanduser('~') #aqui vai até a pasta C: do usuario com o nome exemplo: C:\Users\Yohann
print(userhome)
print(os.getcwd())
os.chdir(userhome + "\Documents\sla\MSC" ) # AQUI MUDA O DIRETÓRIO(CHDIR DE CHANGE DIRETORIO)
print(os.getcwd()) # mostra no terminal onde está o diretório atual

list = ['Material Didático','Plano de Ensino','Atividades Formativas','Atividades Somativas','Atividades TDE']

for items in list:
    if not os.path.exists(items):
        os.makedirs(items)