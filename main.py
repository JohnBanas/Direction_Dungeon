# This is a sample Python script.
from art import *
from os import system


# function to clear the terminal
def clear():
    _ = system('clear')


# Main menu Ascii art
def menu():
    clear()
    tprint(" Welcome to Direction Dungeon! ", font="fancy2", chr_ignore=True, decoration="wave3")
    print(" ")
    # Text for main title "fancy4" decoration="wave3"
    aprint("sword2")
    tprint(" Enter a number for the options below: ", font="fancy4", chr_ignore=True)
    aprint("sword2")
    print(" ")
    option = input('''1. New Game 
2. Leaderboards 
 ''')
    if option == '1':
        print('You have selected a new game.')
        clear()
        pre_game_start()
    else:
        print('You have selected leaderboards.')
        # leaderboard()


class MyColors:
    YELLOW_GOLD = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'
    FOREGROUND_RED = "\033[31m"
    BRIGHT_CYAN = "\033[36;1m"


new_game = True


def new_game_start(person, person_choice):
    clear()
    if person_choice == '5':
        global new_game
        new_game = True
        menu()
    elif person_choice == '1':
        aprint("sword2")
        print(f'''{MyColors.YELLOW_GOLD}{person}{MyColors.END}, some would call you wise to go towards what you can 
        see, but soon you may learn not all is as it seems in the dark. 
        
        As you near the flame you notice it is a torch on the wall, you reach and pull the torch from it's home, 
        and hear a faint click behind the wall. You have only a moment of confusion, for abruptly the floor gives out 
        from under you, as a trapdoor opens and you begin to slide down into the depths of darkness. 
        Down you slide until suddenly you are falling weightless. You slam into a hard stone surface. As you are jarred 
        badly, your breath leaves you, spots dance before your eyes rimmed in silver and purple hues, 
        as you slip into unconsciousness...''')
        aprint("sword2")
        input(f'''In the darkness you hear a voice... wait... you have heard this before... '
        {MyColors.YELLOW_GOLD}(Press <Enter>){MyColors.END}''')
    elif person_choice == '2':
        aprint("sword2")
        print(f'''You grasp the icy cold handle of the door with the {MyColors.YELLOW_GOLD}strange runes{MyColors.END}  
        to enter the room, and almost plummet off the sheer edge of a cliff! The room no longer exists and somehow in 
        it's place an endless sky ridden with flashes of shrieking lighting, howling winds, and deafening thunder. You 
        nearly fall into the room that no longer has a floor but a plummeting drop to a sea as endless as the sky, but
        as you lean forward you still have a firm grip on the cold iron door handle. A gust of wind violently pulls out 
        the door and as it goes so too do you. Swinging wildly over the chasm, looking in horror at the towering waves
        below, you hang on to the door, your salvation, your only hope. Rain begins to not fall, but whip and scour 
        you. You can feel your grip weaken on the handle. Soon your strength will leave, the icy chill numb your hands 
        completely, and the slick handle will let you fall to your doom. As the door swings back to the open hallway,   
        you desperately try to place a foot on the edge! Only to slip off. Again you swing with the door, as it groans 
        and creaks in the storm, you again flail your feet to find the safety of edge, and there! You have done it. As 
        you pull yourself up with the door and begin to maneuver your body into the doorway, a sudden snap! The door 
        gives way and you both fall down as the wind whistles by you, you have too much time to think during the long 
        fall to the crushing embrace of the sea. As it rushes towards you faster and faster, you close your eyes and 
        shield yourself in a futile human instinctual reaction. You hit hard, and the water envelopes you instantly, 
        swirling and tossing with no sense of time or direction. You feel your heart slow, your aching body numb, as you 
        begin to fade into the unconsciousness.''')
        aprint("sword2")
        input(f'''In the darkness you hear a voice... wait... you have heard this before... '
        {MyColors.YELLOW_GOLD}(Press <Enter>){MyColors.END}''')
    elif person_choice == '3':
        aprint("sword2")
        print(f'''As you make your way in the darkness the musty smell becomes stronger and you see a 
        {MyColors.GREEN}glowing green light{MyColors.END} coming from another doorway filled with {MyColors.YELLOW_GOLD}
        strange runes {MyColors.END}. Whispers here as well. They do not call your name though, they hiss venomous 
        warning... and pain. You slowly back away from the door as the glow gets brighter, and you realize the wind is 
        coming from this door! The wood creaks and groans and begins to bulge, then explodes with wooden shards and 
        shrapnel and green mist flying all around you. You are thrown to floor and as you rise you see within the room 
        far back against a wall two small eyes made of {MyColors.GREEN}glowing green light{MyColors.END}. Scrambling to 
        your feet you realize this creature was trapped behind the door. Did it have something to do with the
        {MyColors.YELLOW_GOLD}strange runes{MyColors.END}? You notice the shadow creature is staring directly at you.
        It suddenly appears halfway across the room, and it's shape has changed. Formless before, now it appears almost
        human? You take a step back, and it mirrors you with a step forward, and further defines it's shape. Definitive 
        arms and legs are there now. Your blood begins to turn cold as you take another step back, it moves with you 
        and further defines to your height. You begin to raise your hand to your mouth and watch as it mirrors you 
        exactly. The creature quickly turns and slips into a dark corner of the room and vanishes before you can blink.
        You begin to run back the way you came, a thought seeps into your mind, the shadows are dangerous. You run back 
        to the room you awoke in, but the door will not budge and the runes glow ominously as the whispers scream and 
        cry warnings! You can almost make out what they say... {person}...beware...the shadow... You turn and run to the 
        torch in the hallway, quickly grabbing it and swinging it wildly in the dark. The whispers have silenced. You 
        feel something at your feet, as you look down your shadow made in the torch light is not moving with you! The 
        shadow at your feet oozes up your skin, you know where it touches is gone from you, could you have cut off your 
        feet you would, but you can only watch as the shadow slowly makes it's way up your body. You try to struggle, 
        pull, push, but as you touch it, the shadow oozes to your hands and now it moves more quickly. The numbness is 
        spreading through your body, it is now at your neck. Useless tears begin to form and as it crawls over your face 
        and into your body, your last thought is gratitude it is over. Darkness envelopes you.''')
        aprint("sword2")
        input(f'''In the darkness you hear a voice... wait... you have heard this before... '
        {MyColors.YELLOW_GOLD}(Press <Enter>){MyColors.END}''')
    elif person_choice == '4':
        aprint("sword2")
        print(f'''As you make your way towards the darkness of hallway, you arrive at the edge of where the light ends 
        and a pitch blackness begins. Odd, there is not a gradual transition, it just... ends. You reach your hand out 
        gradually, and witness your fingers disappear bit by bit as they cross that divide. Quickly you pull your 
        fingers back and see that they are fine. A deep and hearty laugh that shakes the foundations of this place and 
        booms in your body shocks you to covering your ears. {MyColors.FOREGROUND_RED}"WELL, HERE YOU ARE AGAIN. DO YOU 
        AT LEAST HAVE YOUR MEMORY THIS TIME? IT'S ALWAYS ENTERTAINING WHEN YOU REMEMBER AS WELL... FOR ME."
        {MyColors.END} Your mouth dry, you nervously lick your lips, {MyColors.YELLOW_GOLD}"Who are you, and 
        why am..."{MyColors.END} The bellowing laugh returns and shakes you to your core. {MyColors.FOREGROUND_RED}"WHO 
        AM I? YOU PATHETIC CREATURE, I AM WHAT YOU CANNOT FATHOM, I AM WHAT YOU HAVE FACED FOR A THOUSAND YEARS! FACED 
        AND FAILED TIME AND TIME AGAIN! YOU LET THEM DOWN. I ADMIT I UNDERESTIMATED YOU, BUT YOU THOUGHT YOU WOULD 
        DESTROY ME? HA. THE INSOLENCE. THE FAILURE. YOU ARE THE LAST, AND YOU DON'T EVEN KNOW. HAHAHAHAH! IT WILL END 
        THIS TIME THERE IS NO ONE ELSE TO SPARE YOU THAT FATE THIS TIME. I WILL RIP YOUR..."{MyColors.END} The voice 
        ends. Time seems to slow and you cannot move, you float in between a dream. A faint whisper catches your ear
        {MyColors.BRIGHT_CYAN}"We will not abandon you here. We made a blood oath with the fa'da'Mael, 
        it cannot be broken only fulfilled. You are the last. Fulfill our oath so that all may rest, 
        even Shah'Me'hett. You loved him as brother once and he you. We cannot heal your mind, it is self-inflicted, but 
        you did not say why. We will never let you die. We will keep the bond, though we will 
        never know peace, we know only pain in the dream. The last of my spells is hidden in the Mithriem, 
        you have need of it. Don't follow the speaker in your mind there, tell him my name, that is the only direction 
        to go. Speak of{MyColors.END}{MyColors.YELLOW_GOLD} 
        Shah'Em'Mahael{MyColors.END}{MyColors.BRIGHT_CYAN}. The others will find you if they can. Peace to you 
        Shah'Me..."{MyColors.END}{MyColors.FOREGROUND_RED}
        "NOOO! YOU WILL HAVE NO AID. YOU WILL DIE LIKE THE WORM YOU 
        ARE!!! YOU WILL HAVE NO NAME AND I WILL LEAVE NOTHING OF YOU TO BURY! THE DECEIVER WILL BE SCOURED UNTIL NOTHING 
        IS LEFT OF EVEN YOUR SOUL."{MyColors.END} 
        Suddenly the edge of the darkness begins to quiver and tendrils of 
        stinging blackness whip your skin as they surround and tighten onto your arms, legs, neck. They pull you in to 
        the darkness, until even your screams of pain are swallowed in the deep.''')
        aprint("sword2")
        input(f'''In the darkness you hear a voice... wait... you have heard this before... '
        {MyColors.YELLOW_GOLD}(Press <Enter>){MyColors.END}''')
    pre_game_start(person)


