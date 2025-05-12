def get_word_count(booktext):
    words = booktext.split()
    return len(words)

def get_char_count(booktext):
    charCount = {}
    booktext = booktext.lower()
    for char in booktext:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    return charCount

def sort_char_count(charCount):
    sortedChars = []
    for key in charCount:
        sortedChars.append({"char": key, "num": charCount[key]})
    # sortOn = sortedChars["num"]
    # print(sortedChars)
    sortedChars.sort(reverse=True, key=sort_on)
    return sortedChars

def sort_on(dict):
    return dict["num"]