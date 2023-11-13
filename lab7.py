def task1_1():
    print(f"Task 1.1")
    data = open("text1.txt")
    for i, line in enumerate(data):
        print(line, end='')
    data.close()


task1_1()

import random


def task1_2():
    print(f"\n\nTask 1.2")
    data = open("text1.txt")
    lines = data.readlines()
    print(lines[random.randint(0, len(lines))])


task1_2()


def task1_3():
    print(f"\n\nTask 1.3")
    data = open("text1.txt").read()
    uppercaseCount = 0
    for i in range(0, len(data)):
        if data[i].isupper():
            uppercaseCount += 1
    print(uppercaseCount)


task1_3()


def task2_4():
    print(f"\n\nTask 2.4")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for line in range(0, len(lines)):
        if lines[line][0].upper() != 'D':
            cnt += 1
    print(cnt)


task2_4()


def task2_5():
    print(f"\n\nTask 2.5")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if line[len(line) - 1] == '\n':
            if line[len(line) - 2].upper() == 'F':
                cnt += 1
        else:
            if line[len(line) - 1].upper() == 'F':
                cnt += 1
    print(cnt)


task2_5()


def task2_6():
    print(f"\n\nTask 2.6")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cnt += line.count(" all ") + line.count(" none ") + line.count(" all\n") + line.count(" none\n")
    print(cnt)


task2_6()


def task2_7():
    print(f"\n\nTask 2.7")
    data = open("text1.txt")
    punctuation = ".?!,;:-_'\" "
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    wordsDic = {}
    for i in words:
        for j in i:
            if j in wordsDic:
                wordsDic[j] += 1
            else:
                wordsDic[j] = 1
    print(wordsDic)


task2_7()


def task2_8():
    print(f"\n\nTask 2.8")
    data = open("text1.txt")
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    punctuation = ".?!,;:-_'\" "
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    longestWord = words[0][0]
    for i in words:
        for j in i:
            if len(j) > len(longestWord):
                longestWord = j
    print(longestWord)


task2_8()


def task3_9():
    print(f"\n\nTask 3.9")
    data = open("text1.txt").read()
    data = data.replace('B', 'J')
    data = data.replace('b', 'j')
    print(data)


task3_9()


def task3_10():
    print(f"\n\nTask 3.10")
    data = open("text1.txt")
    lines = data.readlines()
    cntA = 0
    cntB = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cntA += line.count('a')
        cntB += line.count('b')
    print(f"a={cntA}, b={cntB}")


task3_10()
