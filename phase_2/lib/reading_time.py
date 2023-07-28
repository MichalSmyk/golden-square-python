
def reading_time(text):
    words_per_min = 200
    words = len(text.split())
    time = words / words_per_min
    return time