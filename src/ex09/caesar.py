import sys

def encode(string, key):
    result = []

    for char in string:
        if "a" <= char <= "z":
            encode_char = chr(
                (ord(char) - ord("a") + key) % 26 + ord("a")
            )
            result.append(encode_char)
        else:
            result.append(char)

    encode_text = "".join(result)
    print(encode_text)

def decode(string, key):
    result = []

    for char in string:
        if "a" <= char <= "z":
            decode_char = chr(
                (ord(char) - ord("a") - key) % 26 + ord("a")
            )
            result.append(decode_char)
        else:
            result.append(char)

    decode_text = "".join(result)
    print(decode_text)

def main():
    mode = sys.argv[1]
    string = sys.argv[2]
    key = int(sys.argv[3])
    if mode == 'encode':
        encode(string, key)
    elif mode == 'decode':
        decode(string, key)
        sys.exit()
    
if __name__ == "__main__":
    main()
          