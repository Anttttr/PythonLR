import pandas as pd
menu = {"Bacon Wrapped Pork Tenderloin": {"bacon": 250, "pork": "50o", "olive oil": 70, "honey": 100},
        "Chicken & Veggie Stir-Fry": {"chicken": 455, "broccoli": 455, "mushrooms": "225", "olive oil": 88},
        "Butter Chicken": {"chicken": 910, "butter": 110, "onion": 225, "garlic": 20, "tomato": 395},
        "Pesto Chicken Bake": {"chicken": "95i", "basil pesto": 130, "tomato": 155, "cheese": 150},
        "Lemon Garlic Salmon & Asparagus": {"salmon": 600, "asparagus": "20u", "butter": 50, "olive oil": 100, "garlic": 35, "lemon": "80"},
        "Roasted Veggie and Black Bean Tacos": {"tomato": "1u0", "corn": 450, "onion": 150, "bell pepper": 300, "olive oil": 20, "beans": "100", "lemon": "9a"},
        "Stuffed Bell Pepper Boats": {"bell pepper": 350, "chicken": 500, "salsa": 50, "cheese": 100}}

products = {"asparagus": [4000, "2022-11-27", 21, "4$"],
            "bacon": [4500, "2022-11-28", 14, '10$'],
            "basil pesto": [3000, "2022-10-30", 80, "3$"],
            "beans": [3000, "2022-11-25", 31, "1.5$"],
            "bell pepper": [9000, "2022-12-02", 7, "4$"],
            "broccoli": [7000, "2022-10-20", 50, '4$'],
            "butter": [3500, "2022-11-30", 20, "3$"],
            "cheese": [4830, "2022-11-22", 30, "6$"],
            "chicken": [40000, "2022-11-25", 10, '10$'],
            "corn": [9000, "2022-11-04", 70, "6$"],
            "garlic": [2000, "2022-10-29", 60, "4$"],
            "honey": [5000, "2022-08-10", 120, '4$'],
            "lemon": [3500, "2022-11-19", 22, "2$"],
            "mushrooms": [4000, "2022-12-01", 60, '7$'],
            "olive oil": [5000, "2022-11-04", 60, '8$'],
            "onion": [5425, "2022-10-29", 50, "2$"],
            "pork": [9500, "2022-11-30", 8,  '15$'],
            "salmon": [13000, "2022-11-30", 11, "20$"],
            "salsa": [500, "2022-11-04", 40, '5$'],
            "tomato": [10000, "2022-11-27", 13, "2$"]}

sales = {"Bacon Wrapped Pork Tenderloin": 16, "Chicken & Veggie Stir-Fry": 15, "Butter Chicken": 11, "Pesto Chicken Bake": 18,
         "Lemon Garlic Salmon & Asparagus": 20, "Roasted Veggie and Black Bean Tacos": 19, "Stuffed Bell Pepper Boats": 8}
date = "2022-12-03"
purchase = {}  # необходимый список закупки
df = pd.DataFrame(data=products)  # формируем датасет из продуктов
for k, v in menu.items():  # проходимся по меню, чтобы исправить буквы на 0 и строки на числа
    for k1, v1 in v.items():
        if type(v1) == str:  # проверяем если значение это строка
            for i in range(len(v1)):  # проходимся по каждому символу
                try:  # пробуем
                    int(v1[i])  # преобразовать в число
                except:  # если получем ошибку
                    v1 = v1[:i] + '0' + v1[i+1:]  # заменяем символ на 0
            v[k1] = int(v1)  # преобразовываем строку в число
df1 = df.copy()  # копируем датасет продуктов для более простого пожсчета
# прибавляем к текущей дате 7 дней
date = pd.to_datetime(date) + pd.DateOffset(days=7)
for k, v in menu.items():  # дальше проходимся по меню
    count = sales.get(k)  # находим количество продаж
    for k1, v1 in v.items():  # для каждого продукта находим остаток
        df1[k1][0] -= count*v1  # вычисляем остаток

for k, v in products.items():  # проходимся по продуктам
    # преобразовываем срок годности из строки в дату
    df1[k][1] = pd.to_datetime(df1[k][1])
    # прибавляем к дате их срок хранения
    df1[k][1] += pd.DateOffset(days=df[k][2])
    if (df1[k][1]-date).days <= 0:  # если срок хранения выйдет на след неделе
        df1[k][0] = 0  # то выбрасывваем все продукты
    # находим количество товара, которое нужно закупить
    delta = df[k][0]-df1[k][0]
    # преобразовываем цену за 100 грамм, убираем знак $
    price = float(df[k][3][:-1])
    if delta >= 0:  # если разница больше или 0, т.е продукт тратили
        # добавляем продукт в словарь
        purchase[k] = [delta, str(round(delta*price/100, 2))+'$']
print(purchase)  # выводим словарь
