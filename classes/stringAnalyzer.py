import re

#CASE FILTERS
JUST_LOWERCASE = [True, False]
JUST_UPPERCASE = [False, True]
INGORE_CASE = [True, True] 

#LETTER COUNT PATTERNS
ALL_LOWERCASE = "a-z"
ALL_UPPERCASE = "A-Z"
LETTER_PATTERNS = [ALL_LOWERCASE, ALL_UPPERCASE]

#VOWEL COUNT PATTERNS
VOWEL_LOWERCASE = "aeiou"
VOWEL_UPPERCASE = "AEIOU"
VOWEL_PATTERNS = [VOWEL_LOWERCASE, VOWEL_UPPERCASE]

#CONSONANT COUNT PATTERNS
CONSONANT_LOWERCASE = "b-df-hj-np-tv-z"
CONSONANT_UPPERCASE = "B-DF-HJ-NP-TV-Z"
CONSONANT_PATTERNS = [CONSONANT_LOWERCASE, CONSONANT_UPPERCASE]

def CountLetters(string, caseFilter):
    pattern = PatternBuilder(LETTER_PATTERNS, caseFilter)
    result = re.findall(pattern, string)
    return len(result)

def CountVowels(string, caseFilter):
    pattern = PatternBuilder(VOWEL_PATTERNS, caseFilter)
    result = re.findall(pattern, string)
    return len(result)

def CountConsonants(string, caseFilter):
    pattern = PatternBuilder(CONSONANT_PATTERNS, caseFilter)
    result = re.findall(pattern, string)
    return len(result)

def PatternBuilder(patterns, caseFilter):
    result = ""

    if caseFilter == INGORE_CASE:
        result = f"[{patterns[0]}{patterns[1]}]"
    elif caseFilter == JUST_LOWERCASE:
        result = f"[{patterns[0]}]"
    elif caseFilter == JUST_UPPERCASE:
        result = f"[{patterns[1]}]"

    return result