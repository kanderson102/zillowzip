import urllib.request
import bs4 as bs
import re
from pyZillowProcessing import land_details

def zpid_to_dict(zpid):
    sauce = urllib.request.urlopen("https://www.zillow.com/"
                               "homedetails/" + str(zpid) + "_zpid").read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    tag = soup.title.string
    address = re.search(r'(.+)\s\d\d\d\d\d',tag)
    zip = re.search(r'\s(\d\d\d\d\d)\s',tag)

    home_dict = {}
    home_dict['address'] = address.group(0)
    home_dict['zip'] = zip.group(1)

    # prices = soup.find_all('span')
    # for price in prices:
    #     if re.search(r'$',price)==True:
    #         print(price.string)

    return home_dict

def sqft_to_acres(sqft_lot):
    return float(sqft_lot)*(0.00002296)

def construct_zillow_URL(type,zip,min,max,):
    type = type
    zip = str(zip)
    min = str(min)
    max = str(max)
    sauce = urllib.request.urlopen("https://www.zillow.com/homes/for_sale/"
                                    ""+zip+"/"+type+"/"+min+"-"+max+"_price/").read()

    return sauce

def get_zip():
    zip = True
    while zip:
        try:
            zip = int(input(r"Search by zip code:"))
        except ValueError:
            print("Error: Must enter a five digit integer.")
            continue

        if len(str(zip)) != 5:
            print("Must enter a five digit integer.")
            continue
        else:
            return str(zip)

def compile_list(zlist):
    home_list = []
    print("Compiling details...")
    for id in zlist[:4]:
        home = zpid_to_dict(id)
        home_list.append(home)

    for home in home_list:
        result = land_details(home['address'],home['zip'])
        home['zpid'] = result.zillow_id
        home['Type'] = result.home_type
        home['Price'] = result.zestimate_amount
        home['Link'] = result.home_detail_link
        home['Size'] = str(sqft_to_acres(result.property_size)) + ' acres'
        print(home)

zip = get_zip()
soup = bs.BeautifulSoup(construct_zillow_URL('land_type',zip,0,200000),'lxml')
match = re.search('zpid:.+,pg',str(soup))   #string of zp-ID's
zlist = re.findall('\d+',match.group())     #list of zp-ID's
if len(zlist)==0:
    print("No properties available for zip code {}".format(zip))
else:
    print('Compiled list of ZPIDs')
    compile_list(zlist)


