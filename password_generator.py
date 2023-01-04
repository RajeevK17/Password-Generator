import random

def randomPassowrdGenerator():
    result = []

    lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

    uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    special_chars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '\\']

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    low_input = int(input('Enter no. of lower case characters: '))
    up_input = int(input('Enter no. of upper case characters: '))
    d_input = int(input('Enter no. of digits: '))
    schars_input = int(input('Enter no. of special characters: '))

    p = random.choices(lowercase_chars, k=low_input)
    q = random.choices(uppercase_chars, k=up_input)
    r = random.choices(digits, k=d_input)
    s = random.choices(special_chars, k=schars_input)

    for i in p:
        result += i

    for i in q:
        result += i

    for i in r:
        result += i

    for i in s:
        result += i

    random.shuffle(result)
    password = ''.join(result)

    print(f"\nYour randomly genereated password is --> {password}")
    print(f"Length : {len(password)} characters")

if __name__ == '__main__':
    try:
        randomPassowrdGenerator()

    except:
        print('Please check your input!')
