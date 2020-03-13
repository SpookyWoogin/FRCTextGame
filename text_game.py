#Text game by Colin Gideon
#The FIRST Robotics Competition and Infinite Recharge are trademarks of FIRST

import random
from msvcrt import getch

lives = 10

print("""Hello and welcome to the 2020 FIRST Robotics Competition!
This years game: INFINITE POSTPONEMENT-er...RECHARGE!
press ENTER to begin or Q to Quit""")

if getch() == b'/r':
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
        The second stage is completed when a alliance scores 20 more power cells and ROTATION CONTROL is completed
        The third stage is completed when a alliance scores 20 more power and POSITION CONTROL is completed
        (The option to spin the CONTROL PANEL will show up when ROTATION & POSITION CONTROL is activated and will dissapear after it's been completed)
    FINALLY, in the last 30 seconds of the game, you're able to score by climbing the SHIELD GENERATOR SWITCH
        For each robot hung, the corrosponding alliance scores 25 points
        For each robot parked, the corrosponding alliance scores 5 points
        If the switch is level, the corrosponding alliance scores 15 points
        
        -=- END OF TEXT WALL -=-""")