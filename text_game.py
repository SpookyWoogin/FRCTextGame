#Text game by Colin Gideon
#The FIRST Robotics Competition and Infinite Recharge are trademarks of FIRST

import random
import time

#Backup method for Linux or MacOS users where msvcrt doesn't exist
try:
    from msvcrt import getch
    def keypress():
        return getch()
except ModuleNotFoundError:
    def keypress():
        key = input()
        if key == "":
            return b'\r'
        else:
            return key.encode()

match_time = 150

class matchtimer():
    #Class that controls the match timer throughout the program
    def auto(self):
        global match_time
        match_time -= 15
    def intake(self):
        global match_time
        if match_time >= 10:
            match_time -= random.randint(3,10)
        else:
            match_time -= random.randint(match_time-2,match_time)
    def lowgoal(self):
        global match_time
        if match_time >= 7:
            match_time -= random.randint(3,7)
        else:
            match_time -= random.randint(match_time-2,match_time)
    def highgoal(self):
        global match_time
        if match_time >= 15:
            match_time -= random.randint(5,15)
        else:
            match_time -= random.randint(match_time-2,match_time)
    def inner(self):
        global match_time
        if match_time >= 17:
            match_time -= random.randint(7,17)
        else:
            match_time -= random.randint(match_time-2,match_time)
    def cwheel(self):
        global match_time
        if match_time >= 10:
            match_time -= random.rantint(5,10)
        else:
            match_time -= random.randint(match_time-2,match_time)
    def end(self):
        global match_time
        if match_time >= 5:    
            match_time -= (5,match_time)
            fail_flag = False
        else:
            fail_flag =True
matchtimer = matchtimer()

#Hella variables
red_alliance_score = 0
blue_alliance_score = 0
low_goal = 1
high_goal = 2
inner_goal = 3
rotation_control = 10
position_control = 20
end_hang = 25
end_park = 5
end_level = 15
stage1 = 9
stage2and3 = 20
pen_auto_sector = 3
pen_alliance_zones = 15
pen_pin = 3
pen_damage = 15
begin_cells = 3
robot_cells = 0
robot_cells_max = 5
powercount = 0

print("""Hello and welcome to the 2020 FIRST Robotics Competition!
This years game: INFINITE POSTPONEMENT-er...RECHARGE!
press ENTER to begin or Q to Quit""")

