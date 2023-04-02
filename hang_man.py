import random

class HangMan:

  def __init__(self):
    self.chance = 7
    self.menu1 = """
    1-Fruit names
    2-Vegetable names
    3-Animal names
    """
    self.fruit_names = [
      'apple', 'banana', 'apricot', 'papaya', 'peach', 'pomegranate',
      'pineapple', 'rambutan', 'raspberries', 'strawberries', 'starfruit',
      'tangerine', 'watermelon', 'sapota'
    ]
    self.vegetable_names = [
      'potato', 'tomato', 'cabbage', 'cauliflower', 'brinjal', 'cucumber',
      'carrot', 'peas', 'radish', 'spinach', 'beetroot', 'broccoli', 'pumpkin',
      'corn', 'mushroom'
    ]
    self.animal_names = [
      'dog', 'lion', 'cat', 'pig', 'rabbit', 'duck', 'fox', 'cow', 'horse',
      'deer', 'snake', 'frog', 'panda', 'scorpion', 'bee', 'sheep', 'otter',
      'bat'
    ]

  def game_choice(self):
    print(self.menu1)
    self.user_choice = input("Press 1,2 or 3 to choose game:\n")
    while True:
      if self.user_choice == "1":
        print("Fruit names game")
        break
      elif self.user_choice == "2":
        print("Vegetable names game")
        break
      elif self.user_choice == "3":
        print("Animal names game")
        break
      else:
        print("Choose 1,2 or 3!!!")
        self.user_choice = input("")

  def computer_word_choice(self):
    self.game_choice()
    if self.user_choice == "1":
      self.computer_choice = random.choice(self.fruit_names)
    if self.user_choice == "2":
      self.computer_choice = random.choice(self.vegetable_names)
    if self.user_choice == "3":
      self.computer_choice = random.choice(self.animal_names)
    # print(self.computer_choice)
    self.word = "_" * len(self.computer_choice)

  def find_letter(self):
    
    print('Find: ', self.word)
    letter = input("Enter the letter: ")
    self.length_word = len(self.computer_choice)

    for i in range(self.length_word):
      if self.computer_choice[i] == letter:
        self.word = self.word[:i] + letter + self.word[i + 1:]
    if letter not in self.computer_choice:
      print("Sorry. This word doesn't exist in this word!!!")
      self.chance -= 1
    print(self.word)

  def play_game(self):
    self.computer_word_choice()
    while (self.chance>0) and (self.word!=self.computer_choice):
      self.find_letter()
    if self.chance==0:
      print("Sorry. You lost the game!!!")
    if self.word==self.computer_choice:
      print("Congratulations!!! You won the game")


hm = HangMan()
hm.play_game()
