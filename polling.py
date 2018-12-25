#use the code from the favorite_languages exercise
#make a list of people who should take the poll.  include some names that are already in the poll and some that are not.
#loop through the list of people who should take the poll.  if they have already taken the poll print a message thanking them.  if they have not yet taken the poll, ask them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

should_take_poll = ['jen', 'sarah', 'mike', 'sam']

for name in should_take_poll:
    if name in favorite_languages.keys():
        print("Thanks for taking the poll, " + name.title())
    else:
        print(name.title() + ", please take the poll!")