def make_amount_str(info=None):
    if not isinstance(info, dict):
        return ''
    if info:
        amount = info.get('amount', '')
        name = info.get('currency', {}).get('name', '')
        if amount == '' or name == '':
            return ''
        return f'{amount} {name}'
    else:
        return ''