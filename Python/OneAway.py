# O()
import unittest

def oneEditReplace(string1, string2):
    foundDifference = False;
    for index in range(len(string1)):
        if (string1[index] != string2[index]):
            if (foundDifference):
                return False
            foundDifference = True
    return True

def oneEditInsert(string1, string2):
    index1 = 0
    index2 = 0
    while (index2 < len(string2) and index1 < len(string1)):
        if (string1[index1] != string2[index2]):
            if (index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True
    
def oneEditAwayA(string1, string2):
    if (len(string1) == len(string2)):
        return oneEditReplace(string1, string2)
    elif (len(string2) == (len(string1) + 1)):
        return oneEditInsert(string1, string2)
    elif (len(string2) == (len(string1) - 1)):
        return oneEditInsert(string2, string1)
    return False

def oneEditAwayB(string1, string2):
    if (abs(len(string1) - len(string2)) > 1):
        return False
    
    if (len(string1) < len(string2)):
        s1 = string1
        s2 = string2
    else:
        s1 = string2
        s2 = string1
    
    index1 = 0
    index2 = 0
    foundDifference = False
    while (index2 < len(s2) and index1 < len(s1)):
        if (s1[index1] != s2[index2]):
            if (foundDifference): return False
            foundDifference = True
            if (len(s1) == len(s2)):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True

class Test(unittest.TestCase):
    string1 = 'pale';
    dataT = [('ple'), ('pales'), ('bale')]
    dataF = [('bae'), ('ples')]

    def test(self):
        # true check
        for string2 in self.dataT:
            actualA = oneEditAwayA(self.string1, string2)
            actualB = oneEditAwayB(self.string1, string2)
            self.assertTrue(actualA)
            self.assertTrue(actualB)
        # false check
        for string2 in self.dataF:
            actualA = oneEditAwayA(self.string1, string2)
            actualB = oneEditAwayB(self.string1, string2)
            self.assertFalse(actualA)
            self.assertFalse(actualB)

if __name__ == "__main__":
    unittest.main(exit=False)