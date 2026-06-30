from structly.structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

# Print Ticker object
# if __name__ == '__main__':
#     from follow import follow
#     import csv
#     lines = follow('../Data/stocklog.csv')
#     rows = csv.reader(lines)
#     records = (Ticker.from_row(row) for row in rows)
#     for record in records:
#         print(record)

# Print as nice table
if __name__ == '__main__':
    from follow import follow
    import csv
    from structly.tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('../Data/stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    print_table(records, ['name', 'price', 'change'], formatter)
