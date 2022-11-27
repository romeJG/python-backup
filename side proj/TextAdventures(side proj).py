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
    player_class=""
    #[0]wizard
    #[1]warrior
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
class main_game():
    class wizard_path():
        def cabin_intro():
            print("*you are now a wizard*")
            s = input("Pierce: no stay untill you completely heal")
            print("stay?")
            print("[Y] ok sure ill stay I still feel a bit dizzy")
            print("[N] No Ive been here for a while now")
            choice = input(">> ")
            if choice in yes:
                main_game.wizard_path.live_1_path()
            elif choice in no:
                main_game.wizard_path.die_1_path()
            else:   
                main_game.wizard_path.live_1_path()
        def live_1_path():
            s = input("Pierce: ok just lay down there")
            s = input("")

        def die_1_path():
            s = input("Pierce: oh no, ok just good luck out there...")

            

    class warrior_path():
        def cabin_intro():
            print("*you are now a warrior*")
            s = input("Pierce: no stay untill you completely heal")
            print("stay?")
            print("[Yes]Normal")
            print("[No]Hard")
            choice = input(">> ")


class new_char():
    def intro():
        wakeup = [f"YOU LAZY ASS MOFO wakeup {c_stats.player_name}", f"YOU wakeup {c_stats.player_name}", f"GOD DAMN IT wakeup{c_stats.player_name}", f"GOD DAMN IT FUCKING wakeup{c_stats.player_name}"]
        choice = "b"
        s = input(f"\nare you redy {c_stats.player_name}?.....")
        s = input("\nyes or no u have no choice haha :3")
        print("\nk here we go")
        s = input("One night You wokeup in a small cabin don't know what happend dizzy af dont know where or who you are........")
        print(f"\nwhile you were laying down pretending to sleep you heared a guy saying: hey {c_stats.player_name} wake up {c_stats.player_name} WAKEUP!.......")
        while choice == "b":
            print("[A]wakeup\n[B] keep sleeping")
            choice = input(">> ")
            if choice == "a":
                break
            else:
                print(wakeup[random.randint(0,3)])
        s = input("You:who are you?...")
        s = input("cabin owner: I'm Pierce your old friend you dont remember me?")
        s = input("Pierce: you have been in my cabin for 2 days now...")
        s = input("there was a warewolf that stuned you in the head when we was hunting in the woods...")

        s = input(f"{c_stats.player_name}: oh god im sorry Pierce is it?. I should headout but idk where and what the hell is happening and I assume that my name is {c_stats.player_name} right?")
        
        s = input(f"Pierce: Yes your name is {c_stats.player_name} and you are a......")
        choice=""
        while choice=="":
            print("\nchoose a class")
            print("[A] Wizard\n")
            print("[B] warrior")
            choice = input(">> ")
            if choice in answer_A:
                print(f"you are a wizard {c_stats.player_name}")
                main_game.wizard_path.cabin_intro()
            elif choice in answer_B:
                print(f"you are a warrior{c_stats.player_name}")
                main_game.wizard_path.cabin_intro()
            else:
                print(f"you are a warrior{c_stats.player_name}")
                main_game.wizard_path.cabin_intro()
        
    def char_create():
        print("\nok then")
        print("What is ur name stranger?")
        c_stats.player_name = input(">> ")
        s = input(f"\nhey {c_stats.player_name} WELCOME to Text Adventures ;D.... press enter to skip")
        new_char.intro()
    


def char_select():
    print("select your character orb")


def game_start():
    while __game_run__:
        choice=""
        print("\nHeyoo Have I seen you before??")
        choice = input(">> ")
        if choice in yes:
            char_select()
            break
        elif choice in no:
            new_char.char_create()
            break
            


if __name__ == '__main__':
    game_start()
    
        
