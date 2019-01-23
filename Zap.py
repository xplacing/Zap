#Resources Used 
#1. https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
#2. https://stackoverflow.com/questions/4690600/python-exception-message-capturing
#3. http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes

import requests
from bs4 import BeautifulSoup

class Zap():
  def urls(file):
    filename = open(file,'r')
    urls = []
    for line in filename:
      urls.append(line+"'")
    print(len(urls),"URLs Loaded.\n")
    return(urls)
  def scan_urls(urls):
    count = 0
    vuln = 0
    notvuln = 0
    errors = 0
    header={'User-agent':'Mozilla/11.0',}
    for line in urls:
      url = line
      try:
        r = requests.get(url)
        content = BeautifulSoup(r.text, 'html.parser')
        test = r.text
        if(test.count("line") > 0):
          count += 1
          vuln +=1
          print(str(count)+"/"+str(len(urls))+ " Scanned\nVulnerable: "+str(vuln)+"/"+str(count)+"\nNot Vulnerable: "+str(notvuln)+"/"+str(count)+"\n")
        else:
          count += 1
          notvuln += 1
      except Exception as e:
        count += 1
        notvuln += 1
        print(str(count)+"/"+str(len(urls))+ " Scanned\nVulnerable: "+str(vuln)+"/"+str(count)+"\nNot Vulnerable: "+str(notvuln)+"/"+str(count)+"\n")
