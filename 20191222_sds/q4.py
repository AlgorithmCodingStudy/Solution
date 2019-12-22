t = int(input())
case = []

for _ in range(t):
    n = int(input())
    computers = list(map(int, input().split()))
    case.append(computers)


def get_lengths(coms):
    visit_coms = [False for _ in range(len(coms))]
    length = 0
    networks = 0
    for i in range(len(coms)-1, -1, -1):
        if coms[i] == 1:
            j = 0
            idx = 1
            same_network = False
            while j < 5:
                if i-idx < 0: break
                if coms[i-idx] == 0:
                    length += idx
                    if not visit_coms[i-idx]:
                        visit_coms[i-idx] = True
                    else:
                        same_network = True
                    j += 1
                idx += 1
            if not same_network:
                networks += 1
    for i, v in enumerate(coms):
        if v == 0 and visit_coms[i] == False:
            networks += 1
    return length, networks


for a, c in enumerate(case):
    print("#{} {} {}".format(a+1, *get_lengths(c)))