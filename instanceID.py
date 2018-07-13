import requests, openpyxl, re

TWXAPPKEY = '43935222-f84f-4dfd-aee2-b909bd419537'
TWXURL = 'ptc-test5.cloud.thingworx.com'

## Opens precursor spreadsheet ##
workBook1 = openpyxl.load_workbook('C:\\Users\\pafable\\Documents\\git\\thingworx_api\\list.xlsx')
print(workBook1)
workSheet1 = workBook1.active

api = 'https://IOTNOCisLYFE/Thingworx/Subsystems/LicensingSubsystem/Services/GetInstanceId'
f = api.replace('IOTNOCisLYFE', TWXURL)
#print(f)

##### POST Request #####
payload = {
           'appkey': 'CS_IOT_IS_THE_BEST!!!',
		   'Content-Type': 'application/json',
		   'Accept': 'application/json'
		  }

payload['appkey'] = TWXAPPKEY
#print(payload)

try:
    ptc = requests.post(f, headers=payload)

    IDRegex = re.compile(r'\w\w\w\w\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w\w\w\w\w\w\w\w\w')
    filteredID = IDRegex.search(ptc.text)
    print(filteredID.group())
except AttributeError:
	print('not found')