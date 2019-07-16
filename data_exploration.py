# File Name: data_exploration.py
# Created By: Galen Palowitch
# Created On: 15 July, 2019
# Last Edited By: Galen Palowitch
# Last Edited On: 15 July, 2019
# Description: Exploring the three datasets.

# Import necessary libraries.
import pandas as pd
import numpy as np
import datetime as dt


# Read in CSVs.
companies = pd.read_csv(r'C:\Users\gdp5st\Documents\Hi5\Data\companies.csv')
highfives = pd.read_csv(r'C:\Users\gdp5st\Documents\Hi5\Data\highfives.csv')
users = pd.read_csv(r'C:\Users\gdp5st\Documents\Hi5\Data\users.csv')


# Remove some empty rows in the companies dataset.
companies = companies[companies['companyName'].notna()]
companies = companies.drop_duplicates(subset = 'companyName', keep = 'last')


# Convert all dates to datetime format.
companies['signupDate'] = pd.to_datetime(companies['signupDate'], unit = 'ms')
highfives['createDate'] = pd.to_datetime(highfives['createDate'], unit = 'ms')
highfives['crownedDate'] = pd.to_datetime(highfives['crownedDate'], unit = 'ms')
users['invitedDate'] = pd.to_datetime(users['invitedDate'], unit = 'ms')
users['joinedDate'] = pd.to_datetime(users['joinedDate'], unit = 'ms')
users['lastLogin'] = pd.to_datetime(users['lastLogin'], unit = 'ms')
users['latestFiveToDate'] = pd.to_datetime(users['latestFiveToDate'], unit = 'ms')


# Merge all data into single dataframe.
fullData = pd.merge(highfives, users, left_on = 'giverId', right_on = '_id', how = 'left')
fullData = pd.merge(fullData, users, left_on = 'receiverId', right_on = '_id', how = 'left')
fullData = pd.merge(fullData, companies, left_on = 'companyName_x', right_on = 'companyName', how = 'left')
fullData = pd.merge(fullData, companies, left_on = 'companyName_y', right_on = 'companyName', how = 'left')


# Rename the columns for easy use.
fullData.columns = ['id', 'giverId', 'receiverId', 'createDate', 'platformGiven',
       'confirmedCount', 'comment', 'media', 'confirmed', 'values', 'crowned',
       'crownedDate', 'taggedIds', 'highfiveComments', 'sentimentScore', 'gId',
       'giverFullName', 'giverUnreadCount', 'giverCompanyId',
       'giverCompanyName', 'giverInvitedBy', 'giverTitle', 'giverStartDate',
       'giverInvitedDate', 'giverJoinedDate', 'giverLastLogin',
       'giverIsActive', 'giverOsType', 'giverLatestFiveToDate',
       'giverPermissions', 'giverReceived', 'giverGiven', 'giverBacked',
       'giverIsCompanyBot', 'rId', 'receiverFullName', 'receiverUnreadCount',
       'receiverCompanyId', 'receiverCompanyName', 'receiverInvitedBy',
       'receiverTitle', 'receiverStartDate', 'receiverInvitedDate',
       'receiverJoinedDate', 'receiverLastLogin', 'receiverIsActive',
       'receiverOsType', 'receiverLatestFiveToDate', 'receiverPermissions',
       'receiverReceived', 'receiverGiven', 'receiverBacked',
       'receiverIsCompanyBot', 'gCompanyId', 'giverCompanyName2', 'giverCompanySubType',
       'giverCompanySignupDate', 'giverActiveCompany', 'giverCompanySize', 'giverCompanyLocation',
       'giverCompanyIndustry', 'rCompanyId', 'receiverCompanyName2', 'receiverCompanySubType', 'receiverCompanySignupDate',
       'receiverActiveCompany', 'receiverCompanySize', 'receiverCompanyLocation', 'receiverCompanyindustry']


fullData.to_csv(r'C:\Users\gdp5st\Documents\Hi5\Data\fulldata.csv')