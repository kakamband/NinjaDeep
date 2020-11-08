import random
import string

from ninjadeep.utils import admin_cmd

print("\033[1;32;40m By----->@DamnitZGuri ☆<----- \n")
# Rewriten For NinjaDeep By @Lovedeep_ViRk


@ninjadeep.on(admin_cmd(outgoing=True, pattern="pGen"))
@ninjadeep.on(sudo_cmd(outgoing=True, pattern="pGen", allow_sudo=False))
async def pass_Gen(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "Processing.....!")


def Pass_Gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    service_name = input("Enter Your Site or platform which you want to Generate\n")
    nlengh = int(input("Enter Your Pass Length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    await eor(event, "Your Pass Is Generating. . . .")

    random.shuffle(s)
    await ups.edit("Your Generated Pass Is\n")
    await ups.edit("".join(s[0:plen]))

    file = open("NinjaPass.txt", "w+")
    file.write(f"\n{service_name} pass is ---> ")
    file.write(f"".join(s[0:nlengh]))
    file.close()

    print eor(event, "Password has been saved in the file")


if __name__ == "__main__":
    Pass_Gen()
