import json


def generate_matrix(key_word):
    alphabet = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
    key_word = key_word.lower().replace('ё', 'е').replace('й', 'и').replace('ь', 'ъ')

    # Отобразить ключевое слово без дубликатов
    key_word = "".join(sorted(set(key_word), key=key_word.index))

    # Создание списка алфавита без символов, которые уже в ключевом слове
    for char in key_word:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")

    # Комбинирование ключевого слова и оставшегося алфавита
    combined = key_word + alphabet

    # Убедитесь, что combined делится нацело на 6
    while len(combined) % 6 != 0:
        combined += ' '

    # Создание матрицы
    matrix = [list(combined[i:i+6]) for i in range(0, len(combined), 6)]
    return matrix


def playfair_cipher(text, key_word, mode):
    matrix = generate_matrix(key_word)
    text = text.lower().replace('ё', 'е').replace('й', 'и').replace('ь', 'ъ')

    # Добавьте "x", если длина текста нечетна
    if len(text) % 2 != 0:
        text += 'x'

    result = ""

    if mode == 'decrypt':
        for i in range(0, len(text)-1, 2):
            pair = text[i:i+2]
            row1 = row2 = col1 = col2 = None
            for row in matrix:
                if pair[0] in row:
                    row1 = matrix.index(row)
                    col1 = row.index(pair[0])
                if pair[1] in row:
                    row2 = matrix.index(row)
                    col2 = row.index(pair[1])

            if row1 is not None and row2 is not None:
                if row1 == row2:
                    result += matrix[row1][(col1-1)%len(matrix[0])]
                    result += matrix[row2][(col2-1)%len(matrix[0])]
                else:
                    result += matrix[row1][col2]
                    result += matrix[row2][col1]
    else:
        for i in range(0, len(text)-1, 2):
            pair = text[i:i+2]
            row1 = row2 = col1 = col2 = None
            for row in matrix:
                if pair[0] in row:
                    row1 = matrix.index(row)
                    col1 = row.index(pair[0])
                if pair[1] in row:
                    row2 = matrix.index(row)
                    col2 = row.index(pair[1])

            if row1 is not None and row2 is not None:
                if row1 == row2:
                    result += matrix[row1][(col1+1)%len(matrix[0])]
                    result += matrix[row2][(col2+1)%len(matrix[0])]
                else:
                    result += matrix[row1][col2]
                    result += matrix[row2][col1]
    return result



with open('input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

results = {}

for key in data:
    decrypted = playfair_cipher(key, data[key], 'decrypt')
    results[key] = {"Decrypted": decrypted}


with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)
