users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for foo in users.keys():
	print(foo)
	nn = 1
	for bar in users[foo]:
		chsum = 0
		fn = bar["first_name"]
		ln = bar["last_name"]
		chsum += len(fn)
		chsum += len(ln)
		print(str(nn) + " - " + fn + " " + ln + " - " + str(chsum))
		nn += 1