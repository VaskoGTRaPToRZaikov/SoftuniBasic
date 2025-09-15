import random

name = input("What is your name? ")

print("Good luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse',
         'water','board', 'geeks', 'algorithm', 'database', 'network', 'software', 'hardware', 'internet', 'keyboard',
         'monitor','processor', 'memory', 'storage', 'cloud', 'server', 'application', 'interface', 'protocol',
         'encryption', 'security','firewall', 'router', 'bandwidth', 'latency', 'pixel', 'resolution', 'graphics',
         'rendering', 'animation', 'virtual','reality', 'augmented', 'machine', 'learning', 'neural', 'artificial',
         'intelligence', 'data', 'analysis', 'statistics', 'probability', 'equation', 'variable', 'function',
         'calculus', 'geometry', 'algebra', 'trigonometry', 'matrix', 'vector','dimension', 'quantum', 'physics',
         'energy', 'motion', 'gravity', 'force', 'velocity', 'acceleration', 'friction', 'wave','particle', 'atom',
         'molecule', 'chemical', 'reaction', 'compound', 'element', 'periodic', 'table', 'biology', 'genetics',
         'evolution', 'ecology', 'organism', 'cell', 'tissue', 'organ', 'system', 'environment', 'climate', 'weather',
         'temperature','pressure', 'humidity', 'wind', 'storm', 'thunder', 'lightning', 'rain', 'snow', 'fog',
         'sunshine', 'ocean', 'river','lake', 'stream', 'pond', 'waterfall', 'glacier', 'mountain', 'valley', 'forest',
         'desert', 'jungle', 'plain', 'plateau','canyon', 'volcano', 'earthquake', 'tsunami', 'tornado', 'hurricane',
         'flood', 'drought', 'wildfire', 'animal', 'mammal','reptile', 'bird', 'fish', 'insect', 'plant', 'tree',
         'flower', 'grass', 'bush', 'vine', 'fruit', 'vegetable', 'seed', 'root', 'stem', 'leaf', 'petal', 'bark',
         'wood', 'metal', 'iron', 'steel', 'copper', 'gold', 'silver', 'aluminum', 'plastic','rubber', 'glass',
         'fabric', 'cotton', 'silk', 'wool', 'leather', 'stone', 'brick', 'cement', 'concrete','building', 'house',
         'apartment', 'office', 'factory', 'warehouse', 'bridge', 'tunnel', 'road', 'highway','railway', 'train',
         'bus', 'car', 'truck', 'bicycle', 'motorcycle', 'airplane', 'helicopter', 'rocket','spaceship', 'satellite',
         'telescope', 'microscope', 'camera', 'lens', 'film', 'screen', 'projector','television', 'radio', 'speaker',
         'microphone', 'headphone', 'phone', 'smartphone', 'tablet', 'laptop', 'desktop', 'printer', 'scanner',
         'joystick', 'mouse', 'trackpad', 'button', 'switch', 'lever', 'gear','engine', 'battery', 'circuit',
         'current', 'voltage', 'resistance', 'capacitor', 'transistor', 'diode','relay', 'fuse', 'plug', 'socket',
         'cable', 'wire', 'fiber', 'optic', 'signal', 'transmission', 'receiver','antenna', 'frequency', 'wavelength',
         'spectrum', 'infrared', 'ultraviolet', 'radiation', 'laser', 'magnet','sensor', 'detector', 'scanner',
         'barcode', 'chip', 'card', 'password', 'username', 'authentication', 'verification', 'session',
         'cookie', 'cache', 'backup', 'restore', 'archive', 'folder', 'file', 'document']

word = random.choice(words)

print("Guess the characters")

guesses = ""
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")

        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("You win\nThe word is: ", word)
        break

    print()
    guess = input("guess a character:")

    if guess in guesses:
        print("This character is already guessed\nEnter new character: ")
        continue

    guesses += guess


    if guess not in word:
        turns -= 1
        print("Wrong input\nYou have", + turns, "more guesses")

        if turns == 0:
            print("You loose\nThe word is: ", word)

