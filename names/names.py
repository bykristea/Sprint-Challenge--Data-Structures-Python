import time
from names_bst import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

bst = BinarySearchTree('duplicated')
# adding names from list names_1 to the bst
for name in names_1:
    bst.insert(name)
# checking all names in list names_2 to see if it exists in the bst. if the bst contains a duplicated name, appended it to the duplicates[] array.
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

## runtime: 0.12141919136047363 seconds NEW ONE ##
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
