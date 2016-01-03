from time import *
from random import *
nouns=[['dog','c'],['cat','c'],['mud','c'],['universe','c'],['tree','c'],['forest','c'],['text document','c'],['apple','v'],['orange','v'],['leash','c'],['fir','c'],['bacon','c'],['adventure','v'],['turtle','c'],['nun','c'],['table','c'],['TV','c'],['peom','c'],['glockenspiel','c'],['dream','c'],['computer','c'],['shortstop','c'],['underwear','v']]
art=['the','a']
verbs=[['run','p'],['walk','p'],['go','p'],['stay here','p'],['eat','a'],['poop','p'],['squirt','a'],['applaud','a'],['dream','p']]
adv=['secretly','suddenly','quickly','happily','angrily','baconly','fuzzily','cheaply','slowly','instantaneously','brightly','groggily','dreamily','rapturously']
adj=['sparkly','shiny','fuzzy','purple','red','orange','yellow','glitterly','yellow','green','blue','white','black','brown','spotted','dark','light','corrugated','paisley','pregnant','snowy','dead']
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
    advn=randint(0,len(adv)-1)
    advu=adv[advn]
    adjn=randint(0,len(adj)-1)
    adju=adj[adjn]
    if verbs[verbn][1] == 'p':
        prep=True
    else:
        prep=False
    if prep==True:
        preu=pre[randint(0,len(pre)-1)]
        sentence=prou+' '+advu+' '+verbu+' '+preu+' '+artu+' '+adju+' '+nounu+'.'
    else:
        sentence=prou+' '+advu+' '+verbu+' '+artu+' '+adju+' '+nounu+'.'
    print(sentence)
    sleep(.4)