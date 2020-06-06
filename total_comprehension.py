# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here


mapped_list = [i * 100 for i in my_numbers]
print("--------------")
print("MAPPED LIST:", mapped_list)

filtered_list = list(filter(lambda i: i>3, my_numbers))
print("--------------")
print("FILTERED LIST W/ MATCHES:", filtered_list)

no_matches = [i for i in my_numbers if i>7]
print("--------------")
print("FILTERED LIST W/O MATCHES:", no_matches)

mapped_and_filtered = [i * 100 for i in my_numbers if i>3]
print("--------------")
print("MAPPED AND FILTERED LIST", mapped_and_filtered)
