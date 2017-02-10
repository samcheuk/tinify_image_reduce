import requests
import os
import json
import urllib
import time

tiny_api = 'PUT YOUR API KEY'

image_paths = [
'put/your/images.paths',
]

for image_path in image_paths:
    os.system('ls -al ' + image_path)
    auth = ('api', )
    data = {'source': open(image_path, 'rb')}
    response = requests.post('https://api.tinify.com/shrink', auth=auth, data=open(image_path, 'rb'))
    try:
        response_json = json.loads(response.content)
        tiny_url = response_json['output']['url']
        urllib.urlretrieve(tiny_url, image_path)
        os.system('ls -al ' + image_path)
    except Exception, e:
        print '!!! Error'
        print response.content
    print '********'
    time.sleep(0.3)
