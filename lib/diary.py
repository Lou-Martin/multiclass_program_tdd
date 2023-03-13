# File: lib/diary.py
import math


class Diary:
    def __init__(self):
        self.allentries = []

    def add(self, entry):
        self.allentries.append(entry)

    def all(self):
        return self.allentries

    def count_words(self):
        word_count = 0
        for entry in self.all():
            word_count += entry.count_words()
        return word_count


    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)    
    # this method notably returns a rounded integer (always rounding up)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_can_read = wpm * minutes
        entries = []
        for entry in self.all(): 
            if entry.count_words() <= words_can_read:
                entries.append(entry.contents)
        final_list = sorted(entries)
        print(entries)
        print(final_list)
        return final_list[-1]
