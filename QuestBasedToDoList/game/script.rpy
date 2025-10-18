# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    scene road with fade Transform(zoom=1.5)
    # Ask player's name
    $ player_name = renpy.input("What is your name, adventurer?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Traveler"

    show text "Welcome to QuestDay — a world where your daily tasks become epic adventures!" with dissolve
    pause 2
    hide text

    sys "Every hero needs guidance. Choose your mentor to shape your journey: press enter to choose"
    show sorcerer happy at Position(yalign=1)
    menu:
        "Choose your mentor:"
        "The Planner of Light (Focus: Organization & Routine)": 
            jump mentor_astra
        "The Warrior of Action (Focus: Fitness & Productivity)": 
            jump mentor_kael
        "The Sage of Balance (Focus: Mindfulness & Rest)": 
            jump mentor_mira

# -----------------------------
# Mentor 1: Astra – Organization
# -----------------------------
label mentor_astra:
    scene cottage bedroom
    show mentor1 normal
    $ selectedQuest = 0
    mentor1 "Greetings, [player_name]. I am Maya, the Planner of Light."
    mentor1 "Your path will be paved by structure, routine, and order. Press enter to continue."
    mentor1 "Let’s begin your first Daily Quest! Press enter to begin."
    jump daily_quest_astra

label daily_quest_astra:
    show sorcerer talking at Position(ypos=500)
    scene cottage bedroom
    sys "Today’s Quests:"
    $ quests = ["Organize your workspace", "Write your top 3 priorities", "Clean your email inbox"]
    $ completed = []
    
    call screen quest_list
    jump day_complete

# -----------------------------
# Mentor 2: Kael – Fitness & Action
# -----------------------------
label mentor_kael:
    show clearing 1
    $ selectedQuest = 1
    mentor2 "Ah, [player_name]! I’m Maya, your mentor in strength and discipline."
    mentor2 "Every day is a battle against procrastination. Let’s conquer it together! Press enter to begin."
    jump daily_quest_kael

label daily_quest_kael:
    scene clearing 1
    sys "Today’s Quests:"
    $ quests = ["Stretch for 10 minutes", "Complete your main workout", "Drink 2L of water"]
    $ completed = []
    call screen quest_list
    jump day_complete
   

# -----------------------------
# Mentor 3: Mira – Mindfulness & Rest
# -----------------------------
label mentor_mira:

    scene castle 4
    show mentor3 normal
    $ selectedQuest = 2
    mentor3 "Welcome, [player_name]. I am Maya, the Sage of Balance."
    mentor3 "We’ll train your mind to rest as hard as it works. Press enter to begin."
    jump daily_quest_mira

label daily_quest_mira:
    scene castle 4
    sys "Today’s Quests:"
    $ quests = ["Meditate for 5 minutes", "Take a short walk outside", "Reflect on one thing you're grateful for"]
    $ completed = []

    call screen quest_list
    jump day_complete
# -----------------------------
# Quest Screen (Reusable)
# -----------------------------
screen quest_list():
    vbox:
        align (0.5, 0.5)
        for quest in quests:
            textbutton "[quest]" action Return(quest)
# -----------------------------
# Day Complete Screen
# -----------------------------
label day_complete:
    scene clearing 1
    sys "Congratulations, [player_name]! You completed all your quests for the day."
    sys "Return tomorrow for new challenges!"
    return
