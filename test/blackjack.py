import itertools
from itertools import combinations
def getSafeProbability(initial_cards, take_num_cards):
    # Write your code here
    # 2+6+10 must be safe 50/50 (if X*10< remain: 100.000000
    # if X*1> remain: 0.000000) base case
    # 10+8+(1?2?3) 3*4/50
    # 10+8+(card_1 choose1 + card_2 choose1) /50
    # count the value of initial cards
    card_0 = {"2.0": 2, "3.0": 3, "4.0": 4, "5.0": 5, "6.0": 6, "7.0": 7, "8.0": 8, "9.0": 9, "10.0": 10, "A.0": 1,
              "J.0": 10, "Q.0": 10, "K.0": 10}
    card_1 = {"2.1": 2, "3.1": 3, "4.1": 4, "5.1": 5, "6.1": 6, "7.1": 7, "8.1": 8, "9.1": 9, "10.1": 10, "A.1": 1,
              "J.1": 10, "Q.1": 10, "K.1": 10}
    card_2 = {"2.2": 2, "3.2": 3, "4.2": 4, "5.2": 5, "6.2": 6, "7.2": 7, "8.2": 8, "9.2": 9, "10.2": 10, "A.2": 1,
              "J.2": 10, "Q.2": 10, "K.2": 10}
    card_3 = {"2.3": 2, "3.3": 3, "4.3": 4, "5.3": 5, "6.3": 6, "7.3": 7, "8.3": 8, "9.3": 9, "10.3": 10, "A.3": 1,
              "J.3": 10, "Q.3": 10, "K.3": 10}

    init_value = 0
    for card_i in initial_cards:
        print(card_i)
        if card_i + '.0' in card_0.keys():
            print(0)
            init_value += card_0[card_i + '.0']
            del card_0[card_i + '.0']
        elif card_i + '.1' in card_1.keys():
            print(1)
            init_value += card_1[card_i + '.1']
            del card_1[card_i + '.1']
        elif card_i + '.2' in card_2.keys():
            print(2)
            init_value += card_2[card_i + '.2']
            del card_2[card_i + '.2']
        else:
            init_value += card_3[card_i + '.3']
            del card_3[card_i + '.3']

    cards_pool = dict(card_0.items() | card_1.items() | card_2.items() | card_3.items())
    card_list = list(cards_pool.values())
    card_list.sort()

    # find all possibilities
    comb = list(combinations(card_list, take_num_cards))
    count_all = len(comb)

    # find correct possibilities
    remain_sum = 21 - init_value
    count_correct = 0
    for c in comb:
        if sum(c) <= remain_sum:
            count_correct += 1
        else:
            break

    possibility = count_correct / count_all
    return ("{:.6}".format(round(possibility, 2)))


if __name__ == '__main__':
    a = getSafeProbability(["A","8"],2)
    print(a)