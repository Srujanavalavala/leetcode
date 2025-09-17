class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if(len(st)==0):
                    return False
                ch2=st.pop()
                if ch==")":
                    if ch2=="(":
                        continue
                    else:
                        return False
                elif ch=="]":
                    if ch2=="[":
                        continue
                    else:
                        return False
                else:
                    if ch2=="{":
                        continue
                    else:
                        return False
        if len(st)==0:
            return True
        else:
            return False