# 2325. Decode the Message
# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

#     Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
#     Align the substitution table with the regular English alphabet.
#     Each letter in message is then substituted using the table.
#     Spaces ' ' are transformed to themselves.

#     For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

# Return the decoded message.


def decodeMessage(key: str, message: str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    key_h = []
    message = list(message)

    for i in key.replace(" ", ""):
        if i not in key_h:
            key_h.append(i)

    for id, val in enumerate(message):
        if val in key_h:
            i = key_h.index(val)
            message[id] = alphabets[i]

    return "".join(message)


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decodeMessage(key=key, message=message))
# --
# this is a secret
