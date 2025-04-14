def num_in_stock(fruit):
    fruit = fruit.lower()

    if fruit == 'apple':
        return 200
    elif fruit == 'mango':
        return 300
    elif fruit == 'banana':
        return 500
    elif fruit == 'pear':
        return 1000
    else:
        return 0

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == '__main__':
    main()