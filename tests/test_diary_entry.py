from lib.diary_entry import DiaryEntry

'''

given a diary entry
counts the words within and returns the resultant number

'''

def test_count_words_with_one_entry():
    diary_entry = DiaryEntry("First Entry", "This is the first dairy entry")
    assert diary_entry.count_words() == 6

'''

same test, different string, more words

'''


def test_count_words_with_different_entry():
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second dairy entry, nice!")
    assert diary_entry_2.count_words() == 7

'''

given a diary entry
return the time (int) it would take to read (approx) in minutes


'''

def test_diaryentry_reading_time():
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second dairy entry, nice!")
    assert diary_entry_2.reading_time(1) == 7

'''

given a different diary entry
return the time (int) it would take to read (approx) in minutes


'''

def test_diaryentry_reading_time_with_new_parameters():
    diary_entry_2 = DiaryEntry("Second Entry", "This is the second dairy entry, nice!")
    assert diary_entry_2.reading_time(4) == 2

'''

#reading_chunk is a method that will return the amount of words that a user can read in a specified time frame. Its passed the arguments wpm and minutes (the speed at which a user can read and the time the user has) and should return a "chunk" of text in string format.

'''

def test_reading_chunk_small():
    my_diary = DiaryEntry("A title", "These are the contents")
    result = my_diary.reading_chunk(4, 1)
    assert result == "These are the contents"

def test_reading_chunk_bigger():
    another_diary = DiaryEntry("Another Diary", "These are also the contents")
    result = another_diary.reading_chunk(5, 1)
    assert result == "These are also the contents"

def test_reading_chunk_sequentially():
    new_diary = DiaryEntry("Big book", "Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor. Eagerly I wished the morrow; vainly I had sought to borrow From my books surcease of sorrow sorrow for the lost Lenore For the rare and radiant maiden whom the angels name Lenore Nameless here for evermore.")
    result = new_diary.reading_chunk(5, 1)
    assert result == "Ah, distinctly I remember it"
    result = new_diary.reading_chunk(5,1)
    assert result == "was in the bleak December;"
    
def test_reading_chunk_refresh():
    new_diary = DiaryEntry("Big book", "Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor. Eagerly I wished the morrow; vainly I had sought to borrow From my books surcease of sorrow sorrow for the lost Lenore For the rare and radiant maiden whom the angels name Lenore Nameless here for evermore.")
    new_diary.reading_chunk(29,2)
    result = new_diary.reading_chunk(5,1)
    assert result == "Ah, distinctly I remember it"

def test_reading_chunk_repeat():
    newest_diary = DiaryEntry("Small book", "This is a small amount of text")
    result = newest_diary.reading_chunk(14,1)
    assert result == "This is a small amount of text"