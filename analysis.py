# Weekend Edition Sunday Puzzle (August 11, 2019)
# Rules: Start with a 5-letter word.
# Insert an "e" after the 2nd letter, 4th letter, and 5th letter. 
# Each of the resulting words will form a 6-letter English word. 
# https://www.npr.org/2019/08/11/750176148/sunday-puzzle-cut-and-paste
#
# Andrew Chamberlain, Ph.D.
# www.achamberlain.com

import pandas as pd

# Load a typical English dictionary
eng = pd.read_csv('http://scrabutility.com/TWL06.txt', names=['words']).astype(str)

# Keep only 5, 6 letter words. 
eng['len'] = eng['words'].apply(lambda x: len(x))
eng5 = eng[eng['len'] == 5]
eng6 = eng[eng['len'] == 6]

# Function to insert "E" after Nth character. 
def ins(string,n):
    return ''.join(string[:n] + 'E' + string[n:])

# Insert "E" after 2nd letter
eng5['e2'] = eng5['words'].apply(lambda x: ins(x,2))

# Insert "E" after 4th letter
eng5['e4'] = eng5['words'].apply(lambda x: ins(x,4))

# Insert "E" after 5th letter
eng5['e5'] = eng5['words'].apply(lambda x: ins(x,5))

# Check if resulting words are in the English dictionary. 
eng5['in_2'] = eng5['e2'].apply(lambda x: 1 if x in tuple(eng6['words']) else 0)
eng5['in_4'] = eng5['e4'].apply(lambda x: 1 if x in tuple(eng6['words']) else 0)
eng5['in_5'] = eng5['e5'].apply(lambda x: 1 if x in tuple(eng6['words']) else 0)

# Find solution: All 4 words in dictionary.
solution = eng5[(eng5['in_2']==1) & (eng5['in_4']==1) & (eng5['in_5']==1)]

# Print result ("SPARS").
print(solution)