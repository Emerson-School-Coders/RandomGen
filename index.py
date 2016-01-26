from time import *
from random import *
import menu
from getkey import getKey
savef = open('all_ever_generated', 'a')
savecache = open('all_ever_generated', 'r')
savef1 = open('all_ever_generated1', 'a')
savecache1 = open('all_ever_generated1', 'r')
saver=[]
saver1=[]
for line in savecache:
    saver.append(line)
for line in savecache1:
    saver1.append(line)
continue1=0
nouns=[['dog','c'],['cat','c'],['mud','c'],['universe','c'],['tree','c'],['forest','c'],['text document','c'],['apple','v'],['orange','v'],['leash','c'],['fir','c'],['bacon','c'],['adventure','v'],['turtle','c'],['nun','c'],['table','c'],['TV','c'],['peom','c'],['glockenspiel','c'],['dream','c'],['computer','c'],['shortstop','c'],['underwear','v'],['Border Collie','c'],['snake','c']]
art=['the','a']
verbs=[['run','p'],['walk','p'],['go','p'],['stay here','p'],['eat','a'],['poop','p'],['squirt','a'],['applaud','a'],['dream','p']]
adv=['secretly','suddenly','quickly','happily','angrily','baconly','fuzzily','cheaply','slowly','instantaneously','brightly','groggily','dreamily','rapturously','stupidly']
adj=[['sparkly','c'],['shiny','c'],['fuzzy','c'],['purple','c'],['red','c'],['orange','c'],['yellow','c'],['glittery','c'],['green','c'],['blue','c'],['purple','c'],['black','c'],['brown','c'],['spotted','c'],['dark','c'],['light','c'],['corrugated','c'],['paisley','c'],['pregnant','c'],['snowy','c'],['dead','c']]
pre=['with','under','over','into','onto','between','through']
pro=['I','We','You','They']
save=[]
verbVN=['Absorb','Actuate','Improve','Generate','Allow','Increase','Attach','Limit','Attract','Maintain','Conduct','Position','Connect','Prevent','Contain','Protect','Control','Provide','Convert','Reduce','Create','Regulate','Decrease','Resist','Direct','Rotate','Facilitate','Transmit','Seal']
nounVN=['Access','Air','Apperance','Circuit','Cold','Component','Corrosion','Current','Deflection','Dirt','Energy','Entry','Flow','Fluid','Friction','Heat','Impact','Mass','Moisture','Noise','Light','Parts','Path','Performance','Stability','Surface','Travel','Vibration']
gen=menu.menu([['Verb/Noun combos','VN'],['Random sentences','RS']],1,'What do you want to generate?')
if gen=='RS':
    while True:
        times=menu.menu([['Generate 1',1],['Generate 10',10],['Generate 20',20],['Generate 50',50],['Generate 100',100],['Generate 200',200],['Generate 500',500],['Generate 1000',1000],['Exit','e'],['View all generated this session','VA'],['View all generated previously','VAG']],3,'What do you want to do?')
        menu.clear()
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                print(save[i-1])
        elif times=='VAG':
            for i in range(len(saver1)):
                print(saver1[i][:-1])
        else:
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
                save.append(sentence)
                savef1.write(sentence+'\n')
                saver1.append(sentence)
        print('Finished!  Press q to continue.')
        while getKey()!='q':
            pass
else:
    while True:
        times=menu.menu([['Generate 1',1],['Generate 10',10],['Generate 20',20],['Generate 50',50],['Generate 100',100],['Generate 200',200],['Generate 500',500],['Generate 1000',1000],['Exit','e'],['View all generated this session','VA'],['View all generated previously','VAG']],3,'What do you want to do?')
        menu.clear()
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                print(save[i-1])
        elif times=='VAG':
            for i in range(len(saver)):
                print(saver[i][:-1])
        else:
            for i in range(times):
                verb=verbVN[randint(0,len(verbVN)-1)]
                noun=nounVN[randint(0,len(nounVN)-1)]
                randomVN=verb + " " + noun
                save.append(randomVN)
                print(randomVN)
                savef.write(randomVN+'\n')
                saver.append(randomVN)
        print('Finished!  Press q to continue.')
        while getKey()!='q':
            pass
