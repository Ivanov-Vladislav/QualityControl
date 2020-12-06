import requests

MOUNTEBANK_HOST = "http://localhost"
MOUNTEBANK_URL = MOUNTEBANK_HOST + ":2525"
IMPOSTERS_URL = MOUNTEBANK_URL + "/imposters"

requests.delete(IMPOSTERS_URL)

post_info = requests.post(IMPOSTERS_URL, json={
    "port": 4545,
    "protocol": "http",
    "stubs": [{
        "predicates": [{
            "and": [{
                "equals": {
                    "path": "/rate/usd",
                    "method": "GET"
                }
            }]
        }],
        "responses": [{
            "is": {"body": {"usd": {"rate": 75.43}}}
        }]
    }, {
        "predicates": [{
            "and": [{
                "equals": {
                    "path": "/rate/eur",
                    "method": "GET"
                }
            }]
        }],
        "responses": [{
            "is": {"body": {"eur": {"rate": 90.25}}}
        }]
    }, {
        "responses": [{
            "is": {"statusCode": 400}
        }]
    }]
})

print(post_info)
print(post_info.status_code)

get_info = requests.get('http://localhost:2525/imposters')
print(get_info)
print(get_info.json()['imposters'])