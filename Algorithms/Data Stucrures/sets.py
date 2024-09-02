items = ["apple","orange","grapes","banana","pineapple","pears",
         "banana","pineapple","pears","orange","grapes",
         "apple","orange","grapes","banana","pineapple"]

unique_items = set()

for i in items:
    unique_items.add(i)

print(unique_items)


# -----------------------------------------
sentence = "The fucking brown dog jump over the fence."

unique_letters = {c for c in sentence.lower() if c.isalnum()}
print(unique_letters)