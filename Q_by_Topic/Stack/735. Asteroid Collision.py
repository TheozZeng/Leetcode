class Solution:
    def asteroidCollision(self, asteroids):
        Res = []
        for this in asteroids:
            # move right 
            if(this > 0):
                Res.append(this)
                
            # move left
            else:
                has_collision = True
                while(has_collision):
                    #no prev for collision
                    if(len(Res) == 0):
                        has_collision = False
                        Res.append(this)
                        continue
                
                    prev = Res.pop()
                    #prev move left
                    if(prev < 0):
                        has_collision = False
                        Res.append(prev)
                        Res.append(this)
                        continue
                    
                    #prev move right
                    else:
                        if(prev > abs(this)):
                            has_collision = False
                            Res.append(prev)
                        elif(prev == abs(this)):
                            has_collision = False
            print(Res)
        return Res
                            
                            
                        

asteroids = [-2,-1,1,2]
sol = Solution()
print(sol.asteroidCollision(asteroids))
                    
        
