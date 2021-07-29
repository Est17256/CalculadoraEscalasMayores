#Luis Esturban 17256
#Musica computacional
notas=["DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SI","DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SOL"]
while True:
    try:
        Escala=[]
        nota=input("Ingrese la nota que quiere comprobar: ")
        nota=nota.upper()
        Escala.append(nota)
        actual=notas.index(nota)
        for i in range(6):
            if i==2:
                actual=actual+1
                Escala.append(notas[actual])
            elif i==6:
                actual=actual+1
                Escala.append(notas[actual])
            else:
                actual=actual+2
                Escala.append(notas[actual])
        print("Escala:")
        print(Escala)
        Escala=Escala+Escala
        Acordes=[]
        cont=0
        for i in Escala:
            cont+=1
            if cont==8:
                break
            else:
                temp=[]
                actual=Escala.index(i)
                temp.append(Escala[actual])
                temp.append(Escala[actual+2])
                temp.append(Escala[actual+4])
                Acordes.append(temp)
        cont2=0
        for i in Acordes:
            cont2+=1
            print("Acorde N.",cont2)
            print(i)
    except:
        print("ingrese una nota valida")