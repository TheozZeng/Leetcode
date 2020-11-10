from queue import PriorityQueue

intervals = [(0,30),(10,20),(22,60),(40,50)]
def meetingRoom2(intervals):
    if(len(intervals)==0):
        return 0
    
    intervals.sort(key=lambda x:x[0])
    End_time = PriorityQueue()
    End_time.put(intervals[0][1])
    for i in range(1,len(intervals)):
        earliest_end = End_time.get()
        current_start = intervals[i][0]
        current_end = intervals[i][1]
        if(earliest_end > current_start):
            End_time.put(earliest_end)
        End_time.put(current_end)
    return End_time.qsize()
        
print(meetingRoom2(intervals))  
    
    
