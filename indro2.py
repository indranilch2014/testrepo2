#print("indroda is nice", end=' @gmail')
#print(4*"\n")
#print("Joy maa tara")
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-&^%$#@!><?/"
all = lower + upper + NUMBER + Symbol
length = 9
password = "".join(random.sample(all,length))
print(" The password you have generated is :",password)
