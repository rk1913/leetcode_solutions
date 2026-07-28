class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0
        right = len(people)-1
        mini = 0
        while left <= right:
            if people[left]+people[right] > limit:
                mini +=1
                right -=1
            elif people[left]+people[right] <= limit:
                mini+=1
                left+=1
                right-=1
        return mini        

                
                
        