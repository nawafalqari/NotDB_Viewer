from notdb import NotDBClient
from time import time

client = NotDBClient('t.ndb', '123')

# while True:
   # val = input('> ')

   # if val == 'print':
   #    s = time()
   #    print(client.get({}))
   #    print(time() - s)
   # elif val == 'clear':
   #    s = time()
   #    client.removeMany({})
   #    print(time() - s)
   # else:
   #    s = time()
   #    client.appendOne({'username': val})
   #    print(time() - s)


# isLoggedIn = False
# username = None

# while True:
#    cmd = input('> ').lower().strip()

#    if cmd == 'whoami':
#       if not isLoggedIn:
#          print('Login/Register first')
#       else:
#          print(username)
   
#    elif cmd == 'register':
#       if isLoggedIn:
#          print('You are logged in')
#       else:
#          username = input('username: ').lower()
#          password = input('password: ')
#          client.appendOne({
#             'username': username,
#             'password': password
#          })
#          print('You have registered successfully.')
   
#    elif cmd == 'login':
#       username = input('username: ').lower()
#       password = input('password: ')

#       print({'username': 'nawaf', 'password': '123'})
#       print({'username': username, 'password': password})
#       print({'username': 'nawaf', 'password': '123'} == {'username': username, 'password': password})

#       user = client.getOne({
#          'username': username
#       })

#       print(user)

#       if not user:
#          print('Invalid username or password')
#       else:
#          isLoggedIn = True
#          username = user['username']
      
#    elif cmd == 'logout':
#       isLoggedIn = False
#       username = None