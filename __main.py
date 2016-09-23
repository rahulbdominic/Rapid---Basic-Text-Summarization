from WebCrawl import crawl
from TextBreakUp import GetSentences, GenerateWordBag, fromPara
#from Analyses import NormalizeSentences
from SentenceAnalyses import tf, idf, QuickSort
from ExportJSON import export

'''
def getMaxFreq(text):
    tokens = str1.split()
    print(tokens)
    final_tokens = []
    flag = 0
    for token in tokens:
        for i in range(len(final_tokens)):
            print(token + " " + final_tokens[i][1])
            if(final_tokens[i][1] == token):
                final_tokens[i][0] = final_tokens[i][0] + 1
                flag = 1
                
        if(flag == 0):
            final_tokens.append([1, token])
        else:
            flag = 0
    final_tokens.sort()
    
    return final_tokens[0][0]
'''

#Get data from crawler
def main(source, url):
    data = crawl(url, source)
    title = data[0]
    paras = data[1]
    nP = data[2] - 1

    for i in range(len(paras)):
        if "See also" in paras[i]:
            paras.pop(i)
            break

    '''
    title = "Uber snatches its first chief security officer away from Facebook"
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
    nP = 10
    '''
    #Sentencize and Tokenize
    text = fromPara(paras)
    sentences = GetSentences(text)
    word_bag = GenerateWordBag(text)

    #Normalize sentences to title
    #normalized_sentences = NormalizeSentences(sentences)

    definate = []

    i = 0
    noL = 0


    for i in range(len(paras)):
        paras[i] = paras[i].split()

    #Get Definate
    for sentence in sentences:
        if(not "Image:" in sentence):
            tfn = tf(sentence, title, len(text))
            idfn = idf(sentence, nP, paras)
            result_f = 0.5 + (10 * (tfn) * (idfn))

            definate.append([sentence, result_f, noL + 1])
            noL = noL + 1

    #.......definate1 = LingusticAnalysis(definate1)
    #.......definate2 = LingusticAnalysis(definate2)

    final = []
    intermediate = []

    i = 0
    j = 0

    final = QuickSort(final, 0, len(final) - 1, 1)
    for sentence in definate:
        if (i <= 2):
            final.append(sentence)
        else:
            intermediate.append(sentence)
        i = i + 1

    #Use these as base wrt others
    for sentence in definate:
        j = 0
        for sentence2 in intermediate:
            tfn = tf(sentence[0], sentence2[0], len(text))
            idfn = idf(sentence2[0], nP, paras)
            result_f = 0.5 + ((tfn) * (idfn) * 10)

            intermediate[j][1] = (intermediate[j][1] + result_f)/2
            j = j + 1
        i = i + 1

    #Sort
    intermediate = QuickSort(intermediate, 0, len(intermediate) - 1, 1)

    if(noL < 5):
        for k in range(int(noL/2) - 1):
            final.append(intermediate[k])
    else:
        for k in range(5):
            final.append(intermediate[k])

    final = QuickSort(final, 0, len(final) - 1, 2)

    new_text = ""
    for sentence in final:
        new_text += sentence[0] + '. '
    print(new_text)
    
main("Mashable", "http://mashable.com/2015/08/06/apple-third-ios-9-public-beta/")
