#! python3
import bs4, requests, re

#address = input("Enter the adress of the bandcamp album page: ")

def scrap(site):
    res = requests.get(site)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elem = soup.select('.track_list')
    # print(elem)
    number_regex = re.compile(r'(?:tracknum=)(\d+)')
    number_mo = number_regex.findall(str(elem))
    # print(number_mo)

    title_regex = re.compile(r'(?:<span itemprop="name">)(.*)(?:</span>)')
    title_mo = title_regex.findall(str(elem))
    # print(title_mo)

    time_regex = re.compile(r'(?:<span class="time secondaryText">\s(.*)\s+)(\d\d:\d\d)')
    time_mo = time_regex.findall(str(elem))
    time_mo = [i[1] for i in time_mo]
    for i in range(len(time_mo)):
        if time_mo[i][0] == "0":
            time_mo[i] = time_mo[i][1:]
    # print(time_mo)

    for i in range(len(number_mo)):
        print(str(number_mo[i]), str(title_mo[i]), str(time_mo[i]), sep="|")
#scrap(address)