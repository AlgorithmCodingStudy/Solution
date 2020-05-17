# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import codecs

# sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import random
import heapq


def shuffle_playlist(playlist, artist):
    length_of_list = len(playlist)

    songs = {}
    for i, who in enumerate(artist):
        if who in songs:
            songs[who].append(playlist[i])
        else:
            songs[who] = [playlist[i]]

    result = []
    for j, who in enumerate(songs.keys()):
        who_list = songs[who]
        random.shuffle(who_list)

        length_of_who = len(who_list)
        if length_of_who > 1:
            step = length_of_list / (length_of_who - 1)
        else:
            step = 0
        distances = [0]*length_of_who
        for i, distance in enumerate(distances):
            distances[i] = i * step + random.random()*0.2 * step
        for i, song in enumerate(who_list):
            heapq.heappush(result, (distances[i], song))

    heap_size = len(result)
    last_result = [heapq.heappop(result)[1] for _ in range(heap_size)]

    return last_result


t = int(input())
for _ in range(t):
    pl = input().strip().split('\t')
    a = input().strip().split('\t')

    playlist_shuffled = shuffle_playlist(pl, a)

    print("\t".join(playlist_shuffled))


