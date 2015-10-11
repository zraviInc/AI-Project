'''
File: 
	djia.py
Authors: 
	Prakash Dhimal, Kevin Sanford
Description:
	Python module to get the list of companies in Dow Jones Industrial Average
'''
import pandas as pd

'''
Uses DJIA_ticker.csv to get the list of company ticker
@param - none
@returns - tickers - list of ticker for all 30 companies in DJIA
'''
def get_djia_list():

	df = pd.read_csv('../Data/DJIA_ticker.csv')
	
	

	ticker = []

	for i in range(len(df)):
		temp = df['Ticker'][i]
		ticker.append(temp)
	return ticker
	

