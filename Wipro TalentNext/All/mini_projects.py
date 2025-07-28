

                                            # MODULE -- PYTHON FUNDAMENTALS
        # PROJECT: 1
'''
distance = float(input("How far would you like to travel in miles? "))

if abs(distance) < 3:
    print("I suggest Bicycle to your destination")
elif abs(distance) < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")
'''



     # PROJECT: 2
'''   
cost_per_hour = 0.51
cost_per_day = cost_per_hour*24
cost_per_week = cost_per_day*7
cost_per_month = cost_per_day*30
total_budget = 918
days_with_budget = total_budget/cost_per_day

print("Cost to operate one server per day: $",round(cost_per_day,2))
print("Cost to operate one server per week: $",round(cost_per_week,2))
print("Cost to operate one server per month: $",round(cost_per_month,2))
print("With $918, you can operate one server for",int(days_with_budget),"days")
'''






                                             # MODULE -- DATA STRUCTURE
           # PROJECT: 1
'''
import random

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original List:")
for person, fact in people.items():
    print(f"{person}: {fact}")

jeff_facts = sorted(people.values())
people["Jeff"] = random.choice(jeff_facts)

people["Jill"] = "Can hula dance."

print("\nUpdated List:")
for person, fact in people.items():
    print(f"{person}: {fact}")
'''


         # PROJECT: 2
'''
scores = [2,3,6,6,5]
max_score = max(scores)

filtered_score = [score for score in scores if score != max_score]
runner_up = max(filtered_score)
print(runner_up)
'''


        #PROJECT: 3
'''       
student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

marks = student_marks.get(name)

if marks:
    average = sum(marks) / len(marks)
    print("Average percentage mark:", average)
else:
    print("Student not found.")
'''



          #PROJECT: 4
'''        
text = input("Enter the string: ")
count = text.count("Alex")
print("Output: ",count)
'''




                                    #MODULE -- FUNCTIONS/MODULES/PACKAGES
         # PROJECT: 1
'''        
def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    sorted_colors = '-'.join(color_list)
    return sorted_colors

input1 = "green-red-yellow-black-white".lower()
print(sort_colors(input1))
'''

        #PROJECT: 2
'''      
import string_utils

name = input("Enter a name: ")
print(string_utils.ispalindrome(name))
print(string_utils.count_the_vowels(name))
print(string_utils.frequency_of_letters(name))
'''




                                # MODULE -- COMMAND LINE ARGUMENTS
           #PROJECT: 1
'''
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
'''






                                              #MODULE -- IO OPERATIONS
         #PROJECT: 1
'''        
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
'''









                                               #MODULE -- EXCEPTION HANDLING
        # PROJECT: 1
'''      
def process_purchase_file(filename):
    try:
        with open(filename + ".txt", 'r') as file:
            lines = file.readlines()

        items_purchased = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.lower().startswith("discount"):
                try:
                    discount = int(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            item_name = parts[0]
            item_price = parts[1]

            if item_price.lower() == 'free':
                free_items += 1
            else:
                try:
                    total_amount += int(item_price)
                    items_purchased += 1
                except ValueError:
                    print(f"Invalid price for item: {item_name}")

        final_amount = total_amount - discount

        print(f"Enter the file name: {filename}")
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter file name (without .txt): ")
process_purchase_file(filename)
'''

