from locust import HttpUser, task, between
from settings import API_KEY_ACCES_LOCAL
import json


data2 = {
  "question": "how many rows are there?",
  "data": {
    "columns": [
        {
            "roles": {
                "values": True
            },
            "type": {
                "underlyingType": 1,
                "category": None,
                "primitiveType": 1,
                "extendedType": 1,
                "categoryString": None,
                "text": True,
                "numeric": False,
                "integer": False,
                "bool": False,
                "dateTime": False,
                "duration": False,
                "binary": False,
                "json": False,
                "none": False
            },
            "displayName": "browser",
            "queryName": "Browsers.browser",
            "expr": {
                "_kind": 2,
                "source": {
                    "_kind": 0,
                    "entity": "Browsers",
                    "variable": "b",
                    "kind": 0
                },
                "ref": "browser",
                "kind": 2
            },
            "sort": 1,
            "sortOrder": 0,
            "rolesIndex": {
                "values": [
                    0
                ]
            },
            "index": 0,
            "identityExprs": [
                {
                    "_kind": 2,
                    "source": {
                        "_kind": 0,
                        "entity": "Browsers",
                        "kind": 0
                    },
                    "ref": "browser",
                    "kind": 2
                }
            ]
        },
        {
            "roles": {
                "values": True
            },
            "type": {
                "underlyingType": 259,
                "category": None,
                "primitiveType": 3,
                "extendedType": 259,
                "categoryString": None,
                "text": False,
                "numeric": True,
                "integer": False,
                "bool": False,
                "dateTime": False,
                "duration": False,
                "binary": False,
                "json": False,
                "none": False
            },
            "displayName": "Visits",
            "queryName": "Sum(Transactions.newVisits)",
            "expr": {
                "_kind": 4,
                "arg": {
                    "_kind": 2,
                    "source": {
                        "_kind": 0,
                        "entity": "Transactions",
                        "variable": "t",
                        "kind": 0
                    },
                    "ref": "newVisits",
                    "kind": 2
                },
                "func": 0,
                "kind": 4
            },
            "rolesIndex": {
                "values": [
                    1
                ]
            },
            "index": 1,
            "isMeasure": True,
            "aggregates": {
                "minLocal": 1,
                "maxLocal": 456122
            }
        }
    ],
    "identity": [
        {
            "identityIndex": 0
        },
        {
            "identityIndex": 1
        },
        {
            "identityIndex": 2
        },
        {
            "identityIndex": 3
        },
        {
            "identityIndex": 4
        },
        {
            "identityIndex": 5
        },
        {
            "identityIndex": 6
        },
        {
            "identityIndex": 7
        },
        {
            "identityIndex": 8
        },
        {
            "identityIndex": 9
        },
        {
            "identityIndex": 10
        },
        {
            "identityIndex": 11
        },
        {
            "identityIndex": 12
        },
        {
            "identityIndex": 13
        },
        {
            "identityIndex": 14
        },
        {
            "identityIndex": 15
        },
        {
            "identityIndex": 16
        },
        {
            "identityIndex": 17
        },
        {
            "identityIndex": 18
        },
        {
            "identityIndex": 19
        },
        {
            "identityIndex": 20
        },
        {
            "identityIndex": 21
        },
        {
            "identityIndex": 22
        },
        {
            "identityIndex": 23
        },
        {
            "identityIndex": 24
        },
        {
            "identityIndex": 25
        },
        {
            "identityIndex": 26
        },
        {
            "identityIndex": 27
        },
        {
            "identityIndex": 28
        },
        {
            "identityIndex": 29
        },
        {
            "identityIndex": 30
        },
        {
            "identityIndex": 31
        },
        {
            "identityIndex": 32
        },
        {
            "identityIndex": 33
        },
        {
            "identityIndex": 34
        },
        {
            "identityIndex": 35
        },
        {
            "identityIndex": 36
        },
        {
            "identityIndex": 37
        },
        {
            "identityIndex": 38
        },
        {
            "identityIndex": 39
        },
        {
            "identityIndex": 40
        },
        {
            "identityIndex": 41
        },
        {
            "identityIndex": 42
        },
        {
            "identityIndex": 43
        },
        {
            "identityIndex": 44
        },
        {
            "identityIndex": 45
        },
        {
            "identityIndex": 46
        },
        {
            "identityIndex": 47
        },
        {
            "identityIndex": 48
        },
        {
            "identityIndex": 49
        },
        {
            "identityIndex": 50
        },
        {
            "identityIndex": 51
        },
        {
            "identityIndex": 52
        },
        {
            "identityIndex": 53
        }
    ],
    "identityFields": [
        {
            "_kind": 2,
            "source": {
                "_kind": 0,
                "entity": "Browsers",
                "kind": 0
            },
            "ref": "browser",
            "kind": 2
        }
    ],
    "rows": [
        [
            "(not set)",
            8
        ],
        [
            "[Use default User-agent string] LIVRENPOCHE",
            1
        ],
        [
            "0",
            7
        ],
        [
            "ADM",
            1
        ],
        [
            "Amazon Silk",
            429
        ],
        [
            "Android Browser",
            490
        ],
        [
            "Android Runtime",
            2
        ],
        [
            "Android Webview",
            7051
        ],
        [
            "Apple-iPhone7C2",
            9
        ],
        [
            "BlackBerry",
            173
        ],
        [
            "Changa 99695759",
            1
        ],
        [
            "Chrome",
            456122
        ],
        [
            "Coc Coc",
            692
        ],
        [
            "CSM Click",
            1
        ],
        [
            "DASH_JR_3G",
            1
        ],
        [
            "DoCoMo",
            1
        ],
        [
            "Edge",
            8761
        ],
        [
            "Firefox",
            31214
        ],
        [
            "Hisense M20-M_LTE",
            1
        ],
        [
            "HTC802t_TD",
            1
        ],
        [
            "IE with Chrome Frame",
            1
        ],
        [
            "Internet Explorer",
            17481
        ],
        [
            "Iron",
            33
        ],
        [
            "Konqueror",
            1
        ],
        [
            "Lunascape",
            5
        ],
        [
            "LYF_LS_4002_11",
            3
        ],
        [
            "LYF_LS_4002_12",
            18
        ],
        [
            "M5",
            1
        ],
        [
            "Maxthon",
            217
        ],
        [
            "Mozilla",
            10
        ],
        [
            "Mozilla Compatible Agent",
            281
        ],
        [
            "MQQBrowser",
            2
        ],
        [
            "MRCHROME",
            261
        ],
        [
            "Nichrome",
            7
        ],
        [
            "Nintendo Browser",
            120
        ],
        [
            "Nokia Browser",
            63
        ],
        [
            "NokiaE52-1",
            2
        ],
        [
            "no-ua",
            2
        ],
        [
            "Opera",
            5159
        ],
        [
            "Opera Mini",
            5826
        ],
        [
            "osee2unifiedRelease",
            5
        ],
        [
            "Puffin",
            91
        ],
        [
            "Reddit",
            1
        ],
        [
            "Safari",
            156127
        ],
        [
            "Safari (in-app)",
            6274
        ],
        [
            "SeaMonkey",
            15
        ],
        [
            "Seznam",
            6
        ],
        [
            "subjectAgent: NoticiasBoom",
            1
        ],
        [
            "TCL P500M",
            1
        ],
        [
            "ThumbSniper",
            3
        ],
        [
            "UC Browser",
            2231
        ],
        [
            "User Agent",
            1
        ],
        [
            "YaBrowser",
            1971
        ],
        [
            "YE",
            2
        ]
    ]
}
}

with open('data_testing.json', 'r') as archivo:
    data = json.load(archivo)
print(data)



class MyUser(HttpUser):
    wait_time = between(5, 9)  # Tiempo de espera entre las tareas

    '''
    @task
    def query_json_llama2(self):
        data = {
            "columns": [{"displayName": "columna1"}, {"displayName": "columna2"}],
            "rows": [{"columna1": "valor1", "columna2": "valor2"}],
        }
        headers = {"x-api-key": API_KEY_ACCES_LOCAL}
        response = self.client.post("/query_json_llama2", json={"question": "tu pregunta aquí", "data": data}, headers=headers)
        print(response.text)  # Puedes imprimir la respuesta para verificar si es exitosa

    '''

    @task
    def query_json_openai(self):
        headers = {"x-api-key": API_KEY_ACCES_LOCAL}
        response = self.client.post("/query_json_openai", json=data, headers=headers)
        print("Respuesta",response.text)  # Puedes imprimir la respuesta para verificar si es exitosa
