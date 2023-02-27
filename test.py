from collections import deque

def message():
    msg = '$big chungus~is kind of sus'
    msg = msg[1:].split('~')
    if not msg:
        return
    top_text = msg[0]
    if len(msg) > 1:
        bottom_text = msg[1]
    print(top_text)
    print(bottom_text)

dq = deque([])

dq.append(('a', 'b', 'c'))
dq.append(('d', 'e', 'f'))

print(dq)

you_are_up = dq.popleft()
print(you_are_up)
print(dq)


def main():
    pass
    #message()


if __name__ == '__main__':
    main()