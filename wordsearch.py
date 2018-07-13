import json
import re
import sys
import difflib
from difflib import SequenceMatcher, get_close_matches

# example with get_close_matches(word, iterable, possibilities, ratio)
# results = get_close_matches('rainn', ['help', 'flower', 'rain'], n=2, cutoff=0.7)


# load data using a python data type
data = json.load(open('data.json', 'r'))


def translate_words():
    #pattern = re.compile(r'(\w+[\s\w+]*)', re.M)

    while True:
        words = input('Enter word(s) here: ')
        words = list(map(lambda word: word.strip().lower(), re.findall(r'(\w+[\s+\w+]*)', words)))
       
        if len(words) == 0 or words[0] == 'quit':
            #sys.exit()
            # or
            raise SystemExit

        for word in words:

            test = [word, word.title(), word.upper()]
            for obj in test:
                if obj in data.keys():
                    # word = op
                    print('**{}**'.format(obj))
                    print('\n'.join(data[obj]))
                    break

            else:
                alt = get_close_matches(word, data.keys(), n=2, cutoff=0.7)
                if len(alt) > 0:
                    for i in range(len(alt)):
                        guess = input('\nDid you mean: {}?'.format(alt[i]))
                        #if guess[0].lower() == 'y':
                        if guess.lower().startswith('y'):
                            print('**{}**'.format(alt[i]))
                            for i, d in enumerate(data[alt[i]]):
                                print(i+1, d)
                        break
                else:
                    print('Cannot find \'{}\''.format(word))

        print()


translate_words()

data.close()

