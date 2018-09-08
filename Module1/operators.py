total = 50
country = 'au'
if country == 'us':
    if total <= 50:
        print('shipping cost is $50')
    elif total <= 100:
        print('shipping cost is $25')
    elif total <= 5:
        print('shipping cost is $5')
    else:
        print('the shipping cost is free')


if country == 'au':
    if total <= 50:
        print('shipping cost is $100')
    else:
        print('free')
