from time import *
from random import *
import menu
nouns=[['dog','c'],['cat','c'],['mud','c'],['universe','c'],['tree','c'],['forest','c'],['text document','c'],['apple','v'],['orange','v'],['leash','c'],['fir','c'],['bacon','c'],['adventure','v'],['turtle','c'],['nun','c'],['table','c'],['TV','c'],['peom','c'],['glockenspiel','c'],['dream','c'],['computer','c'],['shortstop','c'],['underwear','v'],['Border Collie','c']]
art=['the','a']
verbs=[['run','p'],['walk','p'],['go','p'],['stay here','p'],['eat','a'],['poop','p'],['squirt','a'],['applaud','a'],['dream','p']]
adv=['secretly','suddenly','quickly','happily','angrily','baconly','fuzzily','cheaply','slowly','instantaneously','brightly','groggily','dreamily','rapturously']
adj=[['sparkly','c'],['shiny','c'],['fuzzy','c'],['purple','c'],['red','c'],['orange','c'],['yellow','c'],['glittery','c'],['green','c'],['blue','c'],['purple','c'],['black','c'],['brown','c'],['spotted','c'],['dark','c'],['light','c'],['corrugated','c'],['paisley','c'],['pregnant','c'],['snowy','c'],['dead','c']]
pre=['with','under','over','into','onto','between','through']
pro=['I','We','You','They']
while True:
    times=menu.menu([['1',1],['10',10],['20',20],['50',50],['100',100],['200',200],['500',500],['1000',1000],['Exit','e']],3,'How many sentences do you want to generate?')
    menu.clear()
    if times=='e':
        exit()
    for i in range(times):
        adjn=randint(0,len(adj)-1)
        adju=adj[adjn][0]
        nounn=randint(0,len(nouns)-1)
        nounu=nouns[nounn][0]
        artu=art[randint(0,1)]
        verbn=randint(0,len(verbs)-1)
        verbu=verbs[verbn][0]
        pron=randint(0,len(pro)-1)
        prou=pro[pron]
        advn=randint(0,len(adv)-1)
        advu=adv[advn]
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
    print('Finished(enter to continue)')
    input()