def countSegments(s: str) -> int:
    if len(s.replace(" ", "")) <= 0:
        return 0

    res = []
    for word in s.split(" "):
        if len(word) > 0:
            res.append(word)
    return len(res)


s = "Of all the gin joints in all the towns in all the world,   "
print(f"countSegments: {countSegments(s=s)}")
