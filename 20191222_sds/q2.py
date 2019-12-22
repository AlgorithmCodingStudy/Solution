#-*- coding:utf-8 -*-

t = int(input())
case = [[] for _ in range(t)]
for a in range(t):
    n = int(input())
    prince = []
    for _ in range(n+1):
        prince.append(tuple(map(int, input().split())))
    princess = []
    for _ in range(n + 1):
        princess.append(tuple(map(int, input().split())))
    case[a].append(prince)
    case[a].append(princess)

def make_graph(human):
    for i in range(len(human)):
        if i == 0: continue
        human[i-1][0] - human[i][0]

