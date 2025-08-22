def is_correct_bracket_seq(seq: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in seq:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or pairs[char] != stack.pop():
                return False

    return stack == []


def main():
    n = str(input())
    print(is_correct_bracket_seq(n))


if __name__ == '__main__':
    main()