

#############################################################################################################################
import random
letters='abcdefghijklmnopqrstuvwxyz'

def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    
    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    
    s = ''
    s = s + second_half 
    s = s + first_half
    return s
    
def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

def vigenere_cipher(msg, key):   
    s=''
    for i in range(len(msg)):
        if msg[i] == ' ':
            s = s + ' '
        else:
            idx = int(letters.find(msg[i]))
            rem = i % len(key)
            new_idx = (idx+key[rem])%26
            s = s + letters[new_idx]
    return s 

def encoding(amsg, encoder):
    # encoder = 0
    if encoder == 0:
        msg_enc = amsg
    elif encoder == 1:
        msg_enc = even_odd_swap(amsg)
    elif encoder == 2:
        msg_enc = reverse(amsg)
    else:
        msg_enc = swap_middle(amsg)

    return msg_enc


def test():
    amsg = 'python'
    secret_code = ''

 
    for kk in range(10):
        n = random.randint(0, 25)
        secret_code = secret_code + letters[n]

    amsg = amsg + secret_code
    print("msg: ", amsg)

    encoder = random.randint(0, 3)
    # encoder = 0
    if encoder == 0:
        msg_enc = amsg
    elif encoder == 1:
        msg_enc = even_odd_swap(amsg)
    elif encoder == 2:
        msg_enc = reverse(amsg)
    else:
        msg_enc = swap_middle(amsg)

    msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
    print("enemy msg: ", msg_enemy)

    for kk in range(1, 26):
        msg_dec = caesar_cipher(msg_enemy, kk)
        msg_dec_eo = even_odd_swap(msg_dec)
        msg_dec_r  = reverse(msg_dec)
        msg_dec_ms = swap_middle(msg_dec)
    
        
        if msg_dec[0:6:1]=='python':
            print('code cracked : caeser...')

            print('Secret code is ...')
            print(msg_dec[6::1])
            break
        elif msg_dec_eo[0:6:1]=='python':
            print('code cracked caeser + even_odd...')
        
            print('Secret code is ...')
            print(msg_dec_eo[6::1])
            break
        elif msg_dec_r[0:6:1]=='python':
            print('code cracked caeser + even_odd + reverse...')
        
            print('Secret code is ...')
            print(msg_dec_r[6::1])
            break
        elif msg_dec_ms[0:6:1]=='python':
            print('code cracked caeser + even_odd + reverse + swap...')
        
            print('Secret code is ...')
            print(msg_dec_ms[6::1])
            break

print("======================================")
print("Simple Test")
test()

       

print("======================================")
print("Well, well, well. Look whos back!\n")
print("Tired of being a German Commander? Well, you are in the right place!\n")
print("You are now a British Intelligence officer whos job it is to encrypt messages.\n")
print("You and your team believe you have come up with 2 secret codes that will help us defeat the Germans.\n")
print("But to test that, we will try to endcrypt and decrypt some messages.\n")

msg= str(input("Type message: "))
print("======================================")
print("now you must decide which encrpition method you would like to use.\n")
y = str(input("Either: 1. Ceaser Cipher or 2. Vigenere Cipher "))
print("======================================")


if y == '1':
    encoder = random.randint(0, 3)
    msg_enc = encoding(msg, encoder)
    n = random.randint(1, 25)
    coded = caesar_cipher(msg_enc, n)
    z = 'Ceaser Cipher'
    print("Using th secret code:,", z, " you get:")
    print(coded)
    print("======================================")

elif y == '2':
    encoder = random.randint(0, 3)
    msg_enc = encoding(msg, encoder)
    print(msg_enc)
    key = [1,2,3,4,5]
    coded = vigenere_cipher(msg_enc, key)

    z = 'Vigenere Cipher'
    print("Using th secret code:,", z, " you get:")
    print(coded)
    print("======================================")

print("Nice Work! Now we must decrypt the message in an easy and time efficient way.\n")
print("Luckly for you, the team created decrpition methods for each of the secret codes.\n")

print("Since you Used:", z, "We have used the decryption method and got:")

# Decryption
if y == '1':
    msg_dec = caesar_cipher(coded, n)
    if encoder == 0:
        msg_dec = even_odd_swap(msg_dec)
    elif encoder == 1:
        msg_dec = even_odd_swap(msg_dec)
    elif encoder == 2:
        msg_dec  = reverse(msg_dec)
    else:
        msg_dec = swap_middle(msg_dec)
    
    print("======================================")
    print("DECODING")
    print(msg_dec)


