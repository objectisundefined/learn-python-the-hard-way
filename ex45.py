# The Analysis of a Simple Game Engine

# * game
#   - handler scene state, go to next scene, check finished
# * scene_map
#   − store all scenes
# * scene fns
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

# scene is just a function taking some logic and return next scene

from sys import exit
from random import randint
from textwrap import dedent

def death_scene():
  quips = [
    "You died. You kinda suck at this.",
    "Your Mom would be proud...if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this.",
    "You're worse than your Dad's jokes."
  ]

  print(quips[randint(0, len(quips)-1)])
  exit(1)


def central_corridor_scene():
  print(dedent("""
    The Gothons of Planet Percal #25 have invaded your ship and
    destroyed your entire crew. You are the last surviving
    member and your last mission is to get the neutron destruct
    bomb from the Weapons Armory, put it in the bridge, and
    blow the ship up after getting into an escape pod.

    You're running down the central corridor to the Weapons
    Armory when a Gothon jumps out, red scaly skin, dark grimy
    teeth, and evil clown costume flowing around his hate
    filled body. He's blocking the door to the Armory and
    about to pull a weapon to blast you.
  """))

  print("[cheating] actions", ["shoot!",  "dodge!", "tell a joke", "..."])

  action = input("> ")

  if action == "shoot!":
    print(dedent("""
      Quick on the draw you yank out your blaster and fire
      it at the Gothon. His clown costume is flowing and
      moving around his body, which throws off your aim.
      Your laser hits his costume but misses him entirely.
      This completely ruins his brand new costume his mother
      27 bought him, which makes him fly into an insane rage
      and blast you repeatedly in the face until you are
      dead. Then he eats you.
    """))
    return 'death'

  elif action == "dodge!":
    print(dedent("""
      Like a world class boxer you dodge, weave, slip and
      slide right as the Gothon's blaster cranks a laser
      past your head. In the middle of your artful dodge
      your foot slips and you bang your head on the metal
      wall and pass out. You wake up shortly after only to
      die as the Gothon stomps on your head and eats you.
    """))
    return 'death'

  elif action == "tell a joke":
    print(dedent("""
    Lucky for you they made you learn Gothon insults in
    the academy. You tell the one Gothon joke you know:
    Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
    fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
    not to laugh, then busts out laughing and can't move.
    While he's laughing you run up and shoot him square in
    the head putting him down, then jump through the
    Weapon Armory door.
    """))
    return 'laser_weapon_armory'

  else:
    print("DOES NOT COMPUTE!")
    return 'central_corridor'


def laser_weapon_armory_scene():
  print(dedent("""
    You do a dive roll into the Weapon Armory, crouch and scan
    the room for more Gothons that might be hiding. It's dead
    quiet, too quiet. You stand up and run to the far side of
    the room and find the neutron bomb in its container.
    There's a keypad lock on the box and you need the code to
    get the bomb out. If you get the code wrong 10 times then
    the lock closes forever and you can't get the bomb. The
    code is 3 digits.
  """))

  code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"

  print("[cheating] code", code)

  guess = input("[keypad]> ")
  guesses = 0

  while guess != code and guesses < 10:
    print("BZZZZEDDD!")
    guesses += 1
    guess = input("[keypad]> ")

  if guess == code:
    print(dedent("""
      The container clicks open and the seal breaks, letting
      gas out. You grab the neutron bomb and run as fast as
      you can to the bridge where you must place it in the
      right spot.
    """))
    return 'the_bridge'
  else:
    print(dedent("""
      The lock buzzes one last time and then you hear a
      sickening melting sound as the mechanism is fused
      together. You decide to sit there, and finally the
      Gothons blow up the ship from their ship and you die.
    """))
    return 'death'


def the_bridge_scene():
  print(dedent("""
    You burst onto the Bridge with the netron destruct bomb
    under your arm and surprise 5 Gothons who are trying to
    take control of the ship. Each of them has an even uglier
    clown costume than the last. They haven't pulled their
    weapons out yet, as they see the active bomb under your
    arm and don't want to set it off.
  """))

  print("[cheating] actions", ["throw the bomb", "slowly place the bomb", "..."])

  action = input("> ")

  if action == "throw the bomb":
    print(dedent("""
      In a panic you throw the bomb at the group of Gothons
      and make a leap for the door. Right as you drop it a
      Gothon shoots you right in the back killing you. As
      you die you see another Gothon frantically try to
      disarm the bomb. You die knowing they will probably
      blow up when it goes off.
    """))
    return 'death'

  elif action == "slowly place the bomb":
    print(dedent("""
      You point your blaster at the bomb under your arm and
      the Gothons put their hands up and start to sweat.
      You inch backward to the door, open it, and then
      carefully place the bomb on the floor, pointing your
      blaster at it. You then jump back through the door,
      punch the close button and blast the lock so the
      Gothons can't get out. Now that the bomb is placed
      you run to the escape pod to get off this tin can.
    """))
    return 'escape_pod'

  else:
    print("DOES NOT COMPUTE!")
    return "the_bridge"


def escape_pod_scene():
  print(dedent("""
    You rush through the ship desperately trying to make it to
    the escape pod before the whole ship explodes. It seems
    like hardly any Gothons are on the ship, so your run is
    clear of interference. You get to the chamber with the
    escape pods, and now need to pick one to take. Some of
    them could be damaged but you don't have time to look.
    There's 5 pods, which one do you take?
  """))

  good_pod = randint(1,5)

  print("[cheating] good_pod", good_pod)

  guess = input("[pod #]> ")

  if int(guess) != good_pod:
    print(dedent("""
      You jump into pod {guess} and hit the eject button.
      The pod escapes out into the void of space, then
      implodes as the hull ruptures, crushing your body into
      jam jelly.
    """))
    return 'death'
  else:
    print(dedent("""
      You jump into pod {guess} and hit the eject button.
      The pod easily slides out into space heading to the
      planet below. As it flies to the planet, you look
      back and see your ship implode then explode like a
      bright star, taking out the Gothon ship at the same
      time. You won!
    """))
    return 'finished'


def finished_scene():
  print("You won! Good job.")
  return 'finished'

scene_map = {
  'central_corridor': {'name': 'central_corridor', 'fn': central_corridor_scene},
  'laser_weapon_armory': {'name': 'laser_weapon_armory', 'fn': laser_weapon_armory_scene},
  'the_bridge': {'name': 'the_bridge', 'fn': the_bridge_scene},
  'escape_pod': {'name': 'escape_pod', 'fn': escape_pod_scene},
  'death': {'name': 'death', 'fn': death_scene},
  'finished': {'name': 'finished', 'fn': finished_scene},
}

def game(start_scene):
  current_scene = scene_map[start_scene]
  last_scene = scene_map['finished']

  while current_scene['name'] != last_scene['name']:
    next_scene_name = current_scene['fn']()
    current_scene = scene_map[next_scene_name]

  # be sure to print out the last scene
  current_scene['fn']()


game('central_corridor')

# function style, small and simple
# class style
# A foolish consistency is the hobgoblin of little minds. Consistency is good, but foolishly following
# some idiotic mantra because everyone else does is bad style. Think for yourself.

# ex43 in function style way