def month_to_season(number_of_month):
    
    number_of_month = int(input("Введите число:"))

    if number_of_month in [12, 1, 2]:

        return "Zima"
    
    if number_of_month in [3, 4, 5]:

        return "Vesna"
    
    if number_of_month in [6, 7, 8]:

        return "Leto"
    
    if number_of_month in [9, 10, 11]:

        return "Osen"
    
print (month_to_season("number_of_month"))




