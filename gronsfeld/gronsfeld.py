import json

def gronsfeld_cipher(text, key, mode):
    alphabet = "абвгдежзиклмнопрстуфхцчшщъыьэюя "
    len_of_alphabet = len(alphabet)
    text = text.lower().replace('ё', 'е').replace('й', 'и')
    key_length = len(key)
    result = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            if mode == 'encrypt':
                value = (alphabet.index(text[i]) + int(key[i % key_length])) % len_of_alphabet
            else:
                value = (alphabet.index(text[i]) - int(key[i % key_length])) % len_of_alphabet
            result += alphabet[value]
        else:
            result += text[i]
    return result


with open('input_to_encrypt.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

results = {}


for text_to_encrypt, key in data.items():
    encrypted = gronsfeld_cipher(text_to_encrypt, key, 'encrypt')
    results[text_to_encrypt] = {'Encrypted': encrypted}


with open('output_encrypted.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

with open('input_to_decrypt.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

results = {}

for text_to_encrypt, key in data.items():
    decrypted = gronsfeld_cipher(text_to_encrypt, key, 'decrypt')
    results[text_to_encrypt] = {'Decrypted': decrypted}


with open('output_decrypted.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)
