    #时间 90.58  空间5.15
def restoreIpAddresses(s):
        result = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if len(s) > i + j + k + 3 and int(s[0:i + 1]) <= 255:
                        if i >= 1 and s[0] == '0':
                            continue
                        ans = ""
                        ans += s[0:i + 1]
                        ans += "."
                        if len(s[i + 1:i + 2 + j]) > 0 and int(s[i + 1:i + 2 + j]) <= 255:
                            if j >= 1 and s[i + 1] == '0':
                                continue
                            ans += s[i + 1:i + j + 2]
                            ans += "."
                            if len(s[i + j + 2:i + j + 3 + k]) > 0 and int(s[i + j + 2:i + j + 3 + k]) <= 255:
                                if k >= 1 and s[i + j + 2] == '0':
                                    continue
                                ans += s[i + j + 2:i + j + 3 + k]
                                ans += "."
                                if len(s[i + j + k + 3:]) < 4 and int(s[i + j + k + 3:]) <= 255 and s[
                                                                                                    i + j + k + 3:] != "000" and s[
                                                                                                                                 i + j + k + 3:] != "00":
                                    if len(s[i + j + k + 3:]) > 1 and s[k + i + j + 3] == "0":
                                        continue
                                    ans += s[i + j + k + 3:]
                                    result.append(ans)



        return result
