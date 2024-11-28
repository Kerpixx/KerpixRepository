money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  #ме Траты за первый сяц
increase = 1.05  # Ежемесячный рост цен
month = 0
while money_capital >= 0:
    if month == 0:
        money_capital = money_capital + (salary - spend)
    else:
        spend *= increase
        money_capital = money_capital + (salary - spend)
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month - 1)
