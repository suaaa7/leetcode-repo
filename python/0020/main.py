class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for i in range(len(s)):
            if self.is_open_paren(s[i]):
                parens.append(s[i])
            else:
                if len(parens) == 0:
                    return False
                op = parens.pop()
                cl = s[i]
                if not self.paren_is_same_type(op, cl):
                    return False

        return len(parens) == 0

    @staticmethod
    def is_open_paren(p: str) -> bool:
        if p in ['(', '[', '{']:
            return True
        return False

    @staticmethod
    def paren_is_same_type(op: str, cl: str) -> bool:
        if op == '(' and cl == ')':
            return True
        elif op == '[' and cl == ']':
            return True
        elif op == '{' and cl == '}':
            return True
        return False
