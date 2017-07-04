# zillowzip
This program returns a dictionary of Zillow.com search results based on the zip code entered at the command line. You can specify the minimum and/or maximum price for the zip code by using the ```-m``` or ```-M``` optional arguments, respectively. Exlcuding them defaults to all possible search results.

The output dictionary includes the Address, Lot Size, Price, and Link to the listing.

# Usage:
```
$ zillowzip 78702 -m 200000 -M 1000000

Compiled list of ZPIDs
Fetching results...
{'Address': '1130 Northwestern Ave, Austin, TX 78702', 'Size': '0.35 acres', 'Price': '$249,500', 'Link': 'https://www.zillow.com/homedetails/2103607041_zpid/'}
{'Address': '1309 Holly St, Austin, TX 78702', 'Size': '7,840 sqft', 'Price': '$550,000', 'Link': 'https://www.zillow.com/homedetails/29382503_zpid/'}
{'Address': '1809 New York Ave, Austin, TX 78702', 'Size': '0.3 acres', 'Price': '$465,000', 'Link': 'https://www.zillow.com/homedetails/2093812584_zpid/'}
{'Address': '1302 Taylor St, Austin, TX 78702', 'Size': '4,791 sqft', 'Price': '$318,000', 'Link': 'https://www.zillow.com/homedetails/2119884738_zpid/'}
{'Address': '1102 Northwestern Ave, Austin, TX 78702', 'Size': '6,534 sqft', 'Price': '$685,000', 'Link': 'https://www.zillow.com/homedetails/125902963_zpid/'}
{'Address': '1309 Cedar Ave, Austin, TX 78702', 'Size': '6,054 sqft', 'Price': '$319,900', 'Link': 'https://www.zillow.com/homedetails/29389677_zpid/'}
{'Address': '2211 E 5th St, Austin, TX 78702', 'Size': '8,276 sqft', 'Price': '$499,900', 'Link': 'https://www.zillow.com/homedetails/29383127_zpid/'}
{'Address': '1209 Willow St # 1/2, Austin, TX 78702', 'Size': '6,141 sqft', 'Price': '$500,000', 'Link': 'https://www.zillow.com/homedetails/29382584_zpid/'}
```

# Installation
Download the <a href="https://github.com/kanderson102/zillowzip">source</a> above and install.
```
$ git clone https://github.com/kanderson102/zillowzip.git
$ cd zillowzip
$ python setup.py install
```

# Help
```
$ zillowzip -h
```
