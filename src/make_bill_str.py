from get_bill_info import get_bill_info


def make_bill_str(info=None):
    if not isinstance(info, dict):
        return ''
    if get_bill_info(info.get('from', '')) and get_bill_info(info.get('to', '')):
        from_account, bill_from = get_bill_info(info.get('from', ''))
        to_account, bill_to = get_bill_info(info.get('to', ''))
        if all([from_account != '', bill_from != '', to_account != '', bill_to != '']):
            return f'{from_account} {bill_from} -> {to_account} {bill_to}'
        else:
            return ''
    else:
        return ''