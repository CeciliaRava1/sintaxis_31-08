cadena=""
vectorcontador=[0]*14
cadena=input()
cadena = cadena + " "

for i in range(len(cadena)):
    if cadena[i]==">":
        if cadena[i+1]=="=":                           
            vectorcontador[3]+=1
        else:
            vectorcontador[0]+=1
    
    if cadena[i]=="<":
        if cadena[i+1]=="=":
            vectorcontador[4]+=1
        else:
            vectorcontador[1]+=1
    
    
    if cadena[i]=="=":
        if cadena[i-1]!=">" and cadena[i-1]!="<":
            vectorcontador[2]+=1

        

    if cadena[i]=="&":
        vectorcontador[5]+=1

    if cadena[i]=="|":
        vectorcontador[6]+=1

    if cadena[i]=="~":
        vectorcontador[7]+=1

    if cadena[i]=="+":
        vectorcontador[8]+=1
    
    if cadena[i]=="-":
        vectorcontador[9]+=1
    
    if cadena[i]=="*":
        vectorcontador[10]+=1
    
    if cadena[i]=="/":
        vectorcontador[11]+=1
    
    if cadena[i]=="^":
        vectorcontador[12]+=1
    
    if cadena[i]=="%":
        vectorcontador[13]+=1

vectorsimbolos=[">","<","=",">=","<=","&","|","~","+","-","*","/","^","%"]

for i in range(14):
    if i == 0 and (vectorcontador[0] + vectorcontador[1] + vectorcontador[2] + vectorcontador[3] + vectorcontador[4])!=0:
        print("Relacionales")
    if i == 5 and (vectorcontador[5] + vectorcontador[6] + vectorcontador[7])!=0:
        print("Lógicos")
    if i == 8 and (vectorcontador[8] + vectorcontador[9] + vectorcontador[10] + vectorcontador[11] + vectorcontador[12] + vectorcontador[13])!=0:
        print("Aritméticos")
    if vectorcontador[i]!=0:
        print("Cantidad de",vectorsimbolos[i],":",vectorcontador[i])
    