return_neutral_options = [
    print(f'''You suddenly realize you are walking down a hallway. You hear an eerie shriek in the distance. 
    Whipping around you see nothing, yet when you turn again you see a door in front of you. 
    You open the door expecting to go into a room and you come out into a hallway that looks vaguely familiar. 
    As the door closes, you turn to see an all too familiar door with... no...
    {MyColors.YELLOW_GOLD}strange runes{MyColors.END} humming. The whisperers are always present around these doors, but
    their words are unintelligible. Where is this place?'''), print(f'''What lies beyond these endless mazes of hallways, 
    {MyColors.YELLOW_GOLD}"Is it all within my mind? Am I going mad?"{MyColors.END} You say aloud, and inside you wonder 
    who am I speaking to you and narrating your own thoughts to you? All this and more will be revealed. You realize you 
    have come to an intersection with another hallway. 
    {MyColors.GREEN}In front{MyColors.END} there is a small sound, almost like water dripping from somewhere... is that 
    the sea? {MyColors.GREEN}To the right{MyColors.END} you can smell the sun beaming on a field in the midst of full 
    summer day. How long since you have seen light? Is that a faint light down the hall? {MyColors.GREEN}To the left
    {MyColors.END} you glance, the whisperers loudly begin to wail, and the current cacophony of their anguish would 
    pale in comparison to the sounds they would release, if you were to go that way. 
    that way.'''), print(f'''You come to and you are seated on the ground, but for how long? You look and there is a 
    window! The sky, fresh air, how you have longed for it! As you push gently, it doesn't budge. You run hard, and with 
    all of your strength and weight push into the window, but it flies open effortlessly and you tumble in and land 
    hard on your face. As you brush yourself off and gather your surroundings, you don't need to look to hear the 
    whisperers and the gentle hum of the door with runes. You are back where you started, and doomed to be.''')]


