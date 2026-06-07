print("Добро пожаловать на пробную версию Fitlive")
user_name = input("Как вас зовут? ")
user_age = int(input("Ваш возраст? "))
user_weight = float(input("Ваш вес? "))
user_height = float(
    input("Ваш рост в метрах? (например, 1.75) ")
)
bmi = user_weight / (user_height ** 2)  # расчёт индекса массы тела
bmi = round(bmi, 1)  # округление индекса массы тела до 1
water_ml = user_weight * 30  # расчёт нормы воды в мл
water_l = water_ml / 1000  # перевод нормы воды из мл в литры
water_l = round(water_l, 1)  # округление нормы воды до 1
print()
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print()
print("Расчёт окончен. Будьте здоровы!")
