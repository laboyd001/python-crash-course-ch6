# add 3 dictionaries of people.  loop through the list.  print everything you know abou the person.

people = {
    'person1': {
        'first_name': 'jenn',
        'last_name': 'kuhlman',
        'city': 'nashville',
        },
    'person2': {
        'first_name': 'kathy',
        'last_name': 'boyd',
        'city': 'owensboro',
        },
    'person3': {
        'first_name': 'jeane',
        'last_name': 'phillips',
        'city': 'fordsville',
        },
}

for key, value in people.items():
    print("\n" + key.title() + ":")
    full_name = value['first_name'] + " " + value['last_name']
    city = value['city']

    print("\tFull name: " + full_name.title())
    print("\tCity: " + city.title())
