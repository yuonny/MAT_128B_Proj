
# For regular expressions
import re
import string
import pickle 
import csv

def transcribe(filename, output):
    with open(filename, 'r', encoding='utf-8') as file:
        script = file.read()

    # Use raw string literal r'' so that backslashes can be treated as literal characters
    # Makes regex much easier to use since regex has a lot of backslashes

    # Pattern match literal starting brackets with \[
    # [^\]] -> match any character that is not an ending bracket ^\]
    # * -> for 0 or more characters
    # Lastly, match the ending bracket \]
    scriptWithoutBrackets = re.sub(r'\[[^\]]*\]', '', script)

    # re.MULTILINE makes the regular expression match the start of every line
    # the default behavior is to match the start of every string and we don't want that
    # we just want to get rid of the speaker name
    # ^[A-Z] -> match any capital word at the start of each line ()
    # [A-Za-z\s\.\'-] -> match any letters, whitespaces, periods, apostrophes, and hyphens
    # : -> match a colon
    # \s* -> match one or more whitespaces
    # In combination, these expressions should filter out speaker names
    scriptWithoutSpeakers = re.sub(r'^[A-Z][A-Za-z\s\.\'-]*:\s*', '', scriptWithoutBrackets, flags=re.MULTILINE)

    # tokenizes each line into a list of strings
    tokenizedScript = []
    for line in scriptWithoutSpeakers.splitlines():
        tokenizedLine = []
        for word in line.split():
            cleanWord = word.strip(string.punctuation).lower()
            if cleanWord:
                tokenizedLine.append(cleanWord.lower())
        if len(tokenizedLine) > 0:
            tokenizedScript.append(tokenizedLine)
            
    # with open("tokenizedScript.txt" , "w", newline = '', encoding="utf-8") as file:
    #     for line in tokenizedScript:
    #         file.write(" ".join(line) + "\n")
        
    """ 
    So we want to save our tokens into a pickle (.pkl) file such that the data structure in which we saved our tokens in,
    which is a list of lists in this case, is preserved. It will make it easy for other scripts to obtain the tokens without
    having to reparse our data.
    """
    with open(output, "wb") as f:
        pickle.dump(tokenizedScript, f)


if __name__ == "__main__":
    transcribe("new_spongebob.txt", "tokensNew.pkl")
    transcribe("old_spongebob.txt", "tokensOld.pkl")