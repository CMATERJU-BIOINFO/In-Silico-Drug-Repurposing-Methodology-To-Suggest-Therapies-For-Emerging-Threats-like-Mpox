# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:52:55 2023

@author: Sovan Saha
"""

path_set='C:\\Users\\admin\\Desktop\\-Computational-Drug-Repurposing-for-Viral-Infectious-Diseases-A-Case-Study-on-Monkeypox-main\\Drug analysis\\'

f1=open(path_set+'DrugBank.txt','r')
drug_detail=f1.readlines()

f2=open(path_set+'trgts dbrti.txt','r')
spreaders=f2.readlines()

f3=open(path_set+'Spreaders_drug_map.txt','w')

for i in spreaders:
    i=i.strip('\n')
    for j in drug_detail:
        j=j.strip('\n')
        if i in j:
            hld1=j.split('\t')
            if ';' in hld1[4]:
                drug_id=hld1[4].split(';')
                if len(drug_id)>=1:
                    for z in drug_id:
                        f3.writelines(hld1[2]+'|'+ z.strip() +'\n')
            else:
                f3.writelines(hld1[2]+'|'+ hld1[4].strip() +'\n')
f3.close()

f4=open(path_set+'drugbank idnamemapping.txt','r')
drugid_name=f4.readlines()

f5=open(path_set+'Spreaders_drug_map.txt','r')
spreader_drugs=f5.readlines()

f6=open(path_set+'Spreader_drug_name.txt','w')

for i in drugid_name:
    i=i.strip('\n')
    hld2=i.split('\t',1)
    for j in spreader_drugs:
        j=j.strip('\n')
        if hld2[0].strip() in j:
            f6.writelines(j+'|'+hld2[1].strip()+'\n')

f6.close()

import operator
            
f7=open(path_set+'Spreader_drug_name.txt','r')
hld1=f7.readlines()

dict1={}

drugid=[]
for i in hld1:
    i=i.strip('\n')
    hg=i.split('|',1)
    drugid.append(hg[1].strip())
    
drugid=list(set(drugid))
    
for i in drugid:
    i=i.strip('\n')
    w=i.split('|')    
    count=0;
    for j in hld1:
        if w[0].strip() in j:
            count+=1
    dict1[i]=count
sorted_dict =dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
#print(sorted_dict)
with open(path_set+"Spreader_drug_frequency.txt", 'a') as f: 
    for key, value in sorted_dict.items(): 
        f.write('%s|%s\n' % (key, value))
            
f.close()

            
        











            