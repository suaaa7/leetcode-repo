class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        solution = []
        self.letter_combinations_helper(digits, '', solution)
        return solution

    def letter_combinations_helper(
        self,
        digits: str,
        current_str: str,
        solution: List[str]
    ) -> None:
        if len(digits) == 0:
            solution.append(current_str)
            return
        
        possible_chars = self.digit_to_letters(digits[0])
        for char in possible_chars:
            current_str += char
            self.letter_combinations_helper(digits[1:], current_str, solution)
            current_str = current_str[:-1]

    @staticmethod
    def digit_to_letters(digits: str) -> str:
        letters_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        return letters_dict[digits]
