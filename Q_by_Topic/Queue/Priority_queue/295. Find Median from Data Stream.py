from Queue import PriorityQueue

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller_half = PriorityQueue() #max heap
        self.larger_half = PriorityQueue()  #min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.smaller_half.put(-num)
        max_in_smaller_half = - self.smaller_half.get()
        self.larger_half.put(max_in_smaller_half)
        
        if(self.smaller_half.qsize() < self.larger_half.qsize()):
            n = self.larger_half.get() #n is neg
            self.smaller_half.put(-n)
            
        

    def findMedian(self):
        """
        :rtype: float
        """
        if(self.smaller_half.qsize() == self.larger_half.qsize()):
            n1 = - self.smaller_half.get()
            n2 = self.larger_half.get()
            self.smaller_half.put(-n1)
            self.larger_half.put(n2)
            return (n1+n2)/2.0
        
        else:
            n = self.smaller_half.get()
            self.smaller_half.put(n)
            return float(-n)
        
