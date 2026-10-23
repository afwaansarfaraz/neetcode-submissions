class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Collision: right-moving asteroid meets left-moving asteroid
            while stack and stack[-1] > 0 and asteroid < 0:

                # Current asteroid is bigger, so destroy the last one
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                # Same size: both asteroids explode
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    asteroid = 0
                    break

                # Last asteroid is bigger, so current asteroid explodes
                else:
                    asteroid = 0
                    break

            # Add only if the asteroid survived
            if asteroid != 0:
                stack.append(asteroid)

        return stack