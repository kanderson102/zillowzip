import urllib.request
import bs4 as bs
import re
import sys
import argparse


def zpid_to_dict(zpid):
    sauce = urllib.request.urlopen("https://www.zillow.com/"
                               "homedetails/" + str(zpid) + "_zpid").read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    header = soup.head.title
    price = soup.find(class_= "main-row home-summary-row")
    size = soup.find(class_= "addr_bbs")

    home = {}
    if header:
        address = re.search(r'(.+)\s\d\d\d\d\d', header.string)
        home['Address'] = address.group(0)
        home['Size'] = size.string
        home['Link'] = "https://www.zillow.com/homedetails/" + str(zpid) + "_zpid/"
        if price:
            home['Price'] = (price.text[2:-3]) # get rid of the extra spaces
        else:
            home['Price'] = 'None'

    return home

#not in use
def sqft_to_acres(sqft_lot):
    return round(float(sqft_lot)*(0.00002296),3)

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('zip', type=int, help='Enter a valid five digit zipcode')
    parser.add_argument('-m','--min', type=int, default=0, help='Minimum Price, ' + \
                        'Should be less than Max.')
    parser.add_argument('-M','--Max', type=int, default=0, help='Maximum Price. ' + \
                        'Should be greater than min.')
    args = parser.parse_args(argv[1:])

    if len(str(args.zip)) != 5:
        sys.exit("Must enter a five digit integer.")

    if args.min < 0 or args.Max < 0:
        sys.exit("Must enter a positive number")

    if args.min and args.Max:
        if args.min >= args.Max:
            sys.exit("MIN must be less than MAX.")

    return args

def main(argv):
    args = parse_args(argv)
    if not args.Max:
        max = '_price'
    else:
        max = args.Max
    url = "https://www.zillow.com/homes/for_sale/" + str(args.zip) + \
          "/land_type/" + str(args.min) + "-" + str(max) + "_price"
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    match = re.search('zpid:.+,pg',str(soup))   #string of zp-ID's

    try:
        count = 0
        while count < 3:    #sometimes the search produces a false negative
            if match:
                zlist = re.findall('\d+',match.group())     #list of zp-ID's
                print('Compiled list of ZPIDs')
                print('Fetching results...')    #pseudo load screen
                for z in zlist:
                    x = zpid_to_dict(z)
                    if x:
                        print(x)
                break
            else:
                count+=1
    except:
        print("No properties available for zip code {}".format(args.zip))

    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
