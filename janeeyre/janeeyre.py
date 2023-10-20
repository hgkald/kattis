from sys import stdin 
import heapq 

class PriorityQueue: 
    def __init__(self, init=None): 
        self.q = []
        if init: 
            self.push(init)

    def push(self, x): 
        heapq.heappush(self.q, x)

    def pop(self): 
        return heapq.heappop(self.q)

    def first(self): 
        return self.q[0]

    def empty(self): 
        return not self.q

def main():
    n, m, k = [int(i) for i in input().split()] 

    books = PriorityQueue(("Jane Eyre", k))
    newBooks = PriorityQueue()

    for i in range(n): 
        x, book, numPages = stdin.readline().split('"')
        books.push((book, int(numPages))) 

    for i in range(m): 
        time, book, numPages = stdin.readline().split('"')
        newBooks.push((int(time), (book, int(numPages))))

    time = 0 
    janeRead = False 
    while not janeRead:
        while not newBooks.empty(): 
            nextGiftTime = newBooks.first()[0]
            if nextGiftTime <= time:
                books.push(newBooks.pop()[1])
            else:
                break

        nextBook, numPages = books.pop()
        time += numPages 
        if nextBook=="Jane Eyre": 
            janeRead = True 
        
    print(time)
        

if __name__=="__main__": 
    main() 
