alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
chaîneACrypter = input("S'il te plaît, entre un message à crypter :")
chaîneACrypter = chaîneACrypter.upper()
quantitéDécalage = int(input("S'il te plaît, entre un nombre entier de 1 à 25 en gise de clé."))
chaîneCryptée = ""
for caractèreActuel in chaîneACrypter:
    position = alphabet.find(caractèreActuel)
    nouvellePaosition = position + quantitéDécalage
    if caractèreActuel in alphabet:
        chaîneCryptée = chaîneCryptée + alphabet[nouvellePaosition]
    else:
        chaîneCryptée = chaîneCryptée + caractèreActuel
print("Ton message crypté est", chaîneCryptée)
