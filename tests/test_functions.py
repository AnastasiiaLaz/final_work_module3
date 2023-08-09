from arrs.functions import convert_time, \
    convert_payment_dir
from main import main

if __name__ == '__main__':
    main()


def test_convert_time():
    assert convert_time('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_convert_payment_dir():
    assert convert_payment_dir("Счет 38611483061365799794") == "Счет 3861 14** ***9794"
    assert convert_payment_dir("Visa Classic 38611483061365799794") == "Visa Classic 3861 14** ***9794"
    assert convert_payment_dir("Maestro 38611483061365799794") == "Maestro 3861 14** ***9794"
    assert convert_payment_dir(" 38611483061365799794") == " 3861 14** ***9794"
