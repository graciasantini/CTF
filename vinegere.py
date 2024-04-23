def encrypte(msg, key):
    # Filtrer le message pour ne garder que les lettres alphabétiques
    new_message = "".join([char for char in msg if char.isalpha()])

    # Répéter la clé jusqu'à ce qu'elle atteigne la même longueur que le message filtré
    while len(new_message) > len(key):
        key += key

    key = key[:len(new_message)]  # Ajuster la longueur de la clé

    crypt = ""
    posi = 0

    # Parcourir chaque caractère du message original
    for char in msg:
        if char.isalpha():
            # Calculer le décalage à partir de la clé pour déchiffrer le caractère
            key_shift = ord(key[posi % len(key)].lower()) - ord('a')
            # Calculer la position du caractère à déchiffrer
            pos = ord(char.lower()) - ord('a')
            # chiffrer le caractère en appliquant le décalage
            decrypted_char = chr(((pos + key_shift) % 26) + ord('a'))
            crypt += decrypted_char
            posi += 1
        else:
            # Conserver les caractères non alphabétiques tels quels dans le message chiffré
            crypt += char

    return crypt


def decrypted(msg, key):
    # Filtrer le message pour ne garder que les lettres alphabétiques
    new_message = "".join([char for char in msg if char.isalpha()])

    # Répéter la clé jusqu'à ce qu'elle atteigne la même longueur que le message filtré
    while len(new_message) > len(key):
        key += key

    key = key[:len(new_message)]  # Ajuster la longueur de la clé

    decrypt = ""
    posi = 0

    # Parcourir chaque caractère du message original
    for char in msg:
        if char.isalpha():
            # Calculer le décalage à partir de la clé pour déchiffrer le caractère
            key_shift = ord(key[posi % len(key)].lower()) - ord('a')
            # Calculer la position du caractère à déchiffrer
            pos = ord(char.lower()) - ord('a')
            # Déchiffrer le caractère en appliquant le décalage
            decrypted_char = chr(((pos - key_shift) % 26) + ord('a'))
            decrypt += decrypted_char
            posi += 1
        else:
            # Conserver les caractères non alphabétiques tels quels dans le message déchiffré
            decrypt += char

    return decrypt


message = """Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
"""
cle = "FCSC"

# Appeler la fonction pour déchiffrer le message avec la clé donnée
decrypted_message = decrypted(message, cle)
crypt_message = encrypte(decrypted_message, cle)

print(decrypted_message)

print(crypt_message == message.lower())
