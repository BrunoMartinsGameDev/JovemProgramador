#5.Considere o código abaixo e responda as questões:
# if (b1 == True):
#   c1 = True
# else:
#   if (b2 == True):
#       if (b3 == True):
#           c2 = True
#       else:
#           c3 = True
#       c4 = True
# c5 = True
# a.Se b1=V,b2=V e b3=F,quais comandos serão executados pelo algoritmo?
# b.Se b1 = F, b2 = V e b3 = F, quais comandos serão executados?
# c.Se b1 = F, b2 = V e b3 = V, quais comandos serão executados?
#d.Quais valores lógicos b1,b2 e b3 devem receber para que somente o comando C5 seja executado?
print("Resposta A: c1 sera true e c5 tambem, c2,c3 e c4 serão false")
print("Resposta B: c1 sera false,c2 sera false,c3 sera true, c4 sera true e c5 sera true")
print("Resposta C: c1 sera false, c2 sera true, c3 sera false, c4 sera true e c5 sera true")
print("Resposta D: b1 = false, b2 = false, b3 tanto faz, ja q b2 é false nunca irá verificar o b3")