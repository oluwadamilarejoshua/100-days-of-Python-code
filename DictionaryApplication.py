sales_record = {
    'price':  4.56,
    'num_items': 3,
    'person': 'Tumishe'
}

sales_statement = '{} bought {} items for ${} each for a total of ${}'

print(sales_statement.format(sales_record['person'],
                            sales_record['num_items'],
                            sales_record['price'],
                            sales_record['price'] * sales_record['num_items']
                            ))

