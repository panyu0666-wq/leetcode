s = input()
t = input()
class solution:
    def isAnagram(self,s:str,t:str)->bool:
        record = [0]*26
        # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
        for i in s:
            record[ord(i)-ord("a")] += 1
        for i in t:
            record[ord(i)-ord("a")] -= 1
        if sum(record) == 0:
            return True
        else:
            return False
ans = solution()
result = ans.isAnagram(s,t)
print(result)
