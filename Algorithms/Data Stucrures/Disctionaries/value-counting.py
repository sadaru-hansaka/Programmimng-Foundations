items = ["apple","orange","grapes","banana","pineapple","pears",
         "banana","pineapple","pears","orange","grapes",
         "apple","orange","grapes","banana","pineapple"]

counter = dict()

for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)