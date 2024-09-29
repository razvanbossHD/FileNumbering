import os
import time
fisierprim = os.path.abspath(__file__)
fisierprim_path = os.path.dirname(fisierprim)

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

    for i in range(len(lista)):
        if lista[i].extensie=='':
            repet(fisier+'\\'+lista[i].nume)
        elif lista[i].extensie=='.rar' or lista[i].extensie=='.py':
            pass
            #print(lista[i].nume)
        else:
            if lista[i].nume.isdigit():
                l.append(lista[i])
            else:
                temp.append(lista[i])
    for i in range(len(l)):
        for j in range(len(l)):
            if int(l[i].nume)<int(l[j].nume):
                tp=l[i]
                l[i]=l[j]
                l[j]=tp
    x=len(l)
    for i in range(x):
        if int(l[x-1-i].nume) != i+1:
            os.rename(fisier+'\\'+l[x-1-i].nume+l[x-1-i].extensie,fisier+'\\'+str(x-i)+l[x-1-i].extensie)
    for i in range(len(temp)):
        os.rename(fisier+'\\'+temp[i].nume+temp[i].extensie,fisier+'\\'+str(i+1+x)+temp[i].extensie)
repet(fisierprim_path)
sleep(10)