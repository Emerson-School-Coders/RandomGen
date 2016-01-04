from time import *
from random import *
import menu
savef = open('all_ever_generated', 'a')
saver = open('all_ever_generated', 'r')
savef1 = open('all_ever_generated1', 'a')
saver1 = open('all_ever_generated1', 'r')
nouns=[['dog','c'],['cat','c'],['mud','c'],['universe','c'],['tree','c'],['forest','c'],['text document','c'],['apple','v'],['orange','v'],['leash','c'],['fir','c'],['bacon','c'],['adventure','v'],['turtle','c'],['nun','c'],['table','c'],['TV','c'],['peom','c'],['glockenspiel','c'],['dream','c'],['computer','c'],['shortstop','c'],['underwear','v'],['Border Collie','c']]
art=['the','a']
verbs=[['run','p'],['walk','p'],['go','p'],['stay here','p'],['eat','a'],['poop','p'],['squirt','a'],['applaud','a'],['dream','p']]
adv=['secretly','suddenly','quickly','happily','angrily','baconly','fuzzily','cheaply','slowly','instantaneously','brightly','groggily','dreamily','rapturously']
adj=[['sparkly','c'],['shiny','c'],['fuzzy','c'],['purple','c'],['red','c'],['orange','c'],['yellow','c'],['glittery','c'],['green','c'],['blue','c'],['purple','c'],['black','c'],['brown','c'],['spotted','c'],['dark','c'],['light','c'],['corrugated','c'],['paisley','c'],['pregnant','c'],['snowy','c'],['dead','c']]
pre=['with','under','over','into','onto','between','through']
pro=['I','We','You','They']
save=[]
verbVN=['Absorb','Actuate','Improve','Generate','Allow','Increase','Attach','Limit','Attract','Maintain','Conduct','Position','Connect','Prevent','Contain','Protect','Control','Provide','Convert','Reduce','Create','Regulate','Decrease','Resist','Direct','Rotate','Facilitate','Transmit']
nounVN=['Access','Air','Apperance','Circuit','Cold','Component','Corrosion','Current','Deflection','Dirt','Energy','Entry','Flow','Fluid','Friction','Heat','Impact','Mass','Moisture','Noise','Light','Parts','Path','Performance','Stability','Surface','Travel','Vibration']
gen=menu.menu([['Verb/Noun combos','VN'],['Random sentences','RS']],1,'What do you want to generate?')
if gen=='RS':
    while True:
        times=menu.menu([['1',1],['10',10],['20',20],['50',50],['100',100],['200',200],['500',500],['1000',1000],['Exit','e'],['View all generated this session','VA'],['View all ever generated','VAG']],3,'How many do you want to generate?')
        menu.clear()
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                print(save[i-1])
        elif times=='VAG':
            for line in saver1:
                print(line[:-1])
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
        input('Finished!  Press enter to continue.')
else:
    while True:
        times=menu.menu([['1',1],['10',10],['20',20],['50',50],['100',100],['200',200],['500',500],['1000',1000],['Exit','e'],['View all generated this session','VA'],['View all ever generated','VAG']],3,'How many do you want to generate?')
        menu.clear()
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                print(save[i-1])
        elif times=='VAG':
            for line in saver:
                print(line[:-1])
        else:
            for i in range(times):
                verb=verbVN[randint(0,len(verbVN)-1)]
                noun=nounVN[randint(0,len(nounVN)-1)]
                randomVN=verb + " " + noun
                save.append(randomVN)
                print(randomVN)
                savef.write(randomVN+'\n')
        input('Finished! Press enter to continue.')