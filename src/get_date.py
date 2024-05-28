from datetime import datetime


def get_date(date_str=None):
    if date_str:
        try:
            date = datetime.strptime(date_str.split('T')[0], "%Y-%m-%d")
            day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
            month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
            return f'{day}.{month}.{date.year}'
        except:
            return ''
    else:
        return ''