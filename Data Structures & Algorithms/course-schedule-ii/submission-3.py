class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        visiting = set()
        done = set()
        
        
        valid_path = []
        def has_cycle(course):

            if course in visiting:
                # Has cycle return empty array
                return True
            
            if course in done: 
                # Already Checked + has no cycle
               
                return False


            visiting.add(course)
            for pre in prereq[course]:
                if has_cycle(pre):
                    return True
            
            visiting.remove(course)
            done.add(course)
            valid_path.append(course)

            # No cycle, return the path
            return False
        
        for course in range(numCourses):
            if has_cycle(course) == True:
                return []
                    
        return valid_path



