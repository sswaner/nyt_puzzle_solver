from pprint import pprint


def check_word(word, letters):
  if len(word) < 4:
    return False
  #word_set = set([l for l in word])
  if letters[0] not in word:
    return False
  for l in word:
    if l not in letters:
      return False
    
  return True

def scan(letters):
  f = open("vertex_words.txt", 'r')

  words = [word.strip() for word in f.read().split('\n') 
          if check_word(word.strip(), letters)]
  words.sort()
  pprint(words)
  print(len(words))
l = 'dgniatp'

scan(l)