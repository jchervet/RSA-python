# This is my first python program!

# We want to make a program that will allow you to
# A. Enter something to encrypt w/ RSA
# B. Read from an encrypted file and decrypt w/RSA
import pickle


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


response = input("Hi, this program will encrypt/decrypt something for you using RSA encryption.\n"
                 "What would you like to do? Enter 1 for encryption or 2 for decryption.")

if response == '1':
    print("Okay, we'll encrypt.")

    # n = p * q where p and q are large primes.
    # e where gcd(e , phi(n) )=1
    # C = P^e mod n
    i = 0
    toEncrypt = input("Please enter a string that you would like to encrypt:\n")
    plainTxt = [0] * len(toEncrypt)
    cipherTxt = [0] * len(toEncrypt)

    print("hi")

    while i < len(toEncrypt):
        plainTxt[i] = ord(toEncrypt[i])
        i += 1

    print("hi")
    p = int(input("Please enter the first prime number that we will use for the encryption.\n"
                  "The larger the number is, the more secure the encryption will be.\n"
                  "This number MUST be prime!"))
    q = int(input("Please enter the second prime number that we will use for the encryption.\n"
                  "The larger the number is, the more secure the encryption will be.\n"
                  "This number MUST be prime!"))
    n = p * q

    e = int(input("Please enter a number e such that e and phi(n) are coprime.\n"))

    i = 0

    while i < len(toEncrypt):
        cipherTxt[i] = ((plainTxt[i]) ** e) % n
        # print >> 'RSA_data', cipherTxt[i]
        i += 1

    # file = open('RSA_data', 'wb')

    pickle.dump(str(cipherTxt), open('RSA_data', 'w'))

    print(cipherTxt)


    # file.write(cipherTxt)

elif response == '2':
    print("Okay, we'll decrypt.")
    # get e, n, p, q
    # find phi(n) = n-p-q+1
    # find f where e*f = 1 mod phi(n)
    # C^f = P mod n, just do P mod n after so 0 < P < n
    # convert P back to string and concatenate

    p = int(input("Please enter the private key 'p' needed to decrypt."))
    q = int(input("Please enter the private key 'q' needed to decrypt."))
    e = int(input("Please enter the public key 'e' that was used to encrypt."))
    n = p * q
    phi = n - p - q + 1

    f = modinv(e, phi)

    # file = open('RSA_data', 'rb')
    cipherTxt = pickle.load(open('RSA_data', 'r'))
    # ptext = ''.join(chr((int(line)**f)) for line in file)

    x = 0
    # ptext = "x" * len(cipherTxt)

    # while x < len(cipherTxt):
    ptext = ''.join(chr(cipherTxt[x] % n) for x in cipherTxt)

    print("Okay, your decrypted string is: \n")
    print(ptext)

    # do decryption
else:
    print("Sorry, that response was invalid.")
