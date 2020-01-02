import random
import itertools


def random_pick_prob(sequence, probabilities):
    rnd = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(sequence, probabilities):
        cumulative_probability += item_probability
        if rnd < cumulative_probability:
            break
    return item


def random_pick_freq(sequence, freqs):
    # print(sequence,freqs)
    # sequence_new = [z for x, y in zip(sequence, freqs) for z in [x] * int(y)]
    sequence_new = []
    for x, y in zip(sequence, freqs):
        # print([x] * int(y))
        for z in[x] * int(y):
            # print(z)
            sequence_new.append(z)
    # for a in sequence_new:
    #     print(a)
    while True:
        yield random.choice(sequence_new)


def random_pick_freq_2(sequence, freqs):
    sequence_new = [z for x, y in zip(sequence, freqs) for z in [x] * int(y)]
    while True:
        yield random.choice(sequence_new)


def test_random_pick_prob():
    num = 100000
    a = [1, 2, 3, 4]
    b = [0.1, 0.2, 0.3, 0.4]
    ree = dict(zip(a, [0]*4))
    for x in range(num):
        result = random_pick_prob(a, b)
        ree[result] += 1
    for v, value in ree.items():
        ree[v] = float(value)/num
    print(ree)


def test_random_pick_freq():
    x = random_pick_freq(["bueno","buebo","bueni","bieno"], [22408, 1039, 935, 930])
    # print(x)
    # print(itertools.islice(x, 8).__next__())
    print(''.join(itertools.islice(x,1)))

    result = ''.join(itertools.islice(x, 100000))
    c = result.count('bueno')
    i = result.count('buebo')
    a = result.count('bueni')
    o = result.count('bieno')
    min_ = min(c, i, a, o)
    print(float(c)/min_, ':', float(i)/min_, ':', float(a)/min_, ':', float(o)/min_, end=" this is end")


if __name__ == "__main__":
    # test_random_pick_prob()
    test_random_pick_freq()
