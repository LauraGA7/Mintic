n=int(input())
sumPro=0
ivafinal=0
for i in range(n):
    cod=int(input())
    num=input()
    canC=float(input())
    vUni=float(input())
    iva=input()
    if iva== '1': 
        vIva=vUni*canC
        vfIva=0
    elif iva == '2':
        vIva=(vUni+(vUni*0.05))*canC
        vfIva=(vUni*0.05)*canC
    else:
        vIva = (vUni+(vUni*0.19))*canC
        vfIva=(vUni*0.19)*canC
    sumPro=vUni+vIva
    ivafinal=ivafinal+vfIva

    print(cod)
    print(num)
    print(vUni*canC)
    print(vIva)
print(sumPro)
print(ivafinal)