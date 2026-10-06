revenue = float(input("What is the initial revenue? "))
growth_rate = float(input("What is the growth rate percentage? "))

growth_rate = growth_rate / 100

for year in range(1, 11):
    revenue = revenue + (revenue * growth_rate)

    print("Year", year, "- Revenue: $", round(revenue, 2))