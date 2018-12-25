#make a dictionary containing three major rivers and the country each river runs through.

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'rhine': 'germany',
}

for key, value in rivers.items():
    print("The " + key.title() + " river runs through " +
        value.title() + ".")

print("\nHere's a list of rivers:")
for river in rivers:
    print(river.title())

print("\nHere are the countries where the rivers flow:")
for country in rivers.values():
    print(country.title())