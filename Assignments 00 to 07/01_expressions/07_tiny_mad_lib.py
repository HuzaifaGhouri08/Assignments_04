# Old Assignment

#Scene 1
noun = input("Enter any name: ")
pluralNoun = input("Enter plural noun (e.g: Students, Teachers): ")
place = input("Enter any place in the school: ")

#Scene 2
chemical1 = input("Enter any chemical name: ")
chemical2 = input("Enter another chemical name: ")
color = input("Enter any color: ")

story = f"The principal announced over the intercom that all {pluralNoun} were to report to the {place} for a meeting. " \
        f"Because During the science experiment, {noun} mixed {chemical1} with {chemical2}, causing a {color} explosion. "

#using \n for new line
print("\nHere's your Tiny Mad Libs story:\n")
print(story)