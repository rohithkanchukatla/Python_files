
import sys

total=1
del(sys.argv[0])
for arg in sys.argv:
    try:
        number=int(arg)
        total*=number
    except Exception as e:
        print(e)
        print("no strings allowed")
    #sys.exit(1)

print(total)