list_A=["a","e","i","o","u"]
list_B=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
alpb=str(input("enter your string"))
if(alpb in list_A):
  print("Vowel")
elif(alpb in list_B):
  print("consonant")
else:
  print("invalid")
