import requests
from bs4 import BeautifulSoup as bs
import re
from tabulate import tabulate
import subprocess
data = {
    "action": "data_fetch",
    "keyword": input("Enter anime name: ")
        }
response = requests.post("https://simplyaweeb.com/wp-admin/admin-ajax.php", data = data)
soup = bs(response.text, "html.parser")
cover = []
ref = []
results = []

for j,i in enumerate(soup.find_all('a')):
    try:
        if i["class"] == ['a-cover']:
            cover.append(i['href'])
        elif i["class"] == ['video-close', 'search-single']:
            ref.append("https://gogoanime-six.now.sh/api/v1/MusicSingleHandler/"+i["href"])
            results.append([j//2, i.text.strip()])
    except:
        pass
print(tabulate(results))
opt = int(input("Enter number: "))

k = requests.get(ref[opt])
print(ref[opt])
link = k.json()['music'][0]['music_single_url']
token = re.search(r'(download\/dl4\/)(.+)(\/o)', link).group(2)
name = link.split("/")[-1]
dow_link = f"http://dl4.wapkizfile.info/download/{token}/477539e252d5e2e8b94b2892725a838c/osanime+wapkiz+com/{name}"

def download(link):
    query=f"""wget "{link}" -q --show-progress --no-check-certificate -O {name.replace("-(osanime.com)", "")}"""
    subprocess.run(query,shell=True)
    
download(dow_link)