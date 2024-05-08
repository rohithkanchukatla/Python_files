# #file=open("hello.txt",'x')
# #file.write("hey man new file")
# #file.close()


# #file=open("hello.txt",'w')
# #file.write("hey this matters")
# #file.close()

# file=open("hello.txt",'a')
# file.write("hey this matters")
# file.close()


file=open("numbers.txt",'r')

lines=file.readlines()
file.close()

for line in lines:
    line*2
    print(lines)


file=open("numbers.txt",'w')
file.writelines(lines)

file.close()




