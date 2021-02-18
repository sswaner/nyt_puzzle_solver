import math

from datetime import datetime
from pprint import pprint
t1 = datetime.now()
#letters = 'tgjrmsbliuae'
puzzle = 'sokatycrmiel'
#puzzle = 'hedikbtwacrn'
#puzzle = 'adsrmntryico'
#letters = 'qaefcnudlito'
#letters = 'abcdefghilmn'
#letters = '231de[dbmeat'
#letters = None
puzzle = 'tgjrmsbliuae'
puzzle = 'sngtfivhlore'
puzzle = 'sngtfivhloer'
puzzle = 'majiruntbeoc'
puzzle = 'yacihxmnlgop'
puzzle = 'raeyoumszing'
puzzle = 'oedkbuarmwit'
puzzle = 'boxaisulentj'
puzzle = 'stdfculohyim'
puzzle = 'epgoakrnlwic'
puzzle = 'dsayurhkozqe'
puzzle = 'praeduoilntc'
puzzle = 'ltareowmighj'
puzzle = 'ouhbcrminate'
puzzle = 'alotizenhxcu'
puzzle = 'tizenhxcualo'
puzzle = 'mlruatgyosnp'
puzzle = 'ncxitperahlo'
def find_answers_deep(words, letters):
  matrix = []
  for e in words:
    for p in words:
      if e != p:
        if e[-1:] == p[:1]:
          matrix.append((e, p))
  answers = []
  for answer in matrix:
    if letters - set(''.join(answer)) == set():
      answers.append(answer)
      #print(answer)
  #answers = []
  if len(answers) > 2:
    return answers
  max_len = 100
  print("Found {0} two word answers, still searching".format(len(answers)))
  for answer in matrix:
    match_count = 0
    for word in [w for w in words if answer[1][-1:] == w[:1]]:
 
      extended = answer + (word, )
      if letters - set(''.join(extended)) == set():
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

def solve_puzzle(letters):
  if not isinstance(letters, str):
    return {'status': 'fail', 'error' : 'input not a string'}
  response = {'status': 'success', 'error' : '' }
  f = open("vertex_words.txt", 'r')

  words = [word.strip() for word in f.read().split('\n') 
          if check_word(word.strip(), letters)]
  f.close()
  pprint(words)
  response['matching_words'] = len(words)
  #letter_set = set([l for l in letters])
  results = find_answers_deep(words, set(letters))
  response['results'] = results
  max_len = 100
  best_answer = None
  for result in results:
    if len(''.join(result)) < max_len:
      max_len = len(''.join(result))
      best_answer = result
  response['best_answer'] = best_answer
  response['total_options'] = len(results)
  
  t2 = datetime.now()
  response['process_time'] = t2 - t1

  return response

if __name__ == '__main__':
  test = solve_puzzle(puzzle)
  pprint(test)
  print(test['best_answer'])