salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


money_loss = 0 #потраченные на жильё деньги за вычетом зарплаты, станут недостающим money_capital
money_loss = spend - salary #первый месяц
for _ in range(months-1):
    spend = spend + increase * spend
    money_loss = money_loss + spend - salary
money_capital = int(round(money_loss, 0))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)