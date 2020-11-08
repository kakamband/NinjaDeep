print("\033[1;32;40m By----->@DamnitZGuri ☆<----- \n")
#Rewriten For NinjaDeep By @Lovedeep_ViRk


import asyncio
from ninjadeep.utils import admin_cmd
import string
import random


@ninjadeep.on(admin_cmd(outgoing=True, pattern="pGen"))
@ninjadeep.on(sudo_cmd(outgoing=True, pattern="pGen", allow_sudo=False))

async def _(event):
    if event.fwd_from:
        return
        
await (event, "Processing. . . .")

def Pass_Gen():
	s1 = string.ascii_uppercase
	s2 = string.ascii_lowercase
	s3 = string.digits
	s4 = string.punctuation
	
	service_name = input("Enter Your Site or platform which you want to Generate\n")
	plen = int(input("Enter Your Pass Length\n"))
	s = []
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))
	
	await (event, "Your Pass Is Generating. . . .")
	
	random.shuffle(s)
	print("Your Generated Pass Is\n")
	print("".join(s[0:plen]))
	
	file = open("pass.txt" , "a")
	file.write(f"\n{service_name} pass is ---> ") 
	file.write(f"".join(s[0:plen]))
	file.close()
	
	print(event,"Password has been saved in the file")

if __name__=="__main__":
	Pass_Gen()
