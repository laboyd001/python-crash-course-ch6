#make several dictionaries where the name of the dictionary is the name of the pet. in each dictionary include the kind of animal and the owner's name.  store these dictionaries in a dictionary called pets.  lopp through the dictionary and print everythign you know about the pet

pets = {
    'bt': {
        'name': 'bt',
        'pet_type': 'cat',
        'owner': 'lesley',
        },
    'boba': {
        'name':'boba',
        'pet_type': 'dog',
        'owner': 'rachel',
        },
    'salty': {
        'name': 'salty',
        'pet_type': 'cat',
        'owner': 'kathy',
        },
}

for key, value in pets.items():
    print("\n" + key.title() + ":")
    name = value['name']
    pet_type = value['pet_type']
    owner = value['owner']

    print("\tName: " + name.title())
    print("\tPet Type: " + pet_type.title())
    print("\tOwner: " + owner.title()) 