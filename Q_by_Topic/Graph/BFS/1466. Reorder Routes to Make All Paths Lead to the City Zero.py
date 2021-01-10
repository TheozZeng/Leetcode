from collections import deque

class Solution:
    def minReorder(self, n, connections):
        # init adj matrix
        all_city = set()
        Forward_D = {} #non_exist edge to [node]
        Reversed_D = {} #existing edge to [node]
        
        for i in connections:
            i0 = i[0]
            i1 = i[1]   
            all_city.add(i0)
            all_city.add(i1)
            if(i0 in Forward_D):
                Forward_D[i0].add(i1)
            else:
                Forward_D[i0] = set([i1])
                
            if(i1 in Reversed_D):
                Reversed_D[i1].add(i0)
            else:
                Reversed_D[i1] = set([i0])
        print(all_city)
        print(Forward_D)
        print(Reversed_D)

        # Use_BFS_Form_Connected_graph_To_City_0
        reachable = set([0])
        visiting_list = deque([0])
        while(visiting_list):
            node = visiting_list.popleft()
            if(node in Reversed_D):
                adj_list = Reversed_D[node]
                for adj_node in adj_list:
                    reachable.add(adj_node)
                    visiting_list.append(adj_node)
        print(reachable)

        #try to attach none reachable node to Connected_graph
        res = 0
        non_reachable = all_city - reachable
        non_reachable = deque(non_reachable)
        print(non_reachable)
        while(non_reachable):
            print(non_reachable)
            node = non_reachable.popleft()
            is_node_reached = False
            # check node already connect to reached
            if(node in Forward_D):
                adj_list = Forward_D[node]
                for adj_node in adj_list:
                    if(adj_node in reachable):
                        reachable.add(node)
                        is_node_reached = True
                        break
                    
            #check by reversing route can connect to reaced
            if(node in Reversed_D and not is_node_reached):
                adj_list = Reversed_D[node]
                for adj_node in adj_list:
                    if(adj_node in reachable):
                        res += 1
                        reachable.add(node)
                        is_node_reached = True
                        break
                    
            # no way to add node to reachable
            if(not is_node_reached):
                non_reachable.append(node)
        return res


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
sol = Solution()
print(sol.minReorder(n, connections))
