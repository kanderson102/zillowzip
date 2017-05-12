from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

def land_details(address, zip):
    ZWSID = ''
    zillow_data = ZillowWrapper(ZWSID)
    deep_search_response = zillow_data.get_deep_search_results(address, zip)
    result = GetDeepSearchResults(deep_search_response)

    return result