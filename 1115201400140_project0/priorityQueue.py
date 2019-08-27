import heapq

class Priorityqueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item ,priority):
     	entry=[priority,item]
        heapq.heappush(self.heap,entry)
        self.count=self.count + 1

    def pop(self):
     	self.count=self.count - 1
        return heapq.heappop(self.heap)[1]

    def isEmpty(self):
        return self.heap == []

    def update(self , item , priority):
    	entry=[priority,item]
    	flag=0
    	for i in range(self.count):
	    	if entry[1] in self.heap[i][1]:
	    		flag=1
	    		print "exists"
	    		if(self.heap[i][0] > priority):
	    			self.heap[i][0] = priority
	    			heapq.heapify(self.heap)
	    			break;
		if (flag == 0):
			self.push(item,priority)

def PQsort(List):
	q=Priorityqueue()
	for x in List:
		q.push(x,x)
	return [q.pop() for i in range(len(List))]


if __name__ == '__main__':
	input=[1,32,7,9,23,54]
	result= PQsort(input)
	print "before:" , input 
	print "after:" , result
	q=Priorityqueue()
	q.push("task1", 1)
	q.push("task1", 2)
	q.push("task0", 0)
	print q.heap
	t=q.pop()	
	print t
	print q.heap
	t=q.pop()
	print t
	q.push("task3", 3)
	q.push("task3", 4)
	q.push("task2", 0)
	print q.heap
	t=q.pop()
	print t
	q.push("task4",1)
	print q.heap
	q.update("task4",7)
	print q.heap

