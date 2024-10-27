salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен
money_capital = 0
month = 0

for _ in range(10):
    if month == 0:
        money_capital = money_capital + (spend - salary)
    else:
        spend *= increase
        money_capital = money_capital + (spend - salary)
    month += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
