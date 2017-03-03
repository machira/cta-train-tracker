import json
import urllib.parse
import urllib.request

URL = "lapi.transitchicago.com/api/1.0/ttpositions.aspx"
TRAIN_DIRECTION_INTO_LOOP = u'5'
CTA_API_KEY = 'API_KEY_HERE'
example_json_response = """{
   "ctatt":{
      "tmst":"2015-04-30T20:29:44",
      "errCd":"0",
      "errNm":null,
      "route":[
         {
            "@name":"red",
            "train":[
               {
                  "rn":"827",
                  "destSt":"30173",
                  "destNm":"Howard",
                  "trDr":"1",
                  "nextStaId":"40650",
                  "nextStpId":"30125",
                  "nextStaNm":"North/Clybourn",
                  "prdt":"2015-04-30T20:29:24",
                  "arrT":"2015-04-30T20:31:24",
                  "isApp":"0",
                  "isDly":"0",
                  "flags":null,
                  "lat":"41.90383",
                  "lon":"-87.63685",
                  "heading":"269"
               }
            ]
         }
      ]
   }
}"""


def is_train_heading_into_loop(train):
    return train['trDr'] == TRAIN_DIRECTION_INTO_LOOP


def get_all_brown_trains():
    api_url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
    params = {
        'key': CTA_API_KEY,
        'rt': 'brn',
        'outputType': 'JSON'
    }

    param_values = urllib.parse.urlencode(params)
    full_url = api_url + '?' + param_values
    with urllib.request.urlopen(full_url) as response:
        response_text = response.read().decode('utf-8')
        return json_to_map(response_text)


def stops_with_arriving_trains(trains):
    approaching_trains = filter(lambda t: is_train_approaching_station(t) and is_train_heading_into_loop(t), trains)
    return map(lambda t: t['nextStaNm'], approaching_trains)


def format_train(train):
    return {'route_name': train['rn'], 'destination': train['destNm'], 'next_station': train['nextStaNm'],
            'is_approaching': train['isApp']}


def is_train_approaching_station(train):
    return train['isApp'] == u'1'


def json_to_map(json_text):
    response = json.loads(json_text)
    if response["ctatt"][u'errNm'] is not None:
        raise RuntimeError(response[u'errNm'])

    return response["ctatt"]['route'][0]['train']


if __name__ == '__main__':
    all_trains = get_all_brown_trains()
    for i, train in enumerate(all_trains):
        print("Train: %d" % (i + 1))
        print("Next Stop: %s" % ((train['nextStaNm'])))
        print("Heading To: %s" % (train['destNm']))
        print('\n')
