#3--Take a character from the user and check if it is a vowel or consonant.
vowels=["a","i","o","e","u"]
character=input("Enter the character")
for i in (vowels):
    if character==i:
        print("Character is Vowel")
        break
else:
    print("Character is consonant")

vowels=["a","i","o","e","u"]
character=input("Enter the character")
if character.lower() in vowels:
    print("Vowel")
else:
    print("consonant")