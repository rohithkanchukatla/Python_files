import sys

file=open("todo_data.txt",'r')
todos=file.readlines()
file.close()

# print(todos)


#editting the file
if len(sys.argv)>=3 and sys.argv[1].lower()=="add":
    todos.append(f'{sys.argv[2]}\n')
    
# print(todos)


# file.write("todo_data.txt")

#remove something from To_do_list
if len(sys.argv)>=3 and sys.argv[1].lower()=="remove":
    try:
        index_to_del=int(sys.argv[2])
        if index_to_del<=len(sys.argv):
            todos.pop(index_to_del)
        print(todos)
    except Exception as e:
        print(e)
        sys.exit(1)
        

file=open("todo_data.txt",'w')
file.writelines(todos)
file.close()