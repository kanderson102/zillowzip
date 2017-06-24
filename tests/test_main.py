import pytest
import loadZID

def test_sqft_to_acres():
	acres = loadZID.sqft_to_acres(10000)
	assert acres == 0.2296
