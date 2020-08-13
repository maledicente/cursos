__import__("os").system("pip install beautifulsoup4 -q")
import unicodedata
from bs4 import BeautifulSoup
import urllib.request as ur
import pandas as pd

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

urlDic = {'ListOfUSPresidents':'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_by_age'} 

def getData(url):
  u = ur.urlopen(ur.Request(url))
  soup = BeautifulSoup(u, features='html.parser')
  table = soup.find('table', attrs={'class':'sortable wikitable'}) 
  table_body = table.find('tbody')
  #print(table_body)
  rows = table_body.find_all('tr')
  head = [[unicodedata.normalize("NFKD", ele.text.strip()) for ele in row.find_all('th') ]for row in rows if len(row.find_all('th'))>0][0]
  #print(head)
  data = [[unicodedata.normalize("NFKD", ele.text.strip()) for ele in row.find_all('td') ]for row in rows if len(row.find_all('td'))>0] 
  dic =  {head[i]:[j[i] for j in data] for i in range(len(head))}
  indx = list(map(int,dic['#']))
  dic['Height'] = heights
  del dic['#']
  df = pd.DataFrame(dic,index=indx)
  return df

for i in urlDic:
  pres=getData(urlDic[i])
  print(pres)