
history = [("Jason", "Gideon", -3),
           ("Zac", "Yacob", -3),
           ("Gideon", "Brian", -1),
           ("Cindy", "Gideon", -2),
           ("Darren", "Jason", -5),
           ("Jason", "Vivian", -6)]

history_reverse = [("Gideon", "Jason",  -3),
           ("Yacob", "Zac", -3),
           ("Brian", "Gideon", -1),
           ("Gideon", "Cindy", -2),
           ("Jason", "Darren", -5),
           ("Vivian", "Jason" -6)]


# 存一个新的dictionary 对于每个人存一个 遇见的人的tuple list
# 记录存双向。如果原来的history是有6条记录。那么这里应该有12个tuple。
# {
#   "Jason": [("Vivian", -6), ("Darren", -5),("Gideon", -3)]
#   "Darren": [("Jason", -5)]
#   "Cindy": [("Giden", -2)]
#   "Gideon": [("Cindy", -2),("Brian",-1), ("Jason",  -3)]
#   "Brian": [("Gideon", -1)]
#   "Vivian": [("Jason"), -6]
#   "Yacob": [("Zac",  -3])
#   "Zac" : [("Yacob", -3)]
# }
#

# 第0步：将patient，也就是Jason 放入current_infected_people[]

# 第1步
# 将"Jason"作为key去提取到dictionary那一行的value

# 第2步
# 遍历 Jason的value： [("Vivian", -6), ("Darren", -5),("Gideon", -3)]
# 这里面的三个人，如果(接触时间 - (-7)) > 1: 那么感染， 放入current_infected_people[]
# 这时候 current_infected_people  = ["Jason", "Darren", "Gideon"]
# 将第一个人"Jason"删掉
# 将Jason放入最终的infected_people[]
# 这时 current_infected_people= ["Darren", "Gideon"]；
# 最终的infected_people = ["Jason"]


# 第3步
# 遍历current_infected_people=["Darren", "Gideon"]
# 将"Darren"作为key，去提取到dictionary那一行的value
# 遍历 Darren的value：[("Jason", -5)]；
# 判定：if 这个人不存在于最终的infected_people and 感染时间差 >1，则放入current_infected_people
#                      这里Jason已经存在了，所以不要重复添加

# 将 Darren 从current_infected_people中删掉
# 将 Darren 放入最终的infected_people[]
# 此时 current_infected_people = 【"Gideon"]
# 最终的infected_people = ["Jason", "Darren"]


# 第4步
# 继续遍历 current_infected_people=【"Gideon"]
# 将"Gideon"作为key，去提取到dictionary那一行的value
# 遍历Gideon的value：[("Cindy", -2),("Brian",-1), ("Jason",-3)]；
# 判定：Cindy不存在于infected_people  但 感染时间差 <1, pass
#       Brian不存在于infected_people and 感染时间差 >1, 加入current_infected_people，变为【"Gideon", "Brian"]
#       Jason已经存在于infected_people，pass

# 将 Gideon 从current_infected_people中删掉
# 将 Gideon 放入最终的infected_people[]
# 此时 current_infected_people = 【"Brian"]
# 最终的infected_people = ["Jason", "Darren", "Gideon"]

# 第5步
# 继续遍历 current_infected_people=【"Brian"]
# 将"Brian"作为key，去提取到dictionary那一行的value
# 遍历Brian的value：[("Gideon", -1)]
# 判定：Gideon已经存在于最终的infected_people不需要再添加

# 将 Brian 从current_infected_people中删掉
# 将 Brain 放入最终的infected_people[]
# 此时 current_infected_people = []
# 最终的infected_people = ["Jason", "Darren", "Gideon", "Brain"]

# 第6步
# current_infected_people为空， 循环结束
# return 删掉Jason的infected_people = ["Darren", "Gideon", "Brain"]


def trace_contacts(patient:str, history: list):
    """
    :param patient: (str) the name of a person who just starts to
    develop symptoms on the current date.
    :param history: (list)  list of tuples that stores the meeting history of people in the community.
    :return:
    """
    infected_people = []

    return infected_people
