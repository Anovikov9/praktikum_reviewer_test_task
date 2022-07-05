# не используется весь модуль datetime , достаточно вызвать from datetime import datetime, проще получать даты.
import datetime as dt

""" Нет комментариев к функциям в виде Docstrings, необходимо добавить!
начинаются с большой буквы, заканчиваются точкой и содержат описание того, что делает функция. """


class Record:
    # С целью улучшить читаемость кода, можно добавить типизацию, но такого нет в требованиях поэтому не обязательно.
    def __init__(self, amount, comment, date=''):
        # Имена приватных полей нужно начинать с нижнего подчеркивания: self._amount = amount, далее по коду похожее

        self.amount = amount
        # лучше инвертировать уловие и избавиться от not
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # Record имя класса и с заглавной буквы, итератор нужно с маленькой буквы.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # можно использовать двойное условие , без and и повторений  7 > (today - record.date).days >= 0                
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Вместо комментария для описания функции нужно использовать докстринг.
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # Имя переменной без смысловой нагрузки
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # При первом условии функция завершится , return можно без else
        else:
            # Нудно возвращать строку, а не tuple
            return('Хватит есть!')


class CashCalculator(Calculator):
    #  можно просто число.0 без float
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    # метод принимает лишние аргумеенты USD_RATE и EURO_RATE они находятся в зоне видимости класса, и аргументы должны быть с маленкой буквы, если нужно передавать.
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # лишняя переменная, можно использовать currency
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        # Всего 3 валюты, можно вместо elif использовать else
        elif currency_type == 'rub':
            # К чему используется сравнение без условия? Выше по коду используешь /=
            cash_remained == 1.00
            currency_type = 'руб'
        #  Не хватает отступа между разными условиями, сложно читается.
        if cash_remained > 0:
            # В f-строках применяется только подстановка переменных и нет логических или арифметических операций, вызовов функций и подобной динамики.
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        #  можно вместо elif использовать else
        elif cash_remained < 0:
            # Нужно соблюдать консистентность, выше по коду f-string.
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
# Убрать код, метод можно не переопределять, раз нет изменений.
    def get_week_stats(self):
        super().get_week_stats()
