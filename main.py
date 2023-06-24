# Imports
import random
import time
import sys
import os


# Colors
WHITE = "\033[0;37m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
PINK = "\033[1;31m"
BLUE = "\033[0;34m"
PURPLE = '\033[95m'
DARKCYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLACK = "\033[0;30m"
MAGENTA = "\033[0;35m"
BRIGHT_BLACK = "\033[0;90m"
BRIGHT_RED = "\033[0;91m"
BRIGHT_GREEN = "\033[0;92m"
BRIGHT_YELLOW = "\033[0;93m"
BRIGHT_BLUE = "\033[0;94m"
BRIGHT_MAGENTA = "\033[0;95m"
BRIGHT_CYAN = "\033[0;96m"
BRIGHT_WHITE = "\033[0;97m"

# bg = Background colors
bg_black = '\x1b[40m'
bg_red = '\x1b[41m'
bg_green = '\x1b[42m'
bg_yellow = '\x1b[43m'
bg_blue = '\x1b[44m'
bg_magenta = '\x1b[45m'
bg_cyan = '\x1b[46m'
bg_white = '\x1b[47m'
bg_grey = '\x1b[100m'
bg_bright_red = '\x1b[101m'
bg_bright_green = '\x1b[102m'
bg_bright_yellow = '\x1b[103m'
bg_bright_blue = '\x1b[104m'
bg_bright_magenta = '\x1b[105m'
bg_bright_cyan = '\x1b[106m'
bg_bright_white = '\x1b[107m'

# Extras
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# Sleep function
sleep = time.sleep
# sleep(2)     Sleep 2 seconds


def typewriter(message):
  for i in message:
    sys.stdout.write(i)
    sys.stdout.flush()
    if ((i != "\n") and (i != ":")):
        time.sleep(0.05)
    else:
	    time.sleep(0.05)

#typewriter(text)

# Fast Typewriter


def typewriter1(message):
  for i in message:
    sys.stdout.write(i)
    sys.stdout.flush()
    if ((i != "\n") and (i != ":")):
        time.sleep(0.0001)
    else:
	    time.sleep(0.0001)

# Medium Typewriter


def typewriter2(message):
  for i in message:
    sys.stdout.write(i)
    sys.stdout.flush()
    if ((i != "\n") and (i != ":")):
        time.sleep(0.051)
    else:
	    time.sleep(0.033)


# Clear screen function
def clear(): return os.system('clear')
# clear()

# define the countdown func.


def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

# function call
#countdown(20)


