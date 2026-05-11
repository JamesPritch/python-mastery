total_cost = 0.0
# with open('Python_mastery/Data/portfolio3.dat', 'r') as f:
#     for line in f:
#         number = int(line.split()[1])
#         price = float(line.split()[2])
#         total_cost += number*price
# print(total_cost)

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'r') as f:
        for line in f:
            try:
                number = int(line.split()[1])
                price = float(line.split()[2])
                total_cost += number*price
            except ValueError as e:
                print("Couldn't parse", repr(line))
                print("Reason:", e)
    return total_cost

if __name__ == '__main__':
    # Running as main program
    print(portfolio_cost('/data/home/james.pritchard/Python_mastery/Data/portfolio.dat'))