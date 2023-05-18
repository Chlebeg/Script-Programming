# file = open("file.py", "r")
# file_data = file.readlines()
# print(file_data)
# file.close()
#
# for line in file_data:
#     position = file_data.index(line)
#     line = "A"
#     file_data[position] = line
#
# print(file_data)

import re

line = "             asad       sd    dew"

print(re.findall(r"[^\s].*", line))