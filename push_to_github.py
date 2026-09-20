import json, base64, urllib.request, subprocess

TOKEN = 'REDACTED'  # set via environment variable or secret manager
API_URL = 'https://api.github.com/repos/gstokes/dashboard/contents/index.html'

get_req = urllib.request.Request(API_URL, headers={'Authorization': 'token ' + TOKEN, 'Accept': 'application/vnd.github+json'})
with urllib.request.urlopen(get_req) as r:
    file_info = json.loads(r.read())
sha = file_info['sha']

with open('index.html', 'rb') as f:
    content = base64.b64encode(f.read()).decode('utf-8')

today = subprocess.check_output("date +'%d %b %Y'", shell=True).decode().strip()
payload = json.dumps({'message': 'Dashboard update ' + today + ' - automated', 'content': content, 'sha': sha}).encode('utf-8')

put_req = urllib.request.Request(API_URL, data=payload, method='PUT', headers={'Authorization': 'token ' + TOKEN, 'Content-Type': 'application/json', 'Accept': 'application/vnd.github+json'})
try:
    with urllib.request.urlopen(put_req) as r:
        result = json.loads(r.read())
        print('SUCCESS - commit:', result['commit']['sha'])
except urllib.error.HTTPError as e:
    print('FAILED', e.code, e.read().decode())
