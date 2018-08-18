n=input("Enter a String ")
if n.startswith('a') or n.startswith('e') or n.startswith('i')or n.startswith('o') or n.startswith('u'):
    print("The String Starts with Lower Case Vowel")
elif n.startswith('A') or n.startswith('E') or n.startswith('I') or n.startswith('O') or n.startswith('U'):
    print("The String Starts with Upper Case Vowel")
else:
    print("The entered string does not starts with vowel")
