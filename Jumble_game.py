import random


class Jumble_game:

  def __init__(self):
    self.wordlist = [
      'hello', 'world', 'python', 'programming', 'computer', 'science',
      'algorithm', 'data', 'structure', 'network', 'security', 'encryption',
      'decryption', 'authentication', 'authorization', 'database', 'server',
      'client', 'internet', 'website', 'web', 'browser', 'javascript', 'html',
      'css', 'java', 'c', 'c++', 'ruby', 'perl', 'php', 'swift', 'objectivec',
      'android', 'ios', 'mobile', 'application', 'software', 'hardware',
      'machine', 'learning', 'artificial', 'intelligence', 'neural', 'network',
      'deep', 'learning', 'big', 'data', 'cloud'
    ]
    print("Start Jumble game!!!")

  def shuffled_word(self, list1):
    self.word = random.choice(list1)
    list1.remove(self.word)
    self.shuffled = list(self.word)
    random.shuffle(self.shuffled)
    self.shuffled = "".join(self.shuffled)
    print(self.shuffled)

  def find_word(self):
    self.shuffled_word(self.wordlist)
    self.your_version = input("Write the word:\n")
    if self.your_version == self.word:
      self.your_score += 1
      print(f"You are right! Your score: {self.your_score}")
    if self.your_version != self.word:
      print(f"You are wrong! Your score: {self.your_score}")

  def play_game(self):
    self.your_score = 0
    self.game_count = 0
    while self.game_count < 10:
      print(f"Game number: {self.game_count+1}")
      self.find_word()
      self.game_count += 1
    if self.your_score >= 7:
      print(f"Congratulations! Your score:{self.your_score}")
    else:
      print(f"You lost the game! Your score: {self.your_score}")


jg = Jumble_game()
jg.play_game()
