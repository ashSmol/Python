# перевод введеного количества секунд в чч:мм:сс

sec = int(input("Введите количество секунд: "))
hours = sec // 3600
sec -= hours * 3600
minutes = sec // 60
sec -= minutes * 60
print(f"вы ввели: {hours:02.0f}:{minutes:02.0f}:{sec:02.0f}")
