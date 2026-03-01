# Соответствие троек цифрам
code_to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOR": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

# Обратный словарь для вывода ответа
digit_to_code = {v: k for k, v in code_to_digit.items()}

import re

def solve():
    s = input().strip()
    
    # Находим оператор
    op = re.search(r'[\+\-\*]', s).group()
    # Делим строку на два операнда
    parts = s.split(op)
    
    def decode(word):
        res = ""
        # Идем по строке шагом в 3 символа
        for i in range(0, len(word), 3):
            res += code_to_digit[word[i:i+3]]
        return int(res)

    num1 = decode(parts[0])
    num2 = decode(parts[1])

    # Считаем результат
    if op == '+': result = num1 + num2
    elif op == '-': result = num1 - num2
    else: result = num1 * num2

    # Конвертируем обратно (учитываем минус, если он есть)
    res_str = str(result)
    ans = ""
    for char in res_str:
        if char == '-':
            ans += "-" # Обычно в таких задачах минус остается знаком
        else:
            ans += digit_to_code[char]
    
    print(ans)

# solve()