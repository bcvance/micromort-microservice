import json
from django.test import TestCase
from rest_framework.test import APIClient
from parameterized import parameterized


base_path = '/Users/b.vance/Coding Projects/micromort/unit_testing/api_inputs/'
api_url = "http://127.0.0.1:8000/api/"

test_pairs = [
    ('com-1.json', 1340),
    ('com-42.json', 578),
    ('com-64.json', 3340)
    ]

# def test_micromort_endpoint(input, output):
#     print('done')
    # client = APIClient()
    # for each test case, read in corresponding json input file
    # file = open(base_path + input)
    # json_input = file.read()
    # request_json = json.loads(json_input)
    # # print(request_json)

    # # make request to API
    # response = client.post('/api/', request_json, format={'json'})

    #response_json = json.loads(response.text)

    #print(response_json)

    # check that correct output was produced
   # assert response.status_code == 200 and response_json['total_micromorts'] == output

class MicromortsTestCase(TestCase):
    @parameterized.expand(
        test_pairs = [
        ('com-1', 'com-1.json', 1340),
        ('com-42', 'com-42.json', 578),
        ('com-64', 'com-64.json', 3340)
        ]
    )
    def test_micromort_endpoint(self, name, input, output):
        client = APIClient()
        # for each test case, read in corresponding json input file
        file = open(base_path + input)
        json_input = file.read()
        request_json = json.loads(json_input)
        # print(request_json)

        # make request to API
        response = client.post('/api/', request_json, format={'json'})

        response_json = json.loads(response.text)

        print(response_json)

        # check that correct output was produced
        assert response.status_code == 200 and response_json['total_micromorts'] == output