elif y == '2':
    new_key = [26-1, 26-2, 26-3, 26-4, 26-5]
    msg_dec = vigenere_cipher(coded, new_key)
    print(coded)
    print(msg_dec)
    print("encoder: ", encoder)
    if encoder == 0:
        msg_dec = even_odd_swap(msg_dec)
    elif encoder == 1:
        msg_dec = even_odd_swap(msg_dec)
    elif encoder == 2:
        msg_dec  = reverse(msg_dec)
    else:
        msg_dec = swap_middle(msg_dec)
    
    print("======================================")
    print("DECODING")
    print(msg_dec)
else :
    print('error') 


def check_palindrome(x):
    ans = str(x) == reverse(x)
    return ans

z = ""


"""print('The Story begins during the battle of Beligum. Our hero is a German Platoon leader battling the French and British in the very north of france.\n')
print("Soldier: Sir! the enemy is pinning our units down with heavy artillery and motars. We can't get to the enemy base without taking heavy losses!\n")
print("You: I belive I have an idea! How far are we from the coast?\n")
print("Soldier: -Consults Map- I believe we are only 5 miles away from the nearest coast, sir!\n")
print("You: Excellent! I shall send a message to the High Command and ask them to send planes and the Kriegsmarine for some Battleships to bombard the enemy base! Have our men stand down and take cover in the meantime. Keep them ready to attack at any moment!\n")
print('Soldier: Yes Sir!\n')

print('You: -picks up Enigma (a machine used by the Germans to encript and decript messages) to type message-')


x= input("Type message: ")
if check_palindrome(x):
    print("Contragulations, you have made your Message a Palindrome! You have earned the title of Palindrome Master! This was a secret Easter Egg added to the game")
else:
    print(x)
    print('\n Now you must decide which encrpition method you would like to use. \n')
    print("1. Even/Odd Swap")
    print("2. Reverse")
    print("3. Reverse Word")
    print("4. Swap Middle")
    print("5. Swap Middle Reverse")
    y = input("Type the number of the method you would like to use: ")
    if y == '1':
        x_even_odd = even_odd_swap(x)
        print(x_even_odd)
        
    elif y == '2':
        x_reverse = reverse(x)
        print(x_reverse)    
        x_rev = reverse(x)
        print(x_rev)
        z = x_rev
    elif y == '3':  
        x_rev_word = reverse_word(x)
        print(x_rev_word)
        z = x_rev_word
    elif y == '4':
        x_swap_mid = swap_middle(x)
        print(x_swap_mid)
        z = x_swap_mid
    else:   
        x_swap_mid_rev = swap_mid_rev(x)
        print(x_swap_mid_rev)
        z = x_swap_mid_rev
    
    print("decoded method")
    print(z)
    
    
    
    
    print('=============')
    print("Later, At the German Military Base... \n")
    print(" The Radio Operater get a message..." )
    print(z)
    print("-The Radio Operater puts the message into the Enigma Machine to decode it...-")
    print()
    if y == '1':
        encode = even_odd_swap(x)
        decode = even_odd_swap(encode)
        print('=============')
        print("Encoded:", encode)
        print("Decoded:", decode)
        print('=============')
    
    elif y == '2':
        encode = reverse(x)   
        decode = reverse(encode)
        print('=============')
        print("Encoded:", encode)
        print("Decoded:", decode)
        print('=============')
    elif y == '3':  
        encode =  reverse_word(x)
        decode = reverse_word(encode)
        print('=============')
        print("Encoded:", encode)
        print("Decoded:", decode)
        print('=============')
    elif y == '4':
        encode =  swap_middle(x)
        decode = swap_middle(encode)
        print('=============')
        print("Encoded:", encode)
        print("Decoded:", decode)
        print('=============')
    else:   
        encode = swap_mid_rev(x)
        decode = swap_mid_rev(encode)
        print('=============')
        print("Encoded:", encode)
        print("Decoded:", decode)
        print('=============')
    
    print("Soldier: Sir! We have just received a message from SCHÜTZENKOMPANIE! It says \n", x)
    print("General: Alright, I want you to send the Bismark and her Company for the Big guns and send 40 Luftwaffe planes for support! \n")
    print("Congrautlations! You have completed the Mission by sucesslfully getting a message to command. Your troops have been saved! \n")"""