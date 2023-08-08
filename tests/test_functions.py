from arrs.functions import get_data, get_executed_operations, get_recent_five_operations, convert_time, \
    convert_payment_dir
from main import main
from path import PATH_TO_JSON

if __name__ == '__main__':
    main()

def test_get_data():
    assert get_data(PATH_TO_JSON) == list[dict]

def test_get_executed_operations():
    assert get_executed_operations(get_data(PATH_TO_JSON)) == list[dict]

def test_get_recent_five_operations():
    assert get_recent_five_operations(get_executed_operations(get_data(PATH_TO_JSON))) == list[dict][:5]

def test_convert_time():
    assert convert_time('2019-08-26T10:50:58.294041') == '26.08.2019'

def test_convert_payment_dir():
    assert convert_payment_dir("Счет 65298957349197687907") == "6529 89** ***197687907"

