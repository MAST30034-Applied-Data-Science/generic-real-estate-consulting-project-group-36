import requests
import re
import json

import csv

def get_html(url, ty):
    """This function is used to extract information from the website"""
    
    #file path used to save 
    log_path = './domain_' + ty + '.csv'
    file = open(log_path, 'a+', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([f'address', 'price','beds','baths','parking','propertyTypeFormatted'])
    
    #set haeader
    headers = {"Host":"www.domain.com.au",\
    "Connection":"keep-alive",\
    "Cache-Control":"max-age=0",\
    "Upgrade-Insecure-Requests":"1",\
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",\
    "Accept":"text/html",\
                   "Accept-Encoding":"gzip, deflate, br",\
    "Accept-Language":"zh-CN,zh;q=0.9"}
    
    # send request
    res = requests.get(url,headers=headers)
    html = res.text
    
    # match information
    rs = re.search("(type=\"application/json\">)(.|\n)*?(</script>)", html, re.I)
    jsonStr=rs[0].replace('type="application/json">','').replace('</script>','')
    mes_to_dict = json.loads(jsonStr)
    infos=(mes_to_dict['props']['pageProps']['componentProps']['listingsMap'])
    
    # Loop to retrieve information content
    for i in infos:
        listingModel=infos[i]['listingModel']
        price=listingModel['price']
        address=listingModel['address']
        addressStr=address['suburb']+' '+address['street']+' '+address['state']+' '+address['postcode']
        feature=listingModel['features']
        beds = 0
        if 'beds' in feature.keys():
            beds = feature['beds']
        baths = 0
        if 'baths' in feature.keys():
            baths = feature['baths']
        parking = 0
        if 'parking' in feature.keys():
            parking = feature['parking']
        propertyTypeFormatted = feature['propertyTypeFormatted']
        csv_writer.writerow([addressStr,price,beds,baths,parking,propertyTypeFormatted])#写入csv文件
    file.close()

# the URL for page 1
URL = "https://www.domain.com.au/rent/melbourne-vic-3000/?ptype=apartment-unit-flat,block-of-units,duplex,free-standing,new-apartments,new-home-designs,new-house-land,pent-house,semi-detached,studio,terrace,villa&excludedeposittaken=1&page=1"


# try to read 50 pages
pages = 50
for i in range(0, pages):
    page = i+1
    print("Page %d starts to read" % (page))
    get_html("https://www.domain.com.au/rent/?ptype=house&excludedeposittaken=1&state=vic&page=%d" % page, "house")
    get_html("https://www.domain.com.au/rent/?ptype=apartment&excludedeposittaken=1&state=vic&page=%d" % page, "apartment")
    print("Page %d finished" % (page))
print("read all")