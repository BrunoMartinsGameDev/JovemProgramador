idade = int(input("Por favor, me diga, qual a sua idade para eu saber em qual \n categoria de Nadador você se classifica! "))
categoria = ""

def imprimir(categorias):
    print("Você é da categoria", categorias,"!")

if idade <5:
    print("Você é muito jovem ainda para ser programador meu pequenino")
elif idade<8:
    categoria = "Infantil A"
    imprimir(categoria)
elif idade<11:
    categoria = "Infantil B"
    imprimir(categoria)
elif idade<14:
    categoria = "Juvenil A"
    imprimir(categoria)  
elif idade<18:
    categoria = "Juvenil B"
    imprimir(categoria)  
else:
    categoria = "Adulto"
    imprimir(categoria)        
