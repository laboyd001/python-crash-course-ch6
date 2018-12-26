#a dictionary of similar objects

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

#==================================================
#first way to access value without loop:

# print("Sarah's favorite language is " + 
#     favorite_languages['sarah'].title() +
#     ".")
#===================================================
#Now using a loop with item method

# for name, language in favorite_languages.items():
    # print(name.title() + "'s favorite language is " +
    #     language.title() + ".")
#====================================================
#keys method

# for name in favorite_languages.keys():
    # print(name.title())

#default behavior is keys method:

# for name in favorite_languages:
    # print(name.title())
#=================================================== friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
    # print(name.title())

    # if name in friends:
        # print(" Hi " + name.title() +
        #     ", I see your favorite language is " +
        #     favorite_languages[name].title() + "!")
# if 'erin' not in favorite_languages.keys():
        # print("Erin, please take our poll!")

#===================================================
#sorted dictionary

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll!")

#===================================================
#values method:

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

#====================================================
#printing unique values using set:

# for language in set(favorite_languages.values()):
#     print(language.title())

#====================================================
#Nesting lists in dictionaries


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


