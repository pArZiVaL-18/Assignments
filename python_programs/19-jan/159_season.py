def print_season(month):
    if month in [6, 7, 8, 9]:
        print("Spring")
    elif month in [3, 4, 5]:
        print("Summer")
    else:
        print("Winter")


print(print_season(8))