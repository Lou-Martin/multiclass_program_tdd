from lib.diary import Diary

'''

given no entries (on initialization)
ensure diary entry list is empty

'''

def test_init_list_is_empty():
    diary = Diary()
    assert diary.all() == []