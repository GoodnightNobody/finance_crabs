import json


transactions = {}
transactions['transactions_in'] = []
transactions['transactions_in'].append({
                                   'product_name': product_name,
                                   'size': size,
                                   'kilo': kilo,
                                   'price_per_kilo': price_per_kilo,
                                   'alive': alive,
                                   'delivery': delivery,
                                   'cooked': cooked,
                                   'date': date
                               })

with open('transactions.txt', 'w') as outfile:
    json.dump(transactions, outfile)
