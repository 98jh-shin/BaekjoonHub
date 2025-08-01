result = ""

def akaraka(k, arr):
    if k == 1:
        arr += "AKARAKA"
        return arr

    return akaraka(k - 1, arr) + "RAKA"

print(akaraka(int(input()), result))

