from functools import reduce
num=[1,2,3,4,5]


#map_results=(list(map(lambda number:number*2,num)))



#filter_results = list(filter(lambda number: number % 2 == 0, num))

#print(filter_results)

reduce_results=reduce(lambda total,number:number+total,num,0)

print(reduce_results)
