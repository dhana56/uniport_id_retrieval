import requests,pickle
from bs4 import BeautifulSoup
value= []
dic_1 ={}

#avoiding the scrappy block as a scrapper, have to use headers and proxies
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
proxies = {
    "https": "http://172.16.2.251:3128" ,"https": "http://172.16.2.250:3128",
    "https": "http://172.16.2.252:3128"
}

with open(r"C:\Users\dhana\OneDrive\Desktop\thesis_work_final\prj501\Single_mutation\run_script\uniport_sadh\code\pdb_allchain_uniport\pdbscrap_722023.txt","r")as file: # provide the file path
    for i in file:
        value.append(i.replace("\n",''))
value = list(set(value))      
# print(value)  
# value = ['3mv7']       
for i,r in enumerate(value[:]):
    dic ={}
    print(r)
    print(len(value)-i)
    pageurls = r"https://www.rcsb.org/structure/"+r[:4]
    try:
        # url = requests.get(pageurls,proxies=proxies,headers=headers)
        url = requests.get(pageurls)
        soup = BeautifulSoup(url.content, 'html.parser')
        chain_dic = {}
        for z in [1,2,3,5,6,7]: #multiple looping for the multple chains.
                    try :
                        d =soup.find('table',{'class':"table table-bordered table-condensed tableEntity" ,
                                        'id':f'table_macromolecule-protein-entityId-{z}'}) 
                        s = d.find('tr',{'id':f"macromolecule-entityId-{z}-rowDescription"})
                        uniport = d.find('span',{'class':"label label-rcsb"}).text
                        chain = s.find('td',{'style':'width:200px;'}) #.text.replace(',','').replace('Less','')
                        sam_1 =[i.get_text() for i in chain.find_all('a')] #Stores the chain value as list
                        # sam = [i[8:9] if len(i)>1 else i for i in set(sam_1)  ]

               
                        chain_dic[tuple(sam_1)] =uniport #
                        if uniport== '30% Identity': #When chain have no uniport id is not provided,it will add value = 'None' 
                            uniport ='None'
                            with open(r"30%_identity.txt",'a') as file_30:
                                file_30.write(r+' '+'\n')
                                file_30.close()
                        chain_dic[tuple(sam_1)] =uniport
                        dic_1[r] =chain_dic
                        print(chain_dic)
                    except: 
                         pass
    except Exception as e:
            print('not_done')
            with open(r"error_uniport_notdone.txt",'a') as file_3:# Save the pdb_ids that can't be scrapped or got error 
                file_3.write(r+'\n')
                file_3.write(str(e)+'\n')
                file_3.close
            pass
with open('pbd_allchainui.pkl', 'wb') as f: #Stores in the pickle file
    pickle.dump(dic_1, f)






























