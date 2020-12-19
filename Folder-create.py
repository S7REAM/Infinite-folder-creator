import os
p = 1
u = 1
current_directory = os.getcwd()
name = input("what is it called")
while p == 1:
 u = u + 1
 current_directory = os.getcwd()
 final_directory = os.path.join(current_directory, name + str(u))
 if not os.path.exists(final_directory):
   os.makedirs(final_directory)
   name = name 
   
   
