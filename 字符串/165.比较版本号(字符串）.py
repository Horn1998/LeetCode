#time 99 room 5.6
class Solution:
    def compareVersion(self, version1, version2) :
        version1 =[int(i) for i in version1.split('.')]
        version2 =[int(i) for i in version2.split('.')]
        Min = min(len(version1), len(version2))
        for i in range(Min):
            if version1[i] > version2[i]:
                return 1
            elif version2[i] > version1[i]:
                return -1
        #如果前一部分两个版本完全相同
        if len(version1) > len(version2):
            for i in range(Min,len(version1)):
                if version1[i] != 0:
                    return 1
            return  0
        elif len(version2) > len(version1):
            for i in range(Min, len(version2)):
                if version2[i] != 0:
                    return -1
            return 0
        else:
            return 0