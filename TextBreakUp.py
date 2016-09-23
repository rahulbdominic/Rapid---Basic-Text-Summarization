def fromPara(paras):
    text = ""
    for i in paras:
        text = text + " " + i
    return text

def GetSentences(text):
    sentences = text.split('.')
    return sentences

def GenerateWordBag(text):
    tokens = text.split()
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
    
