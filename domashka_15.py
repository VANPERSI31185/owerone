###################### 14.11 #########################

# Установите статичечкий атрибут
# мин цена в салоне красоты
# Допишите методы.
# Маникюр стоит на 20% больше
# Стрижка зависит от длины
# волос:
# меньше 30см - +20%,
# От 30 до 50 см - +50%
# Свыше 50 см - +80%

class Beauty_salon:

    minimum_price = 15

    def price_manicure(self):
        return f'Цена маникюра:{Beauty_salon.minimum_price * 1.2}'

    def price_a_haircut(self, hair_length):
        if hair_length < 30:
            return f'Цена стрижки:{Beauty_salon.minimum_price * 1.2}'
        elif 30 <= hair_length <= 50:
            return f'Цена стрижки:{Beauty_salon.minimum_price * 1.5}'
        else:
            return f'Цена стрижки:{Beauty_salon.minimum_price * 1.8}'

salon = Beauty_salon()
print(salon.price_manicure())
print(salon.price_a_haircut(24))