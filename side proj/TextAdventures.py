import sys
import random

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes","YES","Yes","Yep","yep"]
no = ["N", "n", "no","NO","No","nope","Nope"]
run = ["run", "Run","RUN"]
fight = ["Fight","FIGHT","fight"]
#Global stuff

__game_run__=True
class c_stats():
    player_name=""
    player_money=0
    #cannot be lesthan 0
    player_power=1
    player_reputation=0
    player_level=0
    #player reputation titles 
    # evil > -151 && -500 (-151 to -500)
    # dishonest > -150 && -51 (-150 to-51)
    # lost > -50 && < -11(-50 to -11) 
    # neutral >-10 && < 10 (-10 to 10)
    # off-worlder >11 && < 50 (11 to 50)
    # trusted >51 && < 150 (51 to 150)
    # kin > 151 && < 500 (151 to 500)
class player_rep():
    
    def p_behevior(rep):
        if rep == 1:
            pass
        elif rep==2:
            pass
        elif rep==3:
            pass
        elif rep==4:
            pass
        elif rep==5:
            pass
        elif rep==6:
            pass
        elif rep==7:
            pass
        elif rep==8:
            pass
        elif rep==9:
            pass
        elif rep==10:
            pass
        elif rep==-1:
            pass
        elif rep==-2:
            pass
        elif rep==-3:
            pass
        elif rep==-4:
            pass
        elif rep==-5:
            pass
        else:
            pass

class new_char():
    def intro():
        wakup = [f"YOU LAZY ASS MOFO WAKUP {c_stats.player_name}", f"YOU WAKUP {c_stats.player_name}", f"GOD DAMN IT WAKUP{c_stats.player_name}", f"GOD DAMN IT FUCKING WAKUP{c_stats.player_name}"]
        choice = "b"
        s = input(f"are you redy {c_stats.player_name}?.....")
        s = input("yes or no u have no choice haha :3")
        print("k here we go")
        s = input("One night You wokeup in a small cabin don't know what happend dizzy af dont know where or who you are........")
        print(f"while you were laying down pretending to sleep you heared a guy saying: hey {c_stats.player_name} wake up {c_stats.player_name} WAKEUP!.......")
        while choice == "b":
            choice = input("[a]wakup\n[b] keep sleeping")
            if choice == "a":
                break
            else:
                print(wakup[random.randint(0,3)])
        s = input("you asked. who are you?")
        s = input("cabin owner: I'm Pierce your old friend you dont remember me?")
        s = input("Pierce: you have been in my cabin for 2 days now")
        s = input(f"{c_stats.player_name}: oh gosh im sorry Pierce is it? im sorry im really dizzy. I should headout but idk where and what the hell is happening and I assume that my name is {c_stats.player_name}")
        
    def char_create():
        print("ok then")
        print("What is ur name stranger?")
        c_stats.player_name= input(">> ")
        s = input(f"hey {c_stats.player_name} WELCOME to Text Adventures ;D.... press enter to skip")
        new_char.intro()
    


def char_select():
    print("select your character orb")


def game_start():
    while __game_run__:
        choice=""
        print("hi")        #run break
        print("Welcome...")
        print("Have u played the game before?")
        choice = input(">> ")
        print(choice)
        if choice in yes:
            char_select()
            break
        elif choice in no:
            new_char.char_create()
            break
            


if __name__ == '__main__':
    game_start()
        
