class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p_s = []
        times = []

        for i in range(len(position)):
            p_s.append([position[i], speed[i]])

        p_s.sort(key=lambda x: x[0])

        for i in range(len(p_s)):
            times.append((target - p_s[i][0]) / p_s[i][1])

        car_fleet = 0
        p = len(times) - 1
        
        stack = []

        while p >= 0:
            if not stack:
                stack.append(times[p])
                car_fleet += 1
                continue
            
            elif times[p] > stack[-1]:
                stack.append(times[p])
                car_fleet += 1
        
            p -= 1

        return car_fleet
        