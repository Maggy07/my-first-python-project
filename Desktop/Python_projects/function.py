def print_account_details():
    account_number = input("Enter your account number: ")
    account_name = input("Enter your account name: ")
    otp = "123456"  # Simple static OTP for simplicity

    print(f"Account Number: {account_number}")
    print(f"Account Name: {account_name}")
    print(f"OTP: {otp}")
# Run the function
    print_account_details()


import random

def GenerateAccountNumber():
    phone = int(input('Enter your phone number :'))
    phone = str(phone)
    
    if len(phone) == 12:
        return f'your account number is  {phone[2:]}'
    
    return 'invalid phone number'




def generate_username():
    first_name = input('Enter your first name')
    last_name = input('Enter your last name')
    
    if first_name == '' or last_name == '':
        return 'invalid username'
    return first_name[:3] + last_name[-3]

def generate_otp(n):
    otp = ''
    for i in range(n):
        otp += str(random.choice(range(0,9)))
        x = '0'
        x = ''.join(otp)
    
    return otp
    
    
print(generate_otp(5))


def generate_password():
    password = input('Enter your password').capitalize
    num = range(10)
    for i in num:
        if password!= num[i]:
            return 'invalid'  
    if password == '':
        return 'invalid'
    if len(password)<9:
        return 'invalid'
    if password!= ascii:
        return 'invalid'
    
    return password


def login(username, password):
    username = input('Enter username')
    password = input('Enter password')
    
    if username == generate_username()and password == generate_password():
        return 'login'
    return 'invalid'



numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('*' * number)  # Prints '*' repeated 'number' times

#OR
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = " "
    for count in range (x_count):
        output += "x"
    print(output)

numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = " "
    for count in range (x_count):
        output += "x"
    print(output)


