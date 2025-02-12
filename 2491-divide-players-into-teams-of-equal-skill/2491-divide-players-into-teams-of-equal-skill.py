class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0 
        right = len(skill) - 1
        sum_chem = 0
        result = 0
        comp = skill[left] + skill[right]

        while left < right:
            team_skill = skill[left] + skill[right]

            if team_skill  != comp:
                return -1
            else:
                result += skill[left] * skill[right]
            left += 1
            right -= 1
        return result

