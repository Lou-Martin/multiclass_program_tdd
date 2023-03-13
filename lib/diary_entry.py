# File: lib/diary_entry.py
import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.unread_library = self.contents.split()
        
    def count_words(self):
        if self.contents.strip() == "":
            return 0
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)    
    # this method notably returns a rounded integer (always rounding up)

    def reading_chunk(self, wpm, minutes):
        amount_user_can_read = wpm * minutes #this is the calculation that determines the size of chunk
        chunk = ""
        if amount_user_can_read >= len(self.contents.split()):
            return " ".join(str(word) for word in self.contents.split())
        else:
            if self.unread_library == []:
                self.unread_library = self.contents.split()
                #self.unread_library - this is a copy of the diary entry, in list format and should contain all unread text
            else:
                chunk += " ".join(str(word) for word in self.unread_library[0:amount_user_can_read]) #this is the text that the user will read in their alotted time
                del self.unread_library[0:amount_user_can_read] #deletes first word within self.unread library up to the index equal to amount_user_can_read
                return chunk