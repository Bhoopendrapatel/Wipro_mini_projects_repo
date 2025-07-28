scores = [2,3,6,6,5]
max_score = max(scores)

filtered_score = [score for score in scores if score != max_score]
runner_up = max(filtered_score)
print(runner_up)