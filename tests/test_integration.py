from lib.diary import Diary
from lib.diary_entry import DiaryEntry

'''

given an entry (diary_entry)
#add stores the entry to entries list

'''

def test_add_given_entry_to_list():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first dairy entry")
    diary.add(diary_entry)
    assert diary.all() == [diary_entry]

'''

given multiple diary entries
adds all entries to list

'''



def test_add_next_given_entry_to_list():
    diary = Diary()
    diary_entry = DiaryEntry("First Entry", "This is the first dairy entry")
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second dairy entry, nice!")
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry, diary_entry_2]

'''

given a diary
return number of words in all entries

'''

def test_count_words():
    
