# RSA implementation code in python
# a function to check whether a number is a prime number
def is_prime(num):
    v = 0  # a variable v to store counts of divisor of that number
    for i in range(2, num + 1):  # loop through all numbers less than p and see if there is more than one divisor
        if num % i == 0:
            v = v + 1  # count all those divisors
    if v > 1:  # if they are more than one than number is not a prime number
        return False
    else:
        return True


# function to check if greatest common divisor of e and q(n) is 1
def gcd(i, t):
    while i > 0:
        temp = i
        i = t % i
        t = temp
    return t


# function to calculate value of public key e
def calculate_e(q_n):
    e = 0
    for i in range(2, q_n + 1):
        if gcd(i, q_n) == 1:    # call function gcd to check if greatest common division btn e and q(n) is 1
            e = i
            break               # if is found break the loop
    return e


# function to calculate private key d using e*d mod q(n) == 1
def calculate_d(e, q_n):
    k = 1
    while True:         # loop until you get d and break the loop
        k = k + q_n
        if k % e == 0:
            d = k // e  # calculate d using integer division operator(//) to avoid decimal point
            break
    return d


# function to encrypt the plain text and return cipher text
def encrypt(e, n, plaintext):
    cipher = []  # allocation of empty list to store cipher text
    # Convert each letter in plaintext to numbers using built in function (ord) and encrypt using a^e mod n
    for char in plaintext:
        cipher.append(pow(ord(char), e) % n)  # append each cipher value in the empty list
    return cipher


# function to decrypt cipher text to plain text and return plain text
def decrypt(d, n, cipher_text):
    plain = []  # allocation of empty list to store plain text
    # Convert each value in cipher text using  a ^ d mod n
    for value in cipher_text:
        plain.append(pow(value, d) % n)  # append each value in an empty list
    return plain


# this is a function where execution will start
def start():
    print("..............Welcome to the RCA cryptography........")  # Welcome message
    while True:
        p = int(input("enter the value of prime number P: "))  # enter value of p and q
        q = int(input("enter the value of prime number Q: "))
        if not is_prime(p) or not is_prime(q):  # check whether p and q are prime numbers
            print("wrong input!, prime is number which is divisible by 1 and itself only!")
        else:
            break
    n = p * q  # calculate value of n
    q_n = (p - 1) * (q - 1)  # calculate value of Q(n)
    print(f"result of computing n = p*q = {n}")
    print(f"result of computing Q_n = {q_n}")

    e = calculate_e(q_n)  # call function to calculate public key e
    d = calculate_d(e, q_n)  # call function to calculate private key d

    print(f"RSA public key is (n = {n}, e = {e})")
    print(f"RSA private key is (n = {n}, d = {d})")

    message = input("Enter your message you need to encrypt: ")  # prompt user to enter message to be encrypted

    encrypted_msg = encrypt(e, n, message)  # call function to encrypt the message which return a cipher text and
    # store it in variable encrypted_msg
    print(f"Encrypted message is:")
    print(''.join(map(chr, encrypted_msg)))  # typecast each cipher number to a corresponding character for a better
    # view and join them to become a sentence
    print(f"Decrypted message is: {''.join(map(chr, decrypt(d, n, encrypted_msg)))}")  # call decrypt function and
    # print the plain text


start()  # call start function for the execution of whole program
