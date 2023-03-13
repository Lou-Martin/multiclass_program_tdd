from lib.diary import Diary
from lib.diary_entry import DiaryEntry

'''

given an entry (diary_entry)
#add stores the entry to entries list

'''

def test_add_given_entry_to_list():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary.add(diary_entry)
    assert diary.all() == [diary_entry]

'''

given multiple diary entries
adds all entries to list

'''



def test_add_next_given_entry_to_list():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry, diary_entry_2]

'''

given a diary
return number of words in all entries

'''

def test_count_words():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.count_words() == 13

'''

same test given a different number of entries to counteract hardcoded result

'''

def test_count_words_for_three_entries():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary_entry_3 = DiaryEntry("Third Entry", "This is the third diary entry, it's super nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.count_words() == 22


'''

given a value (words per minute)
return an integer that represents the time it would take for a user to read all entries in the diary

'''

def test_reading_time():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary_entry_3 = DiaryEntry("Third Entry", "This is the third diary entry, it's super nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(1) == 22

'''

same test, different value to check float to integer

'''

def test_reading_time_10():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first dairy entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary_entry_3 = DiaryEntry("Third Entry", "This is the third diary entry, it's super nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(10) == 3

'''

given a diary, a number (represnting wpm) and a number (representing minutes)
return the instance of diaryentry that is closest to (but not exceeding) the length the user can read in the given time

'''

def test_find_best_entry_second_entry():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary_entry_3 = DiaryEntry("Third Entry", "This is the third diary entry, it's super nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.find_best_entry_for_reading_time(7, 1) == "This is the second diary entry, nice!"

'''

test the math on the same method

'''

def test_find_best_entry_first_entry():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first diary entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second diary entry, nice!")
    diary_entry_3 = DiaryEntry("Third Entry", "This is the third diary entry, it's super nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.find_best_entry_for_reading_time(2, 3) == "This is the first diary entry"