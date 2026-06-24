from cofollow import consumer, receive

@consumer
def print_ints():
    while True:
        val = yield from receive(int)
        print('Got:', val)

if __name__ == '__main__':
    p = print_ints()
    p.send(42)
    p.send(3)
    p.send(4.2)
    p = print_ints() # Once broken, needs redefining
    p.send(4)
    p.send('four')
