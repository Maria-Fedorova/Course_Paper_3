from src import utils


def test_load_operations():
    x = utils.load_operations('operations.json')
    assert len(x) != 0
    assert type(x) == list
    assert type(x[0]) == dict


def test_filter_operations():
    x = utils.load_operations('operations.json')
    y = utils.filter_operations(x)
    assert y[0].get('state') == 'EXECUTED'


def test_sort_operations():
    x = utils.load_operations('operations.json')
    y = utils.filter_operations(x)
    z = utils.sort_operations(y)
    assert z[0].get('date') > z[1].get('date')
    assert z[1].get('date') > z[2].get('date')
    assert z[2].get('date') > z[3].get('date')
    assert z[3].get('date') > z[4].get('date')
    assert z[4].get('date') > z[5].get('date')


def test_cut_operations():
    x = utils.load_operations('operations.json')
    y = utils.filter_operations(x)
    z = utils.sort_operations(y)
    k = utils.cut_operations(z)
    assert len(k) <= 5
    assert k[0] == z[0]


def test_formatter_date():
    assert utils.formatter_date('2019-10-14') == '14.10.2019'


def test_mask_account():
    assert utils.mask_account(None) == ('', '')
    assert utils.mask_account('MasterCard 1234567812345678') == ('MasterCard ', '1234 56** **** 5678 ')
    assert utils.mask_account('Счет 12345678123456781234') == ('Счет ', '**1234 ')
