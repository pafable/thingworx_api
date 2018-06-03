'''
This will provide info on active threads and core pool size. 
Active threads should never be greater than or equal to core pool size for more than 5 mins.
'''
import json, requests

##### POST REQUEST - Interacts with TWX API to find threads #####
urlInput = '<ENTER_URL_HERE>'
urlAppKey = '<ENTER_APP_KEY_HERE>'

url = 'https://SOMEURL/Thingworx/Subsystems/EventProcessingSubsystem/Services/GetPerformanceMetrics'
url = url.replace('SOMEURL', urlInput)

payload = {'appkey': 'SOME_APPKEY', 'Content-Type': 'application/json', 'Accept': 'application/json'}
payload['appkey'] = urlAppKey

postTxt = requests.post(url, headers=payload)
postTxt = postTxt.text
#print(postTxt + '\n')


##### Convert to JSON #####
jsonTxt = json.loads(postTxt)

metricDict = dict() ## Takes data from jsonTxt and puts it into a dictionary called metricDict
for item in jsonTxt['rows']:
    dict_key = item['name']
    dict_value = item['value']
    #print(dict_key, dict_value) ## Prints each entry from jsonTxt before entering into metricDict. Uncomment to TSHOOT
    metricDict[dict_key] = dict_value

print('Core Pool size: ' + str(metricDict['corePoolSize']))
print('Active Threads: ' + str(metricDict['activeThreads']))

actThread = int(metricDict['activeThreads'])
cPoolSize = int(metricDict['corePoolSize'])


##### If statement to output condition of threads ######
if actThread >= cPoolSize:
    print('\n' + 'Threads (CRITICAL): ' + str(actThread))
else:
    print('\n' + 'Threads are good breh')
