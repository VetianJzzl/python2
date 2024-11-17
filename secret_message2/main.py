def even_odd_swap(x):
    if (len(x)%2 != 0) :
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

letters = 'abcdefghijklmnopqrstuvwxyz'
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
msg = 'python'
secret_code = ''

# 10 random letters 
for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]    

encoder = random.randint(0, 3)
encoder = 0
if encoder == 0:
    msg_enc = msg
elif encoder == 1:
    msg_enc = even_odd_swap(msg)
elif encoder == 2:
    msg_enc = reverse(msg)
else:
    msg_enc = swap_middle(msg)

msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
print()
print('I am hearing ...')
print(msg_enemy)
print()

for kk in range(1, 26):
    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_ms = swap_middle(msg_dec)
   
    #print(msg_dec, msg_dec_eo, msg_dec_r, msg_dec_ms)
    if msg_dec[0:6:1]=='python':
        print('code cracked ...')
       # print('kk is equal to ...', kk)
        print('Secret code is ...')
        print(msg_dec[6::1])
        break
    elif msg_dec_eo[0:6:1]=='python':
        print('code cracked ...')
       # print('kk is equal to ...', kk)
        print('Secret code is ...')
        print(msg_dec_eo[6::1])
        break
    elif msg_dec_r[0:6:1]=='python':
        print('code cracked ...')
       # print('kk is equal to ...', kk)
        print('Secret code is ...')
        print(msg_dec_r[6::1])
        break
    elif msg_dec_ms[0:6:1]=='python':
        print('code cracked ...')
       # print('kk is equal to ...', kk)
        print('Secret code is ...')
        print(msg_dec_ms[6::1])
        break  

def check_palindrome(x):
    ans = str(x) == reverse(x)
    return ans

z = ""


print('The Story begins during the battle of Beligum. Our hero is a German Platoon leader battling the French and British in the very north of france.\n')
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
    
    print("Soldier: Sir! We have just received a message from SCHÜTZENKOMPANIE! It says \n" input)
    print("General: Alright, I want you to send the Bismark and her Company for the Big guns and send 40 Luftwaffe planes for support! \n")
    print("Congrautlations! You have completed the Mission by sucesslfully getting a message to command. Your troops have been saved! \n")


# print()