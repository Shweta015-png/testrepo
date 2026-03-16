import random
import math

#Function to check if a number is prime or not

def is_prime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0 :
                return False
    return True

#Function to generate random prime numbers
def generate_prime(bits):  #bits is bit length (binary size)
    of prime number
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

#Function to gcd
def gcd(a,b):  # a=e (random) and b=phi value from generate_key_pairs this function
    while b:
        a, b=b , a%b  #this calculates a%b and assign (b=r)remainder to b and (a=b) b to a
    return a

#function to find modular multiplicative inverse
def mod_inverse(a,m):  #a=e & m=phi from generate_key_pairs this function
    m0, x0, x1=m, 0, 1
    while a>1:
        q=a // m
        m, a=a%m, m
        x0, x1=x1-q*x0, x0
    return x1+m0 if x1<0 else x1

#function to generate key pairs
def generate_key_pairs(bits):
    p=generate_prime(bits)
    q=generate_prime(bits)
    n=p*q
    phi=(p-1)*(q-1)

    while True:
        e=random.randint(2,phi-1)
        if gcd(e,phi)==1:
            break
    d=mod_inverse(e,phi)

    public_key = (n,e)
    private_key = (n,d)

    return public_key, private_key

#funciton to encryptia message
def encrypt(public_key, message):
    n, e = public_key
    cipher_text= [pow(ord(char),e,n) for char in message]  #convert each char to ASCII
    return cipher_text

#decryt

def decrypt(prvate_key,cipher_text):
    n,d = private_key
    decrypt_message =''.join([chr(pow(char,d,n)) for char in cipher_text])
    return decrypt_message

#main
if __name__=="__main__":
    bits=8
    public_key,private_key = generate_key_pairs(bits)
    print(f" Generate public key: {public_key} \n Generate private key:{private_key}")

    message = (input("Enter the message to be encrypted:"))    
    print("Original message:",message)

    encrypted_message = encrypt(public_key,message)
    print("Generate message:", encrypted_message)

    decrypted_message = decrypt(private_key,encrypted_message)
    print("Generate message:",decrypted_message)














    
        
