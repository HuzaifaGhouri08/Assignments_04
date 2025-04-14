def get_user_info():
    first_name: str = input("What's your first name?: ")
    last_name: str = input("What's your last name?: ")
    profession: str = input("What's your Profession?: ")
    age:int = input("what's your age?: ")
    email_address : str = input("What's your email address?: ")
    
    return first_name, last_name, age, profession, email_address

def main():
    user_data = get_user_info()
    print("User Data Received:", user_data)

if __name__ == "__main__":
     main()