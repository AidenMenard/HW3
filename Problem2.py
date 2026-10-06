preferences = ["coffee", "tea", "coffee", "soda","tea"
"coffee"]

counts = {}

for product in preferences:
    if product in counts:
        counts[product] = counts[product] + 1
    else:
        counts[product] = 1

total_responses = len(preferences)

for product in counts:
    percent = (counts[product] / total_responses) * 100
    print(product , ":" , round(percent, 2) , "%")
