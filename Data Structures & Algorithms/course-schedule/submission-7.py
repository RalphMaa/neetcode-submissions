class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build adjacency
        prereq = defaultdict(list)
        for i, j in prerequisites:
            prereq[i].append(j)

        visiting = set()
        done = set()

        def has_cycle(course):
            if course in visiting: # Found a cycle
                return True
            
            if course in done: # Already visited -> Has no cycle
                return False
            
            visiting.add(course)
            for p in prereq[course]:
                if has_cycle(p):
                    return True
                
            visiting.remove(course) # Leaving path
            done.add(course) # Save that course was visited and is cycle free

            return False
        
        return not any(has_cycle(c) for c in range(numCourses))
