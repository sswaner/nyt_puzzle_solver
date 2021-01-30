import math
from itertools import combinations
from datetime import datetime
from pprint import pprint
t1 = datetime.now()
#letters = 'tgjrmsbliuae'
letters = 'sokatycrmiel'
letters = 'hedikbtwacrn'
#letters = 'vbregnilcasf'

letter_set = set([l for l in letters])

def find_answers(words, letters):
  matrix = []
  for e in words:
    for p in words:
      if e != p:
        if e[-1:] == p[:1]:
          matrix.append((e, p))
  answers = []
  for answer in matrix:
    #print("testing {0}".format(' '.join(answer)))
    if letters - set([l for l in ''.join(answer)]) == set():
      answers.append(answer)
  return answers

def find_answers_deep(words, letters):
  matrix = []
  for e in words:
    for p in words:
      if e != p:
        if e[-1:] == p[:1]:
          matrix.append((e, p))
  answers = []
  for answer in matrix:
    if letters - set([l for l in ''.join(answer)]) == set():
      answers.append(answer)
  #answers = []
  if len(answers) < 3:
    max_len = 100
    print("No two word answers, still searching")
    print(len(matrix))
    print(len(words))
    for answer in matrix:
      match_count = 0
      for word in words:
        #print(answer[1][-1:], word[:1])
        if answer[1][-1:] == word[:1]:
          
          extended = answer + (word, )
          if letters - set([l for l in ''.join(extended)]) == set():
            #print(letters - set([l for l in ''.join(extended)]))
            if len(''.join(extended)) < max_len:
              #print("ANSWER:", extended)
              answers.append(extended)
              #max_len = len(''.join(answer))
              match_count += 1


  return answers

def check_word(word, letters):
  #word_set = set([l for l in word])
  for l in word:
    if l not in letters:
      return False
  for i in range(0, len(word)-1):
    pair = word[i:i+2]
    ll = math.ceil((letters.index(pair[0])+1)/3)
    lr = math.ceil((letters.index(pair[1])+1)/3)
    if ll == lr:
      return False
  return True

f = open("vertex_words.txt", 'r')

words = [word.strip() for word in f.read().split('\n') 
        if check_word(word.strip(), letters)]
print(len(words), "matching words")

results = find_answers_deep(words, letter_set)
pprint(results)
max_len = 100
best_answer = None
for result in results:
  if len(''.join(result)) < max_len:
    max_len = len(''.join(result))
    best_answer = result
print("Total Options:", len(results))
print("Best Option: ", best_answer)
t2 = datetime.now()
print(t2 -t1)
