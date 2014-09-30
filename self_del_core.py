# main file - include code
###

import os

print 'hello i am self destroyer!!!'
new = open("self_del_cp3.py", "w")

data = "import os\n\nprint 'hello i am self destroyer!!!'\nnew = open('self_del_cp1.py', 'w')\n\nnew.write(data)\n\ncmd='DEL self_del_cp1.py'\nos.system(cmd)"

new.write(data)

cmd = 'DEL self_del_cp1.py'
os.system(cmd)

###

import os

print 'hello i am self destroyer!!!'

cmd = 'DEL self_del_cp1.py'

os.system(cmd)

###