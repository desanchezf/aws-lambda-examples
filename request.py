


import requests

# El id para los proposals de metaciudad es el 2074
url = "https://webapidev.neuromobile.io/api/v4/proposals?filter[center]=2074"

headers = {
    "accept": "application/json",
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
    "Authorization": "Bearer 5YyWl7EacMj0ymCO7TnlcmVFckzmtA8g5ubn7NvwMaB3bUYZ0bTfssG81D6b"
}

response = requests.get(url, headers=headers)
response_data = response.json()['data']
proposal = {
    'id': '',
    'name': '',
    'description': '',
    'start_date': '',
    'end_date': '',
    'sex': '',
    'age' : '',
    '': '',
}

#for prop in response_data:
    # Do something


# Contenido de la petición
# type(response.__dict__['_content'])


import pdb; pdb.set_trace()


"""
{
   "data":[
      {
         "type":"proposals",
         "id":"313369",
         "attributes":{
            "created-at":"2022-11-22T09:50:03+00:00",
            "updated-at":"2022-11-22T09:50:10+00:00",
            "name":"Bienvenidos a Metaciudad",
            "proposal-type":"center",
            "start-date":"2022-11-19T23:00:00+00:00",
            "end-date":"2024-12-30T23:00:00+00:00",
            "priority":null,
            "description":"<p>Hola! Esperemos que disfrutes de tu nueva ciudad<\\/p>",
            "minimum-age":0,
            "maximum-age":99,
            "sex":[
               "H",
               "M"
            ],
            "custom-target":1,
            "published":1,
            "featured":"0",
            "is-event":"0",
            "event-start-date":null,
            "event-end-date":null,
            "segment-operator-type":"and",
            "publication-requested":0,
            "hide-home":"0",
            "languages":[
               {
                  "code":"es",
                  "name":"Bienvenidos a Metaciudad",
                  "description":"<p>Hola! Esperemos que disfrutes de tu nueva ciudad<\\/p>",
                  "channels":[
                     {
                        "name":"app",
                        "image-url":"https:\\/\\/s3-eu-west-1.amazonaws.com\\/dev.neuromobile.io\\/0168b1fdd3d1d0856994b48a31d3da7bf8c60fc0.png"
                     },
                     {
                        "name":"web",
                        "image-url":""
                     }
                  ]
               }
            ],
            "channels":[
               {
                  "name":"app",
                  "image-url":"https:\\/\\/s3-eu-west-1.amazonaws.com\\/dev.neuromobile.io\\/0168b1fdd3d1d0856994b48a31d3da7bf8c60fc0.png"
               }
            ],
            "calls":0,
            "emails":0,
            "impressions":141,
            "my-impressions":0,
            "my-views":0,
            "shares":0,
            "views":0,
            "likes":0,
            "dislikes":0
         },
         "relationships":{
            "center":{
               "data":{
                  "type":"centers",
                  "id":"2074"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/center"
               }
            },
            "category":{
               "data":{
                  "type":"categories",
                  "id":"369"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/category"
               }
            },
            "commerce":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/commerce"
               }
            },
            "extras":{
               "data":[

               ],
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/extras"
               }
            },
            "staff":{
               "data":{
                  "type":"staff_members",
                  "id":"128"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/staff"
               }
            },
            "campaign":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/campaign"
               }
            },
            "coupon":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/coupon"
               }
            },
            "segments":{
               "data":[

               ],
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369\\/relationships\\/segments"
               }
            }
         },
         "links":{
            "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313369"
         }
      },
      {
         "type":"proposals",
         "id":"313370",
         "attributes":{
            "created-at":"2022-11-22T09:54:31+00:00",
            "updated-at":"2022-11-22T15:06:48+00:00",
            "name":"Visita guiada Teatro Romano",
            "proposal-type":"center",
            "start-date":"2022-11-19T23:00:00+00:00",
            "end-date":"2023-11-30T00:01:00+00:00",
            "priority":null,
            "description":"<p>Disfruta durante el fin de semana de visitas guiadas en el Teatro Romano de Metaciudad. Estaremos encantados de ense\\u00f1arte nuestra maravillosa ciudad<\\/p>",
            "minimum-age":0,
            "maximum-age":99,
            "sex":[
               "H",
               "M"
            ],
            "custom-target":1,
            "published":1,
            "featured":"0",
            "is-event":"1",
            "event-start-date":"2022-12-22T23:00:00+00:00",
            "event-end-date":"2022-12-24T23:00:00+00:00",
            "segment-operator-type":"and",
            "publication-requested":0,
            "hide-home":"0",
            "languages":[
               {
                  "code":"es",
                  "name":"Visita guiada Teatro Romano",
                  "description":"<p>Disfruta durante el fin de semana de visitas guiadas en el Teatro Romano de Metaciudad. Estaremos encantados de ense\\u00f1arte nuestra maravillosa ciudad<\\/p>",
                  "channels":[
                     {
                        "name":"app",
                        "image-url":"https:\\/\\/s3-eu-west-1.amazonaws.com\\/dev.neuromobile.io\\/d9689bfb36294f6c525ab659cb90c7381aa28a3f.png"
                     },
                     {
                        "name":"web",
                        "image-url":""
                     }
                  ]
               }
            ],
            "channels":[
               {
                  "name":"app",
                  "image-url":"https:\\/\\/s3-eu-west-1.amazonaws.com\\/dev.neuromobile.io\\/d9689bfb36294f6c525ab659cb90c7381aa28a3f.png"
               }
            ],
            "calls":0,
            "emails":0,
            "impressions":231,
            "my-impressions":0,
            "my-views":0,
            "shares":0,
            "views":0,
            "likes":1,
            "dislikes":1
         },
         "relationships":{
            "center":{
               "data":{
                  "type":"centers",
                  "id":"2074"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/center"
               }
            },
            "category":{
               "data":{
                  "type":"categories",
                  "id":"3"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/category"
               }
            },
            "commerce":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/commerce"
               }
            },
            "extras":{
               "data":[

               ],
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/extras"
               }
            },
            "staff":{
               "data":{
                  "type":"staff_members",
                  "id":"128"
               },
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/staff"
               }
            },
            "campaign":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/campaign"
               }
            },
            "coupon":{
               "data":null,
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/coupon"
               }
            },
            "segments":{
               "data":[

               ],
               "links":{
                  "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370\\/relationships\\/segments"
               }
            }
         },
         "links":{
            "self":"http:\\/\\/webapidev.neuromobile.io\\/api\\/v4\\/proposals\\/313370"
         }
      }
   ]
}

"""