def bank(X, Y):
    for _ in range(Y):
        X += X * 0.10 
    return X

initial_deposit = float(input("Введите размер вклада в рублях: "))
years = int(input("Введите срок вклада в годах: "))

final_amount = bank(initial_deposit, years)
print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")