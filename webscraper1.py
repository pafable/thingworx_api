import requests, openpyxl, os, re, datetime

## Opens precursor spreadsheet ##
wb1 = openpyxl.load_workbook('<ENTER_LOCATION_OF_SPREADSHEET>')
ws1 = wb1.active

def scrapeSheet():
    ##### Creates URL and App key lists #####
    p = ENTER_NUMBER_OF_ROWS
    url_list = []
    for i in range(2,p):
        row = ws1.cell(row=i, column=1).value
        #print(row)
        url_list.append(row)

    appkey_list = []
    for h in range(2,p):
        col = ws1.cell(row=h, column=2).value
        #print(col)
        appkey_list.append(col)

    #print('URLs: ' + str(url_list))         ## UNCOMMENT TO SEE WHAT ITEMS ARE INSIDE URL LIST
    #print('App Keys: ' + str(appkey_list))  ## UNCOMMENT TO SEE WHAT ITEMS ARE INSIDE APP KEY LIST
    c = 0
    d = 0
    b = 0
    a = 1
    n = 1
    while c < len(url_list) and d < len(appkey_list):
        api = 'https://IOTNOCisLYFE/Thingworx/Subsystems/PlatformSubsystem/Services/GetThingworxVersion'
        e = url_list[c]
        f = api.replace('IOTNOCisLYFE', e)
        # print(f)
        c += 1

        ##### POST Request #####
        payload = {'appkey': 'CS_IOT_IS_THE_BEST!!!', 'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        g = appkey_list[d]
        payload['appkey'] = g
        # print(payload)
        d += 1
        ptc = requests.post(f, headers=payload)

        ##### REGEX #####
        twxapiRegex = re.compile(r'\d\.\d\.\d\d?\-\w\d\d\d?') ## FILTERS API OUTPUT AND GRABS TWX VERSION INFO
        filtered = twxapiRegex.search(ptc.text)
        if filtered != None:
            #print(e + ' =' + '=' + '= ' +filtered.group())
            w = e
            m = filtered.group()
            #print(w)
        else:
            m = 'UNKNOWN'
            w = e
            print('[ ERROR ] '+ e + ' did not respond' + '\n')

        ##### Creates new spreadsheet #####
        if b == 0:
            now = datetime.datetime.now()
            now = now.strftime('%Y%m%d')
            out = '<REPLACE_WITH_OUTPUT_LOCATION>/BREH!!!'
            out = out.replace('BREH!!!', 'TWX_VERSIONS_' + now + '.xlsx')
            b += 1
            wb2 = openpyxl.Workbook()
            wb2.save(out)
        else:
            #print('inputs file already exists')
            pass

        #### Fills cells in spreadsheet with version info #####
        s = 'A' + str(a)
        j = 'B' + str(n)
        wb2 = openpyxl.load_workbook(out)
        ws2 = wb2['Sheet']
        ws2[s] = w
        ws2[j] = m
        wb2.save(out)
        print('Writing ' + w + ' to ' + str(s) + ', TWX Version ' + m + ' to ' + str(j) + '\n')
        a += 1
        n += 1

scrapeSheet()
