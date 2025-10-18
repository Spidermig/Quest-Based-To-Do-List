# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

# game/script.rpy
# ------------------------------------------------------
# TITLE: Quest-Based To-Do List (Mentor Selection Story)
# ------------------------------------------------------

# Declare characters
define p = Character("[player_name]", color="#a8e6cf")
define mentor1 = Character("Astra", color="#ffd3b6")
define mentor2 = Character("Kael", color="#ffaaa5")
define mentor3 = Character("Mira", color="#dcedc1")
define sys = Character("System", color="#b2ebf2")

# Start of the game
label start:

    # Ask player's name
    $ player_name = renpy.input("What is your name, adventurer?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Traveler"

    scene black with fade
    show text "Welcome to QuestDay — a world where your daily tasks become epic adventures!" with dissolve
    pause 2
    hide text

    sys "Every hero needs guidance. Choose your mentor to shape your journey: press enter to choose"

    menu:
        "Choose your mentor:"
        "Astra – The Planner of Light (Focus: Organization & Routine)": 
            jump mentor_astra
        "Kael – The Warrior of Action (Focus: Fitness & Productivity)": 
            jump mentor_kael
        "Mira – The Sage of Balance (Focus: Mindfulness & Rest)": 
            jump mentor_mira

# -----------------------------
# Mentor 1: Astra – Organization
# -----------------------------
label mentor_astra:
    scene bg room
    show mentor1 normal
    mentor1 "Greetings, [player_name]. I am Astra, the Planner of Light."
    mentor1 "Your path will be paved by structure, routine, and order. Press enter to continue."
    mentor1 "Let’s begin your first Daily Quest! Press enter to begin."
    jump daily_quest_astra

label daily_quest_astra:
    scene bg desk
    sys "Today’s Quests:"
    $ quests = ["Organize your workspace", "Write your top 3 priorities", "Clean your email inbox"]
    $ completed = []

    call screen quest_list(quests, completed, "Astra")
    jump day_complete

# -----------------------------
# Mentor 2: Kael – Fitness & Action
# -----------------------------
label mentor_kael:
    scene bg gym
    show mentor2 normal
    mentor2 "Ah, [player_name]! I’m Kael, your mentor in strength and discipline."
    mentor2 "Every day is a battle against procrastination. Let’s conquer it together! Press enter to begin."
    jump daily_quest_kael

label daily_quest_kael:
    scene bg gym
    sys "Today’s Quests:"
    $ quests = ["Stretch for 10 minutes", "Complete your main workout", "Drink 2L of water"]
    $ completed = []
    call screen quest_list(quests, completed, "Kael")
    jump day_complete
   

# -----------------------------
# Mentor 3: Mira – Mindfulness & Rest
# -----------------------------
label mentor_mira:
    scene bg garden
    show mentor3 normal
    mentor3 "Welcome, [player_name]. I am Mira, the Sage of Balance."
    mentor3 "We’ll train your mind to rest as hard as it works. Press enter to begin."
    jump daily_quest_mira

label daily_quest_mira:
    scene bg garden
    sys "Today’s Quests:"
    $ quests = ["Meditate for 5 minutes", "Take a short walk outside", "Reflect on one thing you're grateful for"]
    $ completed = []

    call screen quest_list(quests, completed, "Mira")
    jump day_complete
# -----------------------------
# Quest Screen (Reusable)
# -----------------------------
screen quest_list(quests, completed, mentor_name):

    menu
    #vbox:
    #    spacing 15
    #    text "[mentor_name]'s Daily Quests" size 35 xalign 0.5
#     for q in quests:
    #        if q in completed:
#             text "✓ [q]" color "#77dd77"
#         else:
    #            textbutton "[q]" action [SetVariable("completed", completed + [q]), Return()] 
    #    if len(completed) == len(quests):
    #        textbutton "Finish Day" action Jump("day_complete")
    menu:
        "[mentor_name]'s Daily Quests"
        "[q[0]]":
            jump day_complete
        "[q[1]]":
            jump day_complete
        "[q[2]]":
            jump day_complete
        
# -----------------------------
# Day Complete Screen
# -----------------------------
label day_complete:
    scene bg sunset
    sys "Congratulations, [player_name]! You completed all your quests for the day."
    sys "Return tomorrow for new challenges!"
    return
