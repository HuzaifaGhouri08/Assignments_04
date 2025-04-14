def spaceship_countdown():
    for count in range(10, 0, -1):
        print(count, end=" ")
    print("Liftoff!")

if __name__ == "__main__":
    spaceship_countdown()