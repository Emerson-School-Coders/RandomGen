from time import *
from random import *
import easygui
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
nounVN=[]
nounVNfile=open('nounVN.rgf')
for line in nounVNfile:
    nounVN.append(item)
nounVNfile.close()
verbVN=[]
verbVNfile=open('verbVN.rgf')
for line in verbVNfile:
    verbVN.append(item)
verbVNfile.close()
pro=[]
profile=open('pro.rgf')
for line in profile:
    pro.append(item)
profile.close()
pre=[]
prefile=open('pre.rgf')
for line in prefile:
    pre.append(item)
prefile.close()
nouns=[]
nounsfile=open('nouns.rgf')
for line in nounsfile:
    nouns.append(item)
nounsfile.close()
verbs=[]
verbsfile=open('verbs.rgf')
for line in verbsfile:
    verbs.append(line)
verbsfile.close()
art=[]
artfile=open('art.rgf')
for line in artfile:
    art.append(line)
artfile.close()
adj=[]
adjfile=open('adj.rgf')
for line in adjfile:
    adj.append(item)
adjfile.close()
adv=[]
advfile=open('adv.rgf')
for line in advfile:
    adv.append(item)
advfile.close()
gen=easygui.buttonbox('What do you want to generate?','Make a choice',['Random sentences','Functions'])
if gen=='Random sentences':
    gen = 'RS'
else:
    gen = 'VN'
if gen=='RS':
    while True:
        times=easygui.choicebox("What do you want to do?","Choose an option",['Generate 1','Generate 10','Generate 20','Generate 50','Generate 100','Generate 200','Generate 500','Generate 1000','Generate 10000(Not recommended)','Exit','View all generated this session','View all ever generated'])
        if times=='Generate 1':
            times=1
        elif times=='Generate 10':
            times=10
        elif times=='Generate 20':
            times=20
        elif times=='Generate 50':
            times=50
        elif times=='Generate 100':
            times=100
        elif times=='Generate 200':
            times=200
        elif times=='Generate 500':
            times=500
        elif times=='Generate 1000':
            times=1000
        elif times=='Generate 10000(Not recommended)':
            times=10000
        elif times=='View all generated this session':
            times='VA'
        elif times=='View all ever generated':
            times='VAG'
        else:
            exit()
        stuffs=''
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                stuffs=stuffs+save[i-1]+'\n'
        elif times=='VAG':
            for i in range(len(saver1)):
                stuffs=stuffs+saver1[i][:-1]+'\n'
        else:
            for i in range(times):
                adjn=randint(0,len(adj)-1)
                adju=adj[adjn]
                nounn=randint(0,len(nouns)-1)
                nounu=nouns[nounn]
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
                stuffs=stuffs+sentence+'\n'
                save.append(sentence)
                savef1.write(sentence+'\n')
                saver1.append(sentence)
        easygui.textbox('Your sentences:','The sentences',stuffs)
else:
    while True:
        times=easygui.choicebox("What do you want to do?","Choose an option",['Generate 1','Generate 10','Generate 20','Generate 50','Generate 100','Generate 200','Generate 500','Generate 1000','Generate 10000(Not recommended)','Exit','View all generated this session','View all ever generated'])
        if times=='Generate 1':
            times=1
        elif times=='Generate 10':
            times=10
        elif times=='Generate 20':
            times=20
        elif times=='Generate 50':
            times=50
        elif times=='Generate 100':
            times=100
        elif times=='Generate 200':
            times=200
        elif times=='Generate 500':
            times=500
        elif times=='Generate 1000':
            times=1000
        elif times=='Generate 10000(Not recommended)':
            times=10000
        elif times=='View all generated this session':
            times='VA'
        elif times=='View all ever generated':
            times='VAG'
        else:
            exit()
        stuffs=''
        if times=='e':
            exit()
        elif times=='VA':
            for i in range(len(save)):
                stuffs=stuffs+save[i-1]+'\n'
        elif times=='VAG':
            for i in range(len(saver)):
                stuffs==stuffs+saver[i][:-1]+'\n'
        else:
            for i in range(times):
                verb=verbVN[randint(0,len(verbVN)-1)]
                noun=nounVN[randint(0,len(nounVN)-1)]
                randomVN=verb + " " + noun
                save.append(randomVN)
                stuffs=stuffs+randomVN+'\n'
                savef.write(randomVN+'\n')
                saver.append(randomVN)
        easygui.textbox('Your functions:','The functions',stuffs)

