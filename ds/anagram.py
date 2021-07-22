s1 = "bedca"
s2 = "adbec"


def anagram(s1, s2):
    count = 0
    hmap = {}

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count = count + 1

    if count == len(s1):
        return True
    else:
        return False


print(anagram(s1, s2))