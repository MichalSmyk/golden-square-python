def count_words(str):
    if not str.strip():
        return 0
    
    words_number = str.split(" ")
    return len(words_number)