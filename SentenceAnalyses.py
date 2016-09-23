import math

def getTokens(str1):
    tokens = str1.split()
    final_tokens = []
    flag = 0
    for token in tokens:
        for i in range(len(final_tokens)):
            if(final_tokens[i][0] == token):
                final_tokens[i][1] = final_tokens[i][1] + 1
                flag = 1
                
        if(flag == 0):
            final_tokens.append([token, 1])
        else:
            flag = 0
    final_tokens.sort()
    return final_tokens

def tf(S1, S2, total):
    SBag1 = getTokens(S2)
    SBag2 = getTokens(S1)

    freq = 0
    
    for i in range(len(SBag1)):
        for j in range(len(SBag2)):
            if(SBag1[i][0] == SBag2[j][0]):
                freq = freq + SBag2[j][1]
    tfin = (freq / total)
    return tfin * 1000

def idf(S1, nP, paras):
    SBag1 = getTokens(S1)
    freq = 0
    for i in range(len(SBag1)):
        for j in range(len(paras)):
            for k in range(len(paras[j])):
                if(SBag1[i][0].replace('"', '').replace(",", "").replace("'", '').replace('.', '') == paras[j][k].replace('"', '').replace(",", "").replace("'", '').replace('.', '')):
                    freq = freq + 1
                    break
    if freq == 0:
        return 0
    else:
        if(nP/freq != 0):
            idfin = -math.log(nP/freq)
        else:
            return 0;

    return idfin
    
def Partition(A,p,q,index):
    i=p
    x=A[i][index]
    for j in range(p+1,q+1):
        if A[j][index]<=x:
            i=i+1
            tmp=A[j][index]
            A[j][index]=A[i][index]
            A[i][index]=tmp
    l=A[p]
    A[p]=A[i]
    A[i]=l
    return i

def QuickSort(A, p, q, index):
    if p<q:
        r=Partition(A,p,q,index)
        QuickSort(A,p,r-1,index)
        QuickSort(A,r+1,q,index)
    return A
