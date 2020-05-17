# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
num_rows = int(input())
rate = [[0] * num_items for _ in range(num_users)]
for _ in range(num_rows):
    x, y, v = map(float, input().split())
    rate[int(x) - 1][int(y) - 1] = v

num_reco_users = int(input())
for _ in range(num_reco_users):
    target = int(input()) - 1
    rate_target = rate[target]
    sim_user = []
    sim_group = []
    for i, user in enumerate(rate):
        if i == target: continue
        s1 = sum(map(lambda x, y: x * y, rate_target, user))
        s2 = sum(map(lambda x: x * x, rate_target)) ** 0.5
        s3 = sum(map(lambda x: x * x, user)) ** 0.5
        simil = s1 / (s2 * s3)
        if len(sim_user) < num_sim_user_topk:
            sim_user.append((simil, i))
            sim_group.append(i)
        else:
            sim_user.sort()
            if sim_user[0][0] < simil:
                sim_user[0] = (simil, i)
                sim_group[0] = i

    sim_user.sort()


    recommend_rate = [-10000000] * num_items
    re_can = set()
    for s_user in sim_group:
        for i, v in enumerate(rate[s_user]):
            if v != 0:
                re_can.add(i)

    for i in re_can:
        simil_rate_sum = 0
        for who_simil, u in sim_user:
            if rate[u][i] == 0: continue
            cnt = 0
            for v in rate[u]:
                if v != 0:
                    cnt += 1
            simil_rate_sum += who_simil * (rate[u][i] - sum(rate[u]) / cnt)
        k = 0
        for who_simil, u in sim_user:
            if rate[u][i] == 0: continue
            k += who_simil
        if k != 0:
            k = 1 / k
        simil_rate_sum *= k
        cnt = 0
        for v in rate_target:
            if v != 0:
                cnt += 1
        simil_rate_sum += sum(rate_target) / cnt
        recommend_rate[i] = simil_rate_sum

    result = []
    while len(result) != num_item_rec_topk:
        max_v, max_idx = -1000000, -1
        for j, v in enumerate(recommend_rate):
            if v > max_v:
                max_v = v
                max_idx = j
        recommend_rate[max_idx] = -1000000
        if rate_target[max_idx] != 0:
            continue
        result.append(max_idx+1)
    print(" ".join(map(str, result)))