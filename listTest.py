tasks = [('4R7hQgwD1Rb6fecg4wZ0', 'Task', 26, 8, 2024, 8262024, 'None', 'None', '0000000000', 'None', 'None', 5, 'None'), ('593aw19KkX5DRiL6GXA2', 'lol', 26, 8, 2024, 8262024, 'None', 'Computer Science 1', 'cOspDDRuA7', 'None', 'None', 5, 'None'), ('WZlhiW9k5KYUkwaPQeB6', 'Task', 26, 8, 2024, 8262024, 'None', 'Intro to Discrete Math', 'zvf23WfGGE', 'None', 'None', 5, 'None'), ('2Agvzjcg999w6f3Ya4X5', 'bob', 27, 8, 2024, 8272024, 'None', 'None', '0000000000', 'None', 'None', 5, 'None'), ('678lSf8wHZ9st1W86r8H', 'joe', 28, 8, 2024, 8282024, 'None', 'United States History', 'MID1F240j3', 'None', 'None', 5, 'None'), ('U09ByK5GHYo1as14gg2R', 'coding', 28, 8, 2024, 8282024, 'None', 'Computer Science 1', 'cOspDDRuA7', 'None', 'None', 5, 'None'), ('V742Bu9801OKMCY68v2B', 'lol', 29, 8, 2024, 8292024, 'None', 'Composition 1', 'T6zt2MFk9B', 'None', 'None', 5, 'None'), ('L3xtxV2A72Y7LH07J8sP', 'bob', 30, 8, 2024, 8302024, 'None', 'Intro to Computers', 'QhzTjxmU1N', 'None', 'None', 5, 'None'), ('zg2Nv9T7cvqSkPGnRj01', 'lol', 30, 8, 2024, 8302024, 'None', 'Intro to Computers', 'QhzTjxmU1N', 'None', 'None', 5, 'None')]

dupTask = []

for i in range(len(tasks)):
    counter = 0
    for c in range(len(tasks)):
        if tasks[i][1] == tasks[c][1]:
            counter += 1

    if counter > 1:
        dupTask.append(tasks[i])
print(dupTask)
