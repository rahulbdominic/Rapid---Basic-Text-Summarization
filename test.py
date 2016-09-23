import math
def getTokens(str1):
    tokens = str1.split()
    print(tokens)
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
    SBag1 = getTokens(S1)
    SBag2 = getTokens(S2)

    freq = 0
    
    for i in range(len(SBag1)):
        for j in range(len(SBag2)):
            if(SBag1[i][0] == SBag2[j][0]):
                freq = freq + SBag2[j][1]
    tfin = (freq / total)
    return tfin

def idf(S1, nP, paras):
    SBag1 = getTokens(S1)
    freq = 0
    for i in range(len(paras)):
        paras[i] = paras[i].split()
    for i in range(len(SBag1)):
        for j in range(len(paras)):
            for k in range(len(paras[j])):
                print(SBag1[i][0] + " " + paras[j][k])
                if(SBag1[i][0] == paras[j][k]):
                    freq = freq + 1
                    break
    idfin = -math.log(nP/freq)
    return idfin

S1 = "Sullivan joins Uber from Facebook, where he worked at the social network's Chief Security Officer for more than five years. On a blog post announcing the new hire, Uber CEO Travis Kalanick said Sullivan will join the transportation startup toward the end of April."
S2 = "Uber snatches its first chief security officer away from Facebook"
paras = ["Uber on Thursday announced that it had hired Joe Sullivan as its first chief security officer.",
"Sullivan joins Uber from Facebook, where he worked at the social network's Chief Security Officer for more than five years. On a blog post announcing the new hire, Uber CEO Travis Kalanick said Sullivan will join the transportation startup toward the end of April.",
"SEE ALSO: Uber passwords from hacked accounts reportedly selling online for $1",
"Before Facebook, Sullivan spent almost seven years at PayPal and eBay. He also worked for the Department of Justice for eight years prosecuting cybercrime.",
"In his own statement, Sullivan wrote that he firmly believes that 'building world-class safety and security are critical' to furthering Uber's mission of 'revolutionizing transportation.'",
"As The New York Times points out, Sullivan is a big hire for Uber. It also underscores just how important security is to the company.",
"Uber handles a ridiculous amount of sensitive information. When you order an Uber, you're offering up your phone number, your name, your credit card information and, even more importantly, your location.",
"With Uber facilitating what it says are 'millions of trips per day,' making sure that kind of sensitive location data is kept secure if going to be incredibly important.",
"And it's not just for passengers. Tens of thousands of individuals drive cars for Uber — their information needs to be secure too. In February, Uber reported that a data breach in 2014 may have compromised sensitive information from more than 50,000 of its drivers.",
"Sullivan is just the latest big-name hire from Uber. Uber has hired away a number of executives away from its competitor in the ride-sharing space, Lyft. Last August, it hired David Plouffe — the guy that ran President Obama's 2008 campaign — as its senior vice president of policy and strategy.",
"In a statement, Sullivan says that 'I look forward to bringing the best practices that I've learned along the way to Uber and doing defining work in bridging the divide between the digital and physical worlds."]
tfn = tf(S1, S2, len(paras))
idfn = idf(S1, 2, paras)

print (0.5 + (tfn * idfn) * 10)
