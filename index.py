from time import *
from random import *
nouns=[['dog','c'],['cat','c'],['mud','c'],['universe','c'],['tree','c'],['forest','c'],['text document','c'],['apple','v'],['orange','v'],['leash','c'],['fir','c'],['bacon','c'],['adventure','v'],['turtle','c'],['nun','c'],['table','c'],['TV','c'],['peom','c'],['glockenspiel','c'],['dream','c']]
art=['the','a']
verbs=[['run','p'],['walk','p'],['go','p'],['stay here','p'],['eat','a'],['poop','p'],['squirt','a'],['applaud','a'],['dream','p']]
pre=['with','under','over','into','onto','between','through']
pro=['I','We','You','They']
for i in range(1000):
    nounn=randint(0,len(nouns)-1)
    nounu=nouns[nounn][0]
    if nouns[nounn][1] == 'c':
        artu=art[randint(0,1)]
    else:
        artu=art[randint(0,1)]
        if artu == 'a':
            artu='an'
    verbn=randint(0,len(verbs)-1)
    verbu=verbs[verbn][0]
    pron=randint(0,len(pro)-1)
    prou=pro[pron]
    if verbs[verbn][1] == 'p':
        prep=True
    else:
        prep=False
    if prep==True:
        preu=pre[randint(0,len(pre)-1)]
        sentence=prou+' '+verbu+' '+preu+' '+artu+' '+nounu+'.'
    else:
        sentence=prou+' '+verbu+' '+artu+' '+nounu+'.'
    print(sentence)
    sleep(.4)