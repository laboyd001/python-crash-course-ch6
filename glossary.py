#use a loop to print out key/value pairs from glossary

glossary = {
    'list': 'A collection of items stored in brackets',
    'dictionary': "Key/ Value pairs stored in curly braces.",
    'tuple': 'A collection of immutable items stored in parenthesis.',
}

for key, value in glossary.items():
    print("\n" + key + " - " + value)
