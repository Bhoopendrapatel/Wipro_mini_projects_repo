like_str, dislike_str, received_str = input().split()

like = set(map(int, like_str.split('-')))
dislike = set(map(int, dislike_str.split('-')))
received = list(map(int, received_str.split('-')))

happiness = 0

for num in received:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print(happiness)