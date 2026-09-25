class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * (len(temperatures))
        for i in range(len(temperatures)):
            current_temperature = temperatures[i]
            while stack and current_temperature > stack[-1][0]:
                previous_temperature, previous_index = stack.pop()
                result[previous_index] = i - previous_index
            stack.append((current_temperature, i))
        return result
