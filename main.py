import random
f = open("words.txt","r")
data = f.readline()
words = data.split()
#words = ["UMBRELLA","TELESCOPE","SMARTPHONE","COMPUTER","JAVASCRIPT","REFRIGERATOR"]
word = random.choice(words)
word = word.upper()
totalchances = 7
guessedwords = "-"*len(word)
while totalchances !=0:
  print(guessedwords)
  letters = input("Guess A Letter: ").upper()
  if letters in word:
    for index in range(len(word)):
      if word[index]==letters:
        guessedwords = guessedwords[:index]+letters+guessedwords[index+1:]
    if guessedwords == word:
      print("You Won!")
      break
  else:
    totalchances -= 1
    print("Incorrect Guess")
    print("Remaining Chances:   ",totalchances)
else:
  print("No Chance Left!")
  print("GAME OVER!")
  print("Correct Word  Was: ",word)