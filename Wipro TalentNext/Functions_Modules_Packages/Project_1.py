def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    sorted_colors = '-'.join(color_list)
    return sorted_colors

input1 = "green-red-yellow-black-white".lower()
print(sort_colors(input1))