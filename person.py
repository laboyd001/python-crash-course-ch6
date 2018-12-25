#use a dictionary to store informationa bout a person you know.  Store first name, last name, age, and city.  Print each piece of information.

person = {
    'first_name': 'jenn',
    'last_name': 'kuhlman',
    'city': 'nashville',
}

print("My girlfriend's name is " +
    person['first_name'].title() +
    " " + person['last_name'].title() +
    " she lives in " + person['city'].title() +
    ".")