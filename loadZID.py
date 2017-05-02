import urllib.request
import bs4 as bs
import re

def zpid_to_address_zip(zpid):
    sauce = urllib.request.urlopen("https://www.zillow.com/"
                                   "homedetails/" + str(zpid) + "_zpid").read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    tag = soup.title.string
    address = re.match(r'(.+),\s(\w+),',tag)
    zip = re.search(r'\s(\d\d\d\d\d)\s',tag)

    home_dict = {}
    home_dict['address'] = address.group(1)
    home_dict['zip'] = zip.group(1)

    # prices = soup.find_all('span')
    # for price in prices:
    #     if re.search(r'$',price)==True:
    #         print(price.string)

    return home_dict
def sqft_to_acres(sqft_lot):
    return sqft_lot/(0.00002296)

def construct_zillow_URL(type,zip,min,max,):
    type = type
    zip = str(zip)
    min = str(min)
    max = str(max)

    sauce = urllib.request.urlopen("https://www.zillow.com/homes/for_sale/"
                                    ""+zip+"/"+type+"/"+min+"-"+max+"_price/").read()

    return sauce

soup = bs.BeautifulSoup(construct_zillow_URL('land_type',28778,0,200000),'lxml')
match = re.search('zpid:.+,pg',str(soup))   #string of zp-ID's
zlist = re.findall('\d+',match.group())     #list of zp-ID's
print('Compiled list of ZPIDs')


from pyZillowProcessing import land_details

home_list = []
for id in zlist[:4]:
    home = zpid_to_address_zip(id)
    home_list.append(home)
    print('Added ' + id + ' to dict.')

for home in home_list:
    try:
        result = land_details(home['address'],home['zip'])
        home['zpid'] = result.zillow_id
        home['Type'] = result.home_type
        home['Size'] = sqft_to_acres(result.property_size)
        home['Price'] = result.zestimate_amount
        home['Link'] = result.home_detail_link
        print(home)
    except:
        print('Error for {}'.format(home))