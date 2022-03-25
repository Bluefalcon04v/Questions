"""heroes = ['spider_man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""

heroes = ['spider_man','thor','hulk','iron man','captain america']

 # Length of the list
print(f"length of the list is: {len(heroes)}")

# Add 'black panther' at the end of this list
heroes.append('black panther')
print(f"list after adding new hero in the list: {heroes}")

# You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
heroes.insert(3, 'black panther')
print(f"Inserting black panther after hulk: {heroes}")

# Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
heroes[1:3] = ['doctor strange']
print(f"Removing thor and hulk by adding doctor strange: {heroes}")

# Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""
heroes.sort()
print(f"arranging heroes in alphabetical order: {heroes}")
