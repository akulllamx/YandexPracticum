# id: 141953242
DIGITS = set("0123456789")

def decode_string(s: str, idx: int = 0) -> tuple[str, int]:
    result: str = ""
    num_str: str = ""
    while idx < len(s):
        if s[idx] in DIGITS:
            num_str += s[idx]
            idx += 1
        elif s[idx] == "[":
            idx += 1
            decoded_string, idx = decode_string(s, idx)
            num = int(num_str) if num_str else 1
            result += decoded_string * num
            num_str = ""
        elif s[idx] == "]":
            idx += 1
            return result, idx
        else:
            result += s[idx]
            idx += 1
    return result, idx

def main_decode(s: str) -> str:
    decoded, _ = decode_string(s)
    return decoded

if __name__ == "__main__":
    compressed_command = input()
    print(main_decode(compressed_command))