#char_catch has to be redefined before every if check since getch() behaves like input()
char_catch = keypress()
if b'\r' in char_catch:
    #Excruciating Pain via Text Wall
    print("""Infinite Recharge is played by 2 alliances of 3 robots each.
    Scoring is done when a robot from either alliance puts a yellow POWER CELL into their alliances POWER PORT
    The POWER PORT has 3 goals:
        A low goal easily completable by any robot with a low chance of missing a majority of the shots made (2 Points during Auto, 1 during Teleop)
        A high goal that requires a robot to aim to the port to score, with a moderate risk of missing (4 Points during Auto, 2 during Teleop)
        A inner port inside of the high goal with a high risk of missing but low chance of missing the high goal (6 Points during Auto, 3 during Teleop)
    The game plays out in a 2:30 timed period where the first 15 are taken by the auto period. During this period you can't make contact with the opposing alliances
    robots or enter the opposing alliances sector. (Penalty of 3 points given to the opposing alliance)
    During the Teleop period, you can defend against other robots to prevent them from scoring. HOWEVER, you can\'t:
        Enter the opposing alliances zones marked out around their TRENCH RUN, LOADING ZONE, and POWER PORT
        (Penalty of 15 points given to the opposing alliance IF contact is made with a opposing robot in this zone)
        Pin for longer than 5 seconds (Penalty of 3 Points given to the opposing alliance)
        You can\'t damage other robots (Penalty of 15 Points given to the opposing alliance and a YELLOW CARD given against you
    There's 3 stages of play during the game
        The first stage is completed when a alliance scores 9 power cells
        The second stage is completed when a alliance scores 20 more power cells and ROTATION CONTROL is completed (10 Points to corrosponding Alliance)
        The third stage is completed when a alliance scores 20 more power and POSITION CONTROL is completed (20 Points to corrosponding Alliance)
        (The option to spin the CONTROL PANEL will show up when ROTATION & POSITION CONTROL is activated and will dissapear after it's been completed)
    FINALLY, in the last 30 seconds of the game, you're able to score by climbing the SHIELD GENERATOR SWITCH
        For each robot hung, the corrosponding alliance scores 25 points
        For each robot parked, the corrosponding alliance scores 5 points
        If the switch is level, the corrosponding alliance scores 15 points
        
        -=- END OF TEXT WALL -=-""")
    #time.sleep(10)

    while True:
        #1 = Blue Alliance
        #2 = Red Alliance
        alliance = random.randint(1,2)
        if alliance == 1:
            user_alliance = "Blue Alliance"
            comp_alliance = "Red Alliance"
        else:
            comp_alliance = "Blue Alliance"
            user_alliance = "Red Alliance"
        print(f"""For the match you are on the {user_alliance}
You will be playing against the computer on the {comp_alliance}""")
        print("Would you like to begin? Press Enter to Continue or Q to Quit")
        char_catch = keypress()
        if b'\r' in char_catch:
            #Start of game
            print("Drivers behind the lines in...")
            countdown = 3
            for x in range(countdown):
                print(f"{countdown}!")
                countdown -= 1
                time.sleep(1)
            print("GO!")
            auto_message_mod = ""
            if random.randint(1,20) == 6:
                if random.randint(1,2) == 2:
                    blue_alliance_score += pen_auto_sector
                    auto_message_mod = "However, your robot entered the opposing alliances sector and incurred a foul! The opposing alliance gained 3 of their points from it!"
                else:
                    red_alliance_score += pen_auto_sector
                    auto_message_mod = "However, the opposing robot entered your alliances sector and incurred a foul! Your alliance gained 3 of your points from it!"
            blue_alliance_score += random.randint(1,12) * (high_goal * 2)
            red_alliance_score += random.randint(1,12) * (high_goal * 2)
            matchtimer.auto()
            print(f"During the auto period, the blue alliance scored {blue_alliance_score}, and the red alliance scored {red_alliance_score}. {auto_message_mod}")
            time.sleep(3)

            wheelstage = 0
            while True:
                colorwheel = "6) Color wheel Unavailable"
                climb = "7) Climb Unavailable"
                while wheelstage == 0:
                    if powercount >= 29:
                        colorwheel = "6) Spin the color wheel"
                    break
                while wheelstage == 1:
                    if powercount >= 49:
                        colorwheel = "6) Spin the color wheel"
                    break
                if match_time <= 30:
                    climb = "7) Climb!!!"

                print(f"""
            MATCH SCORE:
Blue Alliance: {blue_alliance_score} Red Alliance: {red_alliance_score}
            MATCH TIME: {match_time}""")
                print(f"""Power Cells currently in robot: {robot_cells}
What would you like to do?
1) Collect Power Cells
2) Go for the low goal
3) Go for the high goal
4) Go for the inner port
5) Play Defense
{colorwheel}
{climb}
Q) Quit""")
                char_catch = keypress()
                if b'1' in char_catch:
                    powercollect = random.randint(0,5)
                    if powercollect != 0:
                        if powercollect + robot_cells > 5:
                            powercollect = 5 - robot_cells
                        robot_cells += powercollect
                        print(f"Your robot went and collected {powercollect} Power Cells! This brings your total up to {robot_cells} Power Cells!")
                    else:
                        print("Ouch! Your robot didn't collect any Power Cells! Better luck next time!")
                    matchtimer.intake()
                if b'2' in char_catch:
                    if robot_cells >= 1:
                        lowshoot = random.randint(1,robot_cells)
                        lowmiss = random.randint(1,100)
                        if lowmiss == 50:
                            lowmissed = random.randint(1, lowshoot)
                            lowshoot -= lowmissed
                        robot_cells -= lowshoot
                        powercount += lowshoot
                        print(f"Your robot shot {lowshoot} Power Cells, gaining your alliance {lowshoot} points!")
                        if user_alliance == "Blue Alliance":
                            blue_alliance_score += lowshoot
                        elif user_alliance == "Red Alliance":
                            red_alliance_score += lowshoot
                    else:
                        print("You don't have enough Power Cells to do this! Go get more!")
                    matchtimer.lowgoal()
                if b'3' in char_catch:
                    highmissed = 0
                    if robot_cells >= 1:
                        highshoot1 = random.randint(1,robot_cells)
                        highshoot2 = highshoot1
                        highmiss = random.randint(1,2)
                        if highmiss == 2:
                            highmissed = random.randint(1,highshoot2)
                            highshoot2 -= highmissed
                        robot_cells -= highshoot1
                        powercount += highshoot2
                        highscore = highshoot2 * high_goal
                        print (f"Your robot shot {highshoot1} Power Cells and missed {highmissed} shots! Your alliance gained {highscore} points!")
                        if user_alliance == "Blue Alliance":
                            blue_alliance_score += highscore
                        elif user_alliance == "Red Alliance":
                            red_alliance_score += highscore
                    else:
                        print("You don't have enough Power Cells to do this! Go get more!")
                    matchtimer.highgoal()

                
                if match_time == 0:
                    print("Aaaand game! Press Q to Quit")
                    char_catch = keypress()
                    if char_catch in [b'q',b'Q']:
                        exit("Goodbye!")

                    

                elif char_catch in [b'q',b'Q']:
                    exit("Goodbye!")
        
        #Exit condition for pre-game
        elif char_catch in [b'q',b'Q']:
            exit("Goodbye!")

#Exit condition for beginning
elif char_catch in [b'q',b'Q']:
    exit("Goodbye!")