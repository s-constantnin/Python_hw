is_year_leap = int(input("Ведите год: "))
text_1 = "true"
text_2 = "false"
if is_year_leap % 4 == 0:
    print("год:", is_year_leap,':', text_1)
else: print("год", is_year_leap,':', text_2)
