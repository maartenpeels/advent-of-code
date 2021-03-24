inp = [int(num) for num in list(open('input.txt').readline())]


def run(data, total_needed_cups, loops, calc_score, debug=False):
    cups = CircularLinkedList()
    prev_node = None
    for cup in data:
        prev_node = cups.insert_left(cup, prev_node)
    for i in range(len(data) + 1, total_needed_cups + 1):
        prev_node = cups.insert_left(i, prev_node)

    cur_cup = cups.find(data[0])
    move = 1
    for i in range(loops):
        if i % (loops / 1000) == 0:
            print(f'{round((i / loops) * 100, 2)}%', end='\r')

        in_hand = [cups.pop_right(cur_cup) for _ in range(3)]
        destination_cup = None

        pointer = cur_cup.val - 1
        while destination_cup is None:
            if pointer <= 0:
                pointer = total_needed_cups
            elif pointer in in_hand:
                pointer -= 1
            else:
                destination_cup = cups.find(pointer)

        for cup in in_hand[::-1]:
            cups.insert_left(cup, destination_cup)

        if debug:
            print(f'-- move {move} --')
            print(f'cups: {", ".join([str(x) for x in cups.get_list()])}')
            print(f'pick up: {", ".join([str(x) for x in in_hand])}')
            print(f'destination: {destination_cup.val}')

        del destination_cup

        cur_cup = cur_cup.next

        move += 1

    return calc_score(cups)


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.nodes = {}

    def insert_left(self, val, prev_node=None):
        node = Node(val)
        if prev_node is None:
            node.next = node
            node.prev = node
        else:
            node.prev = prev_node
            node.next = prev_node.next
            node.prev.next = node
            node.next.prev = node

        self.nodes[val] = node
        return node

    def pop_right(self, left_node=None):
        node = left_node.next
        val = node.val

        left_node.next = node.next
        node.next.prev = left_node

        del node
        del self.nodes[val]

        return val

    def find(self, val):
        return self.nodes[val]

    def get_list(self, marker=1, max_length=999999999999999):
        cups = []
        node = self.nodes[marker]
        cups.append(node.val)

        node = node.next
        while node.val != marker:
            cups.append(node.val)
            node = node.next

            if len(cups) >= max_length:
                break

        return cups


def calc_score_p1(cups):
    cups = cups.get_list(1)
    return ''.join(str(x) for x in (cups[cups.index(1) + 1:] + cups[:cups.index(1)]))


def calc_score_p2(cups):
    cup = cups.find(1)
    return cup.next.val * cup.next.next.val


if __name__ == '__main__':
    answer_part1 = run(inp.copy(), 9, loops=100, calc_score=calc_score_p1)
    print(f'Answer for part 1: {answer_part1}')

    answer_part2 = run(inp.copy(), total_needed_cups=1000000, loops=10000000, calc_score=calc_score_p2)
    print(f'Answer for part 2: {answer_part2}')
