import requests, openpyxl, re

#TWXAPPKEY = ''
#TWXURL = ''
NumberOfRows = 6

## Opens precursor spreadsheet ##
workBook1 = openpyxl.load_workbook('C:\\Users\\pafable\\Documents\\git\\thingworx_api\\list.xlsx')
workSheet1 = workBook1.active

url_list = []
for i in range(2,NumberOfRows):
    row = workSheet1.cell(row=i, column=1).value
    url_list.append(row)
    #print(url_list)

appkey_list = []
for h in range(2,NumberOfRows):
    col = workSheet1.cell(row=h, column=2).value
    #print(col)
    appkey_list.append(col)

#print('URLs: ' + str(url_list))
#print('AppKeys: ' + str(appkey_list))  ## UNCOMMENT TO SEE WHAT ITEMS ARE INSIDE APP KEY LIST

a = 1
b = 0
c = 0
d = 0
n = 1

while c < len(url_list) and d < len(appkey_list):
    api = 'https://IOTNOCisLYFE/Thingworx/Subsystems/LicensingSubsystem/Services/GetInstanceId'
    e = url_list[c]
    f = api.replace('IOTNOCisLYFE', e)
    #print(f)
    c += 1


    ##### POST Request #####
    payload = {
               'appkey': 'CS_IOT_IS_THE_BEST!!!',
		       'Content-Type': 'application/json',
		       'Accept': 'application/json'
		      }

    g = appkey_list[d]
    payload['appkey'] = g
    #print(payload)
    d += 1

    try:
        ptc = requests.post(f, headers=payload)

        IDRegex = re.compile(r'\w\w\w\w\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w\w\w\w\w\w\w\w\w')
        filteredID = IDRegex.search(ptc.text)
        print(filteredID.group())
    except AttributeError:
	    print('not found')