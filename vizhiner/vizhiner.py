import json


def vigenere_cipher(text, key, mode):
    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"
    len_of_alphabet = len(alphabet)
    text = text.lower().replace('ё', 'е').replace('й', 'и')
    key = key.lower().replace('ё', 'е').replace('й', 'и')
    key_length = len(key)
    key_as_int = [alphabet.index(i) for i in key]
    result = ""
    key_index = 0  # Индекс текущей буквы ключа
    for i in text:
        if i in alphabet:
            if mode == 'encrypt':
                value = (alphabet.index(i) + key_as_int[key_index % key_length]) % len_of_alphabet
            else:
                value = (alphabet.index(i) - key_as_int[key_index % key_length]) % len_of_alphabet
            result += alphabet[value]
            key_index += 1  # Переходим к следующему индексу ключа
        else:
            result += i  # Добавляем символ как есть, без шифрования
    return result


def process_data(json_data):
    output_data = {}
    for text, key in json_data.items():
        encrypted = vigenere_cipher(text, key, 'encrypt')
        decrypted = vigenere_cipher(encrypted, key, 'decrypt')
        output_data[text] = {
            'Key': key,
            'Encrypted': encrypted,
            'Decrypted': decrypted
        }
    return output_data


with open('words_to_crypt_or_encrypt.json', encoding='utf-8') as file:
    data = json.load(file)


output_data = process_data(data)


with open('result.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)

print("Output data saved to 'result.json'.")
