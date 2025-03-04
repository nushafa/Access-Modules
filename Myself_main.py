file_read = open('Myself.txt','r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open('Myself.txt','w')
file_write.write("File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr old.")
file_write.close()