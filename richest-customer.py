class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            s=0
            for j in accounts[i]:
                s=j+s
            l.append(s)
        for i in l:
            count=0
            for j in l:
                if i<j:
                    break
                elif i>=j:
                    count=count+1
                    if count==len(l):
                        return i
                        break
