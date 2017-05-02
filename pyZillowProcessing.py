from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

def land_details(address, zip):
    ZWSID = 'X1-ZWz19adsbelb0r_43hp8'
    zillow_data = ZillowWrapper(ZWSID)
    deep_search_response = zillow_data.get_deep_search_results(address, zip)
    result = GetDeepSearchResults(deep_search_response)

    return result