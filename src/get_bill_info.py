def get_bill_info(data_from=None):
    cart = ''
    if data_from and len(data_from.split()) == 2:
        from_account, account_number = data_from.split()
        if from_account.lower() == 'счет' and len(str(account_number)) == 20:
            account = '*' * (len(account_number) - 4) + account_number[-4:]
            return from_account, account
        elif len(str(account_number)) == 16 and from_account.lower() != 'счет':
            account = account_number[:6] + '*' * (len(account_number) - 6 - 4) + account_number[-4:]
            for i, figure in enumerate(account):
                cart += ' ' + figure if i in [4, 8, 12] else figure
            return from_account, cart
        else:
            return ''
    else:
        return ''