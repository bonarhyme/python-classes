# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, "r") as f:
        lines = f.read()
        return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    asCount = text.lower().replace('\n', '').split().count("as")
    wouldCount = text.lower().replace('\n', '').split().count("would")
    glassCount = text.lower().replace("\n", "").split().count("glass")

    return {"as": asCount, "would": wouldCount, "glass": glassCount}

print(count_words())