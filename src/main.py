import json
from get_date import get_date
from get_last_five import get_last_five
from make_amount_str import make_amount_str
from make_bill_str import make_bill_str


def main():
    with open('operations.json') as f:
        data = json.load(f)
        last_five = get_last_five(data)
        if last_five is not None:
            for info in last_five:
                if all([get_date(info['date']), make_bill_str(info), make_amount_str(info.get('operationAmount', {}))]):
                    print(get_date(info['date']), info['description'])
                    print(make_bill_str(info))
                    print(make_amount_str(info.get('operationAmount', {})))
                else:
                    print('Недостаточно информации')
        else:
            print('Нет информации')


if __name__ == '__main__':
    main()
