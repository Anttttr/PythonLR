Harry_Potter = ["A breeze ruffled the neat hedges of Privet DDDDDrive, ",
                ".which lay silent and tidy under the inky sky, ",
                "891347",
                "     the very last place yo34u would expect astonishing things to happen. ",
                "HHHHarry Potter rolled over inside his blankets without waking up."]

Faust = ["1",
         "..Ihr naht euch wieder, schwankende Gestalten, ",
         "Die fruh sich einst dem truben Blick gezeigt. ",
         "...Versuch ich wohl, euch diesmal festzuhalten? ",
         "     FFFFuhl ich mein Herz noch jen865em WWWWahn geneigt?"]

Le_Petit_Prince = [".Les hommes n'ont plus le t4566emps de rien connaitre. ",
                   "....IIIIIIIl achetent des choses toutes faites chez les marchands. ",
                   "     Mais comme il n'existe point de marchands d'amis, les hommes n'ontplus d'amis. ",
                   "Si tu v5436eux un ami, apprivoise-moi!",
                   "789123148798531"]

authors_and_works = {"Daniel Defoe": {"Robinson Crusoe": "1719*08*05", "A Journal of the Plague Year": 1722},
                     "Johann Wolfgang von Goethe": {"Faust": "1832", "Egmont": 1788},
                     "Ernest Miller Heminhway": {"The Old Man and the Sea": 1952, "For Whom the Bell Tolls": "1940 года"},
                     "Joanne Rowling": {"Harry Potter and the Philosopher's Stone": 1977},
                     "Antoine de Saint-Exupery": {"The Little Prince": "6 апреля 1949 год"}}

Harry_Potter_1 = ""
Faust_1 = ""
Le_Petit_Prince_1 = ""
new_author = ""


def get_author(value):  # здесь находим автора и год
    for k, v in authors_and_works.items():
        for k1, v1 in v.items():
            if value in k1:
                # перменная v1 это год, если нужно будет год засунуть в переменную, то там где new_author напиши year, new_author = далее без изменений
                print(v1)  # а в следующей строчке return v1, *строка без изменения*
                return k.split(" ")[0].upper()


for i in [Harry_Potter, Faust, Le_Petit_Prince]:  # передбираем все переменные
    j = 0
    newstr = []
    for string in i:  # перебираем каждую строку в переменной

        if string.isdigit():  # если эта строка из чисел, то ее пропускаем
            pass
        else:
            # если строка не из чисел то мы добавляем ее и убираем из ее начала точки
            new = string.lstrip(".")
            newstr.append(new)  # добавляем получившуюся строку
    for substr in range(len(newstr)):  # далее перебираем слова в обработанной строке
        new = newstr[substr].split(" ")  # разбиваем строку на слова
        for _ in range(len(new)):  # перебираем слова, убирая повторяющиеся заглавные
            try:  # нужно чтобы не выдвало ошибку если слово состоит из одной буквы
                # проверяем если два первых символа строки совпадают и они заглавные
                if new[_][0] == new[_][1] and new[_][0].isupper() and not new[_][0].isdigit():
                    symb = new[_][0]  # Запоминаем первую букву
                    # Формируем новую строку путем конкотенации первой буквы и срезанных букв, одинаковых с первой
                    new[_] = symb + new[_].lstrip(symb)

            except:
                pass
        newstr[substr] = " ".join(new)  # Склеиваем получившуюся строку
    if i == Harry_Potter:  # Тут формируем новые переменные путем склеивания строк из массива с обработанными строками
        Harry_Potter_1 = "".join(newstr)
        new_author = get_author("Harry_Potter")  # делаем переменную для автора
    elif i == Faust:
        Faust_1 = "".join(newstr)
        new_author = get_author("Faust")
    else:
        Le_Petit_Prince_1 = "".join(newstr)
        new_author = get_author("The Little Prince")
print(new_author)
