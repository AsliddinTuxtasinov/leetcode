def truncateSentence(s: str, k: int) -> str:
    return " ".join([word for word in s.split(' ')][:k])



s: str = "What is the solution to this problem"
k: int = 4
print(f"truncateSentence: {truncateSentence(s=s, k=k)}")
