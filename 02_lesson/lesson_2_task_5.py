month_to_season = int(input("Ведите номер месяца: "))
if 2>=month_to_season or 12<=month_to_season:
    print("Сейчас зима")
if 3<=month_to_season<=5:
    print("Сейчас Весна")
if 6<=month_to_season<=8:
    print("Сейчас Лето")
if 9<=month_to_season<=11:
    print("Сейчас осень")