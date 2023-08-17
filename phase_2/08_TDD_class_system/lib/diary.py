import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        word_counts = [entry.count_words() for entry in self._entries]
        return sum(word_counts)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if self._entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self._entries:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable