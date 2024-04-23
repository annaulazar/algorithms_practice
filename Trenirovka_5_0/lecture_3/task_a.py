n = int(input())
k = int(input())
songs = set(input().strip().split())
for _ in range(n - 1):
    k_temp = int(input())
    temp_songs = set(input().strip().split())
    songs.intersection_update(temp_songs)
print(len(songs))
print(' '.join(sorted(songs)))
