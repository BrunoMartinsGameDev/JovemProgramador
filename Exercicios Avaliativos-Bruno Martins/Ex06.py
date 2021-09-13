#6.O código a seguir está certo?Se não estiver,como você iria resolver e qual é o problema.
# i = 0
# while i < 10:
#   print(i)
#   if i == 7:
#       break
print("O código está errado, pois o problema nele é que ele entra num loop infinito ja que a variavel 'i' sempre será 0")
print("Para resolver eu simplesmente colocaria no final do while(abaixo do break e fora do if) o seguinte:'i+=1'")
print("Pois assim no final de cada execucução do while acrescentaria +1 ao valor da variavel i")
print("Assim quando chegasse em 7, o loop seria interrompido pelo 'break'")