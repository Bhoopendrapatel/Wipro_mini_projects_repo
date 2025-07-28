from collections import Counter

def find_meeting_details(file_path):
    try_encodings = ['utf-8', 'utf-16', 'latin-1']

    for enc in try_encodings:
        try:
            with open(file_path, 'r', encoding=enc) as file:
                lines = file.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise Exception("Unable to decode file with common encodings.")

    num_lines = len(lines)

    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        hour = num_lines % 12
        meeting_time = f"{hour if hour != 0 else 12} PM"

    words = []
    for line in lines:
        clean_line = ''.join(char if char.isalnum() else ' ' for char in line)
        words.extend(clean_line.lower().split())

    word_counts = Counter(words)
    most_common_word, frequency = word_counts.most_common(1)[0]

    meeting_place = f"{most_common_word.capitalize()} Street"

    return meeting_time, meeting_place, num_lines, most_common_word, frequency


file_path = "io_operations.txt"
time, place, lines, word, count = find_meeting_details(file_path)
print(f"Meeting time: {time}")
print(f"Meeting place: {place}")
print(f"Lines: {lines}, Word: {word}, Count: {count}")