WATER_PER_KG = 30
ML_IN_LITER = 1000

print('Добро пожаловать на пробную версию Fitlive')

while True:
    user_name = input('Как вас зовут? ').strip()
    if user_name:
        break
    print('Имя не может быть пустым.')

while True:
    user_age = input('Ваш возраст? ').strip()
    if user_age.isdigit():
        user_age = int(user_age)
        break
    print('Введите возраст целым числом.')

while True:
    user_weight = input('Ваш вес? ').strip()
    try:
        user_weight = float(user_weight)
        if user_weight > 0:
            break
    except ValueError:
        pass
    print('Введите корректный вес.')

while True:
    user_height = input(
        'Ваш рост в метрах? (например, 1.75) '
    ).strip()
    try:
        user_height = float(user_height)
        if user_height > 0:
            break
    except ValueError:
        pass
    print('Введите корректный рост.')

bmi = round(user_weight / (user_height ** 2), 1)

water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_IN_LITER, 1)

if bmi < 18.5:
    bmi_status = 'Недостаточная масса тела'
elif bmi < 25:
    bmi_status = 'Нормальная масса тела'
elif bmi < 30:
    bmi_status = 'Избыточная масса тела'
else:
    bmi_status = 'Ожирение'

print()
print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Категория: {bmi_status}')
print(f'Рекомендуемая норма воды: {water_l} л в день')
print()
print('Расчёт окончен. Будьте здоровы!')