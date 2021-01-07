# 变位词检测
# 例如：heart和earth、 python和typhoon


def anagram_detect(s1, s2):
    list_s1 = [0] * 26
    list_s2 = [0] * 26
    for i in s1:
        index = ord(i) - ord('a')
        list_s1[index] += 1
    for i in s2:
        index = ord(i) - ord('a')
        list_s2[index] += 1
    is_anagram = True
    for i in range(26):
        if list_s1[i] != list_s2[i]:
            is_anagram = False
            break
    return is_anagram


if __name__ == '__main__':
    print(anagram_detect('apple', 'plap'))
    print(anagram_detect('python', 'typhon'))
