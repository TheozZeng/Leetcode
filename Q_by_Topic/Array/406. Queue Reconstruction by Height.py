class Solution:
    def reconstructQueue(self, people):
        num_people = len(people)
        Line = num_people * [None]
        people.sort(key=lambda x: (x[0],x[1]))
        print(people)

        for p in people:
            this_h = p[0]
            num_p_in_front = p[1]
            
            for i in range(num_people):
                p_in_pos = Line[i]
                
                if(num_p_in_front == 0 and p_in_pos == None):
                    Line[i] = p
                    break
                
                elif(p_in_pos == None or p_in_pos[0] >= this_h):
                    num_p_in_front -= 1

            print(Line)
        return Line
        
                
        






people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sol = Solution()
sol.reconstructQueue(people)
