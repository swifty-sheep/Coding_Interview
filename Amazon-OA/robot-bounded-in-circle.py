"""
1041. Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/
"""


class Solution:
    @staticmethod
    def is_robot_bounded(instructions: str) -> bool:
        facing_direction = {
            "n": [0, 1],
            "e": [1, 0],
            "s": [0, -1],
            "w": [-1, 0],
        }
        next_left_direction = {
            "n": "w",
            "e": "n",
            "s": "e",
            "w": "s",
        }
        next_right_direction = {
            "n": "e",
            "e": "s",
            "s": "w",
            "w": "n",
        }
        current_facing = "n"
        current_position = [0, 0]

        for i in range(len(instructions)):
            if instructions[i] == "G":
                go = facing_direction[current_facing]
                current_position[0] += go[0]
                current_position[1] += go[1]
            elif instructions[i] == "L":
                current_facing = next_left_direction[current_facing]
            elif instructions[i] == "R":
                current_facing = next_right_direction[current_facing]

        if current_facing == "n" and current_position != [0, 0]:
            return False
        return True

    def not_my_solution_but_cool(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "G":
                x, y = x + dx, y + dy
            elif i == "L":
                dx, dy = -dy, dx
            elif i == "R":
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


def main():
    instructions = "GGLLGG"
    sol = Solution()
    result = sol.is_robot_bounded(instructions=instructions)
    print(result)
    another_result = sol.not_my_solution_but_cool(instructions)
    print(another_result)


# Driver Code
if __name__ == "__main__":
    main()
