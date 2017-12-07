#! python3
import bs4, requests, re

#address=input("Enter the adress of the metalarchives album page: ")
def scrapper(site):
    res=requests.get(site)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elem= soup.select('#album_tabs_tracklist')
    #print(elem)

    number_regex=re.compile(r'(?:</a>)(.*)(?:.</td>)')
    number_mo=number_regex.findall(str(elem))
    #print(number_mo)

    title_regex=re.compile(r'(?:<td class="wrapWords)(?: bonus)?(?:">\n)(.*)\n(.*)(?:</td>)')
    title_mo=title_regex.findall(str(elem))
    for i in range(len(title_mo)):
        title_mo[i]=title_mo[i][0].strip()
    #print(title_mo)
    time_regex=re.compile(r'\d\d:\d\d')
    time_mo=time_regex.findall(str(elem))[:-1]
    for i in range(len(time_mo)):
        if time_mo[i][0]=="0":
               time_mo[i]=time_mo[i][1:]
    #print(time_mo)
    for i in range(len(time_mo)):
        print(number_mo[i],title_mo[i],time_mo[i], sep="|")
    for i in range (len(time_mo),len(number_mo)):
            print(number_mo[i]+"|"+title_mo[i])
#scrapper(address)