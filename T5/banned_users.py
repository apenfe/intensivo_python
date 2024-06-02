banned_users = ['andrew','carolina','david']

user='maria'

if user not in banned_users:
    print(f'{user.title()}, puedes realizar una publicación')

user='Carolina'
user=user.lower()

if user in banned_users:
    print(f'{user.title()}, NO puedes realizar una publicación')