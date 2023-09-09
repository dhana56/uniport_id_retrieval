
import requests
from bs4 import BeautifulSoup


def scrappy_fun(array):
    """Function used to retrieve the chain name : uniport for a given PDB id
    : array, will take the list of array of pdb_list
    """
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

    for i,r in enumerate(array):
        print(i+1,r)
        pageurls = r"https://www.rcsb.org/structure/"+r[:4]
        url = requests.get(pageurls)
        if url.status_code==200:   
            try:
                #Use downcode incase if you are using the proxy server to connect.
                # url = requests.get(pageurls,proxies=proxies,headers=headers)    
                soup = BeautifulSoup(url.content, 'html.parser')
                chain_dic = {}
                for z in [1,2,3,5,6,7]:   #multiple looping for the multple chains.
                            try :
                                d =soup.find('table',{'class':"table table-bordered table-condensed tableEntity" ,
                                                'id':f'table_macromolecule-protein-entityId-{z}'}) 
                                s = d.find('tr',{'id':f"macromolecule-entityId-{z}-rowDescription"})
                                uniport = d.find('span',{'class':"label label-rcsb"}).text
                                chain = s.find('td',{'style':'width:200px;'})        #.text.replace(',','').replace('Less','')
                                sam_1 =[i.get_text() for i in chain.find_all('a')]   #Stores the chain value as list

                                if uniport== '30% Identity':    #When chain have no uniport id is not provided,it will add value = 'None' 
                                    uniport ='None'
                                    with open(r"30%_identity.txt",'a') as file_30:
                                        file_30.write(r+' '+'\n')
                                        file_30.close()
                                chain_dic[tuple(sam_1)] =uniport
                                dic_1[r.lower()] =chain_dic
                            except: 
                                pass
            except Exception as e:
                    print('not_done')
                    with open(r"error_uniport_notdone.txt",'a') as file_3:# Save the pdb_ids that can't be scrapped or got error 
                        file_3.write(r+'\n')
                        file_3.write(str(e)+'\n')
                        file_3.close
                    pass
            
        elif url.status_code==404:
            print("Page not found")
        else:
            print("There is a problem of loading the page")
            print("Page url: ", pageurls)
            print("Please check the entry by clicking the above url")
        
    return dic_1




























