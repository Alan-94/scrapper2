page=input("Enter the address of the website: ")
if "bandcamp.com" in page:
    from bandcamp_scrapper import scrap
    print(scrap(page))
elif "metal-archives.com" in page:
    from ma_scrapper import scrapper
    print(scrapper(page))
elif "discogs" in page:
    from discogs_scrapper import scrap
    print (scrap(page))
else:
    print ("Unfortunately that website is not supported.")
