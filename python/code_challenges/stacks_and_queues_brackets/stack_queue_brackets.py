from code_challenges.stacks_and_queues.stack import Stack


def multi_bracket_validation(string):
    brackets = {')': '(', ']': "[", '}': '{'}
    stack = Stack()
    for x in string:
        if x in brackets.values():
            stack.push(x)
        elif x in brackets.keys():
            if stack.top:
                if stack.pop() != brackets.get(x):
                    return False
            else:
                return False
    if stack.top:
        return False
    return True

