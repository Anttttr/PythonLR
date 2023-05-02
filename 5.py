stream = "10dgffdfds100fvdgrh01yh16S57ugtv1768hutyrgg78uhgvgvf110A11yfdgrhy003H5greerJKfesghj80fdgdf678hgbtrfd1010yhfrgvrhbyjuyjthyjuhy0tjuyt01trdf35u0yjhyh1101F01V1rgfgthyyuh11yRhgtrf11jufgdsefvrtbht1"
notation = {'8': {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'},
            '16': {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
            }
count = 0  # количество заглавных
binary = ""  # текст с двоичным кодом
binary_transformed = ""  # текст с преобразованным
for i in stream:  # ищем заглавные и цифры 1 и 0
    try:  # пробуем перевести в число
        int(i)  # перевод
        if i == '1' or i == '0':  # если число 1 или 0 то добавляем в строку
            binary += i
    except:  # если перевод не получился
        if i.isupper():  # проверяем заглавная ли это буква
            count += 1
if count == 10:  # если заглавных 10
    # не сказано как переводить в 10, поэтому перевел так
    binary_transformed = str(int(binary, 2))
elif count == 8:  # если их 8
    for i in range(3-len(binary) % 3):  # добаляем вначало 0
        binary = '0'+binary  # добавляем
    convert = binary  # вводим промежуточную переменную
    while convert != '':  # далее дробим на срезы по 3 цифры и сравниваем
        srez = convert[-3:]  # дробим
        convert = convert[:-3]  # удаляем жти 3 цифры
        for k, v in notation['8'].items():  # берем из словаря значения триад
            if srez == k:  # сравниваем
                # записываем значение в преобразованную переменную
                binary_transformed = v + binary_transformed
elif count == 16:  # аналогично для 16, только вместо среза из 3 будет срез из 4
    for i in range(4-len(binary) % 4):
        binary = '0'+binary
    convert = binary
    while convert != '':
        srez = convert[-4:]
        convert = convert[:-4]
        for k, v in notation['16'].items():
            if srez == k:
                binary_transformed = v + binary_transformed

# выводим двоичный код, количество заглавных, результат перевода
print(binary, count, binary_transformed)