return_positive_options = [
    print(f'''You see the bright silver outline of a doorway. These runes are similar to the door
    you awoke behind, but there is no fear or malice in the whispers you hear. {MyColors.BRIGHT_CYAN}"We knew you were 
    the best of us. We knew you would persevere to find the way out and break the Beast's illusions. Oath fulfilled we 
    can rest. The Beast still lives tied to the flesh of Shah'Me'hett, will you be at peace with that?"{MyColors.END} 
    There is no further reply and you know that you can freely leave this prison, but will it be for good?''')]


return_negative_options = [
    print(f'''You have always had feeling that something was watching, waiting, there, but just out of your eye sight, 
    but these {MyColors.FOREGROUND_RED}glowing red eyes{MyColors.END} are very near, and as the creature comes into the 
    light you have the only the briefest moment to realize you will not be getting away this time. You scream as it 
    begins to rip you apart, not because of the pain, but because you suddenly remember this from before.''')]


def game_function(player, option):




def pre_game_start(player=False):
    clear()
    global new_game
    if not player and new_game:
        print(" ")
        player = input(''' In the darkness you hear a voice, barely a whisper, "No you are not ready, but it will have 
        to do. Now, what is your name?"
        ''')
    clear()
    aprint("sword2")
    print(f'''{MyColors.YELLOW_GOLD}{player}{MyColors.END}, you find yourself waking in a dark stone room. 
    As if, from a dream? A dream of pain... wait, what does that mean? You are confused, lost, yet have a feeling of 
    dread, as if danger lurks at the edge of your mind. With no recollection of how you came to be here, 
    you look ahead and notice a large wooden door with a black iron handle. 
    The door is covered in {MyColors.FOREGROUND_RED}strange runes{MyColors.END}. 
    On the edge of your mind you hear faint, yet urgent whispers. "They can lie {player}...", 
    you tell yourself. Where did that thought come from? They do not always though, the same feeling says you know it 
    to be true. Have you been here before? How did you come here, what was before? You ponder as you open the door. 
    You see dark hallways, the air thick and damp. In {MyColors.GREEN}front{MyColors.END} of you, there is a faint 
    light at the far end of the hallway, a flame flickering, perhaps, but too far to tell. To your {MyColors.GREEN}right
    {MyColors.END}, a cold breeze blows with smell of age and dust. To your {MyColors.GREEN}left{MyColors.END}, only 
    darkness, and a crushing silence. {MyColors.YELLOW_GOLD}{player}{MyColors.END}, can you still hear the voices of 
    door whispering {MyColors.GREEN}behind{MyColors.END} you? They whisper repeatedly... 
    {MyColors.YELLOW_GOLD}{player}{MyColors.END} you must... 
    {MyColors.YELLOW_GOLD}{player}{MyColors.END} the oath...
    {MyColors.YELLOW_GOLD}{player}{MyColors.END}, till we rest...''')
    aprint("sword2")
    print(" ")
    choice = input('''Which way will you go?
    1. Forward
    2. Back the way I came
    3. Right
    4. Left
    5. End Game
    
    ''')
    if new_game:
        new_game = False
        new_game_start(player, choice)
    else:
        game_function(player, choice)


menu()




