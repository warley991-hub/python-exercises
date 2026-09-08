'''
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.

def sp_eng(sentence): 
    # your code here
    pass
'''

def sp_eng(sentence):
        try:
            sentence = sentence.lower()
            while True:
                for i, caracter in enumerate(sentence):
                    match = sentence[i:i+7]
                    if match == 'english':
                        return True
                return False
        except AttributeError:
            return False
        except Exception:
            return False