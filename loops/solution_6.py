# WHILE LOOP - EXECUTE WHEN SOMETHING REMAING TRUE

food = input("Enter the food you like (q to quit): ")


while not  food == "q":
    if food.isdigit():
        print("Number is not allowed, type food")
        
    print(f"You like {food}")
    
    food = input("Enter the food you like (q to quit): ")

print("Thank you BYE")