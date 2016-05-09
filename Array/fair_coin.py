# Question: Write code to generate a fair coin from a biased one.

def fairCoin():
    a = biasFlip()
    b = biasFlip()
    if a != b:
        return a
    return fairCoin()
