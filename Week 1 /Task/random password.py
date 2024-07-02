import random
import string
import argparse
 
def ran_pass(length, upper, lower, Digits, special):
    char=""
    if upper:
        char+=string.ascii_uppercase
        
    if lower:
        char+=string.ascii_lowercase
        
    if Digits:
        char+=string.digits
    if special:
        char+=string.punctuation
        
    password="".join(random.choice(char) for _ in range(length))
    return password
parser=argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')   
parser.add_argument('-lo', '--lowercase', action='store_true', help='Include lowercase letters')
parser.add_argument('-d', '--Digits', action='store_true', help='Include digits')
parser.add_argument('-s', '--special', action='store_true', help='Include special characters')   
args=parser.parse_args()
password_genarator=ran_pass(args.length, args.uppercase, args.lowercase,args.Digits, args.special)
print(f"RANDOM PASSWORD GENARATOR: {password_genarator}")
  