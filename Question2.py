import pandas as pd

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    string = str(string)
    count = 0
    for char in string:
         if char in vowels:
             count += 1
     
    return count

imdb = pd.read_csv('titles.csv')
imdb['vowel_count'] = imdb['title'].apply(count_vowels)
print(imdb)
imdb.to_csv('imdb_with_vowel.csv', index=False)

#File with new name will be created in the base path
#so that the source file is not affected 


