def total():

    fruit_prices = {
        'apple': 1.0,      
        'banana': 0.30,    
        'orange': 0.75,     
        'grape': 2.50,     
        'strawberry': 3.00,  
        'mango': 1.50       
    }
    total_bill = 0

    for fruit in fruit_prices:
        price_of_fruit = fruit_prices[fruit]
        how_many = int(input(f"How many ({fruit}) do you want to buy?: "))
        cost_of_this_fruit = price_of_fruit * how_many
        total_bill = total_bill + cost_of_this_fruit

    print(f"Your total is ${total_bill:.2f}")


if __name__ == '__main__':
    total()