# Loading function
def loading():
  print("Loading:")

  animation = ["10%", "20%", "30%", "40%",
               "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
               "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

  for i in range(len(animation)):
      time.sleep(0.6)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  typewriter("\n")


# Owner of Repl
owner = os.environ['REPL_OWNER']
# print(owner)

# Printing Hi
#typewriter(ORANGE + BOLD + "Hey " + owner + "\n\n" + END)

# Using loading
#loading()
#clear()

money = 0
bag_level = []
# Pets
common_pets = []
uncommon_pets = []
rare_pets = []
epic_pets = []
mythical_pets = []
legendary_pets = []

shards = 0
pickaxe_level = []
upgrage_level = []
bag_level.append("level_1")
bag_level.append("Plastic Bag")

# All


def all():
  # Main Menu
  def Menu():

    # Key Values
    print("\nWhat do you wanna do?\n".center(100))
    print("0. How to use.")
    print("S: Sell your mines")
    print("H. Hunt for a pet")
    print("F. Fish")
    print("Q. Quiz")
    print("B. Backpack")
    print("P. Pets")
    print("Qk. Quake")
    print("R. Rage the mines")
    print("K. Kits")
    print("U. Upgrade")
    print("E. Exit")

  # For sell

  def sell():
    global money
    global bag_level
    if 'level_1' in bag_level:
      random_sell = random.randint(300, 800)
      random_item = random.randint(3, 16)
      typewriter(
          WHITE + BOLD + "\nYou sold:- {} items for {}.\n".format(random_item, random_sell) + END)
      money += random_sell
      sleep(0.2)
      clear()

    elif 'level_2' in bag_level:
      random_sell = random.randint(800, 1500)
      random_item = random.randint(15, 28)
      typewriter(
          WHITE + BOLD + "\nYou sold:- {} items for {}.\n".format(random_item, random_sell) + END)
      money += random_sell
      sleep(0.2)
      clear()

    elif 'level_3' in bag_level:
      random_sell = random.randint(1400, 2100)
      random_item = random.randint(28, 41)
      typewriter(
          WHITE + BOLD + "\nYou sold:- {} items for {}.\n".format(random_item, random_sell) + END)
      money += random_sell
      sleep(0.2)
      clear()

    elif 'level_4' in bag_level:
      random_sell = random.randint(2000, 2600)
      random_item = random.randint(32, 49)
      typewriter(
          WHITE + BOLD + "\nYou sold:- {} items for {}.\n".format(random_item, random_sell) + END)
      money += random_sell
      sleep(0.2)
      clear()

    elif 'rage' in bag_level:
      random_sell = random.randint(1500, 2000)
      random_item = random.randint(28, 53)
      typewriter(WHITE + BOLD + "\nRage activated, You sold:- {} items for {}.\n".format(
          random_item, random_sell) + END)
      money += random_sell
      sleep(0.2)
      clear()

  # For hunt
  def hunt():
    global money
    global common_pets
    global uncommon_pets
    global rare_pets
    global epic_pets
    global mythical_pets
    global legendary_pets

    global upgrage_level
    global shards
    common_pets_random = ['Common Cow', 'Common Bat',
                          'Common Pig', 'Common Sheep', 'Common Squid']
    uncommon_pets_random = ['Uncommon Chicken', 'Uncommon Creeper',
                            'Uncommon Ocelet', 'Uncommon Putterfish', 'Uncommon Wolf']
    rare_pets_random = ['Rare Dolphin', 'Rare Enderman',
                        'Rare Guardian', 'Rare Parrot', 'Rare Turtle']
    epic_pets_random = ['Epic Elder-guardian', 'Epic Iron-golem',
                        'Epic Snow-guardian', 'Epic Villager', 'Epic Wither-skeleton']
    mythical_pets_random = ['Mythical Skeleton-horse',
                            'Mythical Spider-horse', 'Mythical Zombie-horse']
    legendary_pets_random = ['Legendary Giant', 'Legendary Wither']
    all_pets = [common_pets_random, uncommon_pets_random, rare_pets_random,
                epic_pets_random, mythical_pets_random, legendary_pets_random]
    random_pet_choice = random.choice(all_pets)

    def check_already():
      global common_pets
      global uncommon_pets
      global rare_pets
      global epic_pets
      global mythical_pets
      global legendary_pets

      if random_pets in common_pets or random_pets in uncommon_pets or random_pets in rare_pets or random_pets in epic_pets or random_pets in mythical_pets or random_pets in legendary_pets:
        typewriter(GREEN + BOLD + "\nYou already have this pet!\n" + END)
        sleep(0.2)
        clear()
        all()

    if random_pet_choice == common_pets_random:
      random_pets = random.choice(common_pets_random)
      random_shards = random.randint(10, 20)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards\n".format(random_pets, random_shards) + END)
      check_already()
      common_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

    elif random_pet_choice == uncommon_pets_random:
      random_pets = random.choice(uncommon_pets_random)
      random_shards = random.randint(20, 30)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards.\n".format(random_pets, random_shards) + END)
      check_already()
      uncommon_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

    elif random_pet_choice == rare_pets_random:
      random_pets = random.choice(rare_pets_random)
      random_shards = random.randint(30, 40)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards.\n".format(random_pets, random_shards) + END)
      check_already()
      rare_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

    elif random_pet_choice == epic_pets_random:
      random_pets = random.choice(epic_pets_random)
      random_shards = random.randint(40, 50)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards.\n".format(random_pets, random_shards) + END)
      check_already()
      epic_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

    elif random_pet_choice == mythical_pets_random:
      random_pets = random.choice(mythical_pets_random)
      random_shards = random.randint(50, 60)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards.\n".format(random_pets, random_shards) + END)
      check_already()
      mythical_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

    elif random_pet_choice == legendary_pets_random:
      random_pets = random.choice(legendary_pets_random)
      random_shards = random.randint(60, 70)
      typewriter(
          YELLOW + BOLD + "\nYou got a {} and {} shards.\n".format(random_pets, random_shards) + END)
      check_already()
      legendary_pets.append(random_pets)
      shards += random_shards
      sleep(0.2)
      clear()

  # For Fish
  def fish():
    global money
    random_money = random.randint(100, 500)
    typewriter(BLUE + BOLD + "\nYou caught {} money.".format(random_money) + END)
    money += random_money
    sleep(0.2)
    clear()

  # For Backpack
  def backpack():
    global bag_level
    global money
    global pets

    typewriter(PURPLE + BOLD +
               "\nYour bag level is {}\n".format(bag_level[0]) + END)
    typewriter(PURPLE + BOLD +
               "\nYour bagpack mode is {}".format(bag_level[1]) + END)
    sleep(0.2)
    clear()

  # For Pets
  def pets():
    global common_pets
    global uncommon_pets
    global rare_pets
    global epic_pets
    global mythical_pets
    global legendary_pets
    global shards
    global common_pets

    typewriter(PURPLE + BOLD + "You have these many pets:-\n" + END)

    typewriter(
        PINK + BOLD + '\nCommon pets:-\n{}'.format(common_pets[0:]) + END)

    typewriter(
        PINK + BOLD + '\n\nUncommon pets:-\n{}'.format(uncommon_pets[0:]) + END)

    typewriter(PINK + BOLD + '\n\nRare pets:-\n{}'.format(rare_pets[0:]) + END)

    typewriter(PINK + BOLD + '\n\nEpic pets:-\n{}'.format(epic_pets[0:]) + END)

    typewriter(
        PINK + BOLD + '\n\nMythical pets:-\n{}'.format(mythical_pets[0:]) + END)

    typewriter(
        PINK + BOLD + '\n\nLegendary pets:-\n{}'.format(legendary_pets[0:]) + END)
    sleep(0.2)
    clear()

  # For quake
  def quake():
    global legendary_pets
    global money
    if 'Legendary Wither' in legendary_pets:
      typewriter(BLUE + BOLD + "\nYou broke over 50,000 blocks!\n")
      random_money = random.randint(1000, 10000)
      random_item = random.randint(90, 190)
      typewriter("You sold {} items for {}.\n".format(
          random_item, random_money) + END)

      money += random_money
      sleep(0.2)
      clear()

    else:
      typewriter(
          RED + BOLD + "\nYou don't have Wither in your pets, Hunt for it!" + END)
      sleep(0.2)
      clear()

  # For Rage
  def rage():
    global legendary_pets
    global money
    global bag_level

    if 'Legendary Giant' in legendary_pets:
      typewriter(BLUE + BOLD + "\nActivated Rage for 20 seconds!\n" + END)
      bag_level.append('rage')
      sell()
      sleep(0.2)
      clear()

    else:
      typewriter(
          RED + BOLD + "\nYou don't have Giant in your pets, Hunt for it!" + END)
      sleep(0.2)
      clear()

  # Under construction process
  while True:
    Menu()

    # The Loop input:-
    choice = input(CYAN + BOLD + "\nEnter your Choice: " + END)
    choice = choice.lower()

    if choice == "0":
      print("\n\n")

    elif choice == "s":
      sell()

    elif choice == "h":
      hunt()

    elif choice == "f":
      fish()

    elif choice == "q":
      pass

    elif choice == "b":
      backpack()

    elif choice == "p":
      pets()

    elif choice == "qk":
      quake()

    elif choice == "r":
      rage()

    elif choice == "k":
      pass

    elif choice == 'u':
      pass

    elif choice == "e":
      print("Exiting\n.\n..\n...")
      break

    else:
      typewriter(RED + BOLD + "\nWrong Choice Entered. Please try again.\n" + END)
      sleep(0.2)
      clear()


all()

print(money)
