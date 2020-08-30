import math
list_a = [5, 10, 11, 13, 15]
list_b = [35, 50, 55, 72, 92]


def get_mse(mylist):
    mse_dict = {}

    for x in range(mylist[0], mylist[len(mylist)-1]):
        mse = 0
        for a in mylist:
            mse += abs(a-x)*abs(a-x)
        mse = math.sqrt(mse)
        mse_dict[x] = mse

    print("The mse of every number is")
    print(mse_dict)
    min_mse = min(mse_dict.values())
    min_key = [key for key in mse_dict if mse_dict[key] == min_mse]
    print("The number with minimum mse is{}".format(min_key))

get_mse(list_a)
print("\n")
get_mse(list_b)
print("\n")
get_mse([204, 215])