import os
import random
import shutil
fisierprim = os.path.abspath(__file__)
fisierprim_path = os.path.dirname(fisierprim)
fisierprim_pathdy = os.path.dirname(fisierprim)

class document():
    def __init__(self, nume, extensie):
        self.nume = nume
        self.extensie = extensie
    

def repet(fisier):
    files = os.listdir(fisier)
    lista= []
    l= []
    temp= []
    for file_name in files:
        file_name, file_extension = os.path.splitext(fisier+'\\'+file_name)
        file_name=file_name[len(fisier+'\\'):]
        lista.append(document(file_name, file_extension))
    rra=[]
    for i in range(len(lista)):
        if lista[i].extensie=='':
            repet(fisier+'\\'+lista[i].nume)
        elif lista[i].extensie=='.rar' or lista[i].extensie=='.py':
            pass
            #print(lista[i].nume)
        else:
            
            c=random.randint(1,10)
            
            if c==1:
                
                tsttt=False
                while tsttt==False:
                    c=random.randint(1,100000)
                    tsttt=True
                    for n in range(len(rra)):
                        if rra[n]==c:
                            tsttt=False
                            
                rra.append(c)
                shutil.copyfile(fisier+'\\'+lista[i].nume+lista[i].extensie, fisierprim_pathdy+'\\'+'rrand'+'\\'+str(c)+lista[i].extensie)
da=False

file=os.listdir(fisierprim_pathdy)
for file_name in file:
    if file_name=='rrand':
        da=True
if da==False:
    os.makedirs(fisierprim_pathdy+'\\'+'rrand')

repet(fisierprim_path)