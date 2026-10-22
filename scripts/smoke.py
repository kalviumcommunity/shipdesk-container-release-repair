import json
import sys
import time
import urllib.request

base = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8080'
expected = {'/health': {'status': 'ok'},
            '/config': {'service': 'ShipDesk', 'mode': 'production', 'version': '1.1.0'}}
for path, body in expected.items():
    for attempt in range(20):
        try:
            with urllib.request.urlopen(base + path, timeout=2) as response:
                actual = json.load(response)
                assert response.status == 200 and actual == body, (path, actual)
            break
        except (OSError, AssertionError):
            if attempt == 19:
                raise
            time.sleep(0.5)
    print('PASS', path, json.dumps(actual))
