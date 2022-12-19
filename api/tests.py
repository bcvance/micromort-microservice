import json
import os
from django.test import TestCase
from rest_framework.test import APIClient
from parameterized import parameterized


base_path = os.getcwd() + '/api/unit_testing/api_inputs/'

class MicromortsTestCase(TestCase):

    @parameterized.expand([
        # test valid inputs for correct micromort calculation output
        ('com-1', 'com-1.json', 1340),
        ('com-42', 'com-42.json', 578),
        ('com-64', 'com-64.json', 3340),
        # case when micromorts exceed 1,000,000, should return 1,000,000
        ('com-1234', 'com-1234.json', 1000000),
        # case when micromorts are between 0 and 1, should return 1
        ('com-2', 'com-2.json', 1),
    ]
    )
    def test_micromort_endpoint_valid(self, name, input, expected):
        client = APIClient()
        # for each test case, read in corresponding json input file
        file = open(base_path + input)
        json_input = file.read()
        request_json = json.loads(json_input)

        # make request to API
        response = client.post('/api/', request_json)


        response_data = response.data
        print(input, response_data)

        # check that correct output was produced
        assert response.status_code == 200 and response_data['total_micromorts'] == expected

    @parameterized.expand([
        # test invalid inputs

        # invalid commuteID format
        ('com56', 'com56.json', 'commuterId must be in format: COM-[integer]'),
        ('com-abc', 'com-abc.json', 'commuterId must be in format: COM-[integer]'),

        # missing actions key
        ('com-99', 'com-99.json', "Missing key: 'actions'"),

        # missing nested key in actions
        ('com-164', 'com-164.json', "Missing key: 'unit'"),

        # incorrect timestamp (date) format
        ('com-1201', 'com-1201.json', 'ts must be in format: YYYY-MM-DD HH:MM:SS and all values must be in valid range (e.g. month must be in range 1-12, hour in range 0-24'),

        # incorrect timestamp (time) format
        ('com-1202', 'com-1202.json', 'ts must be in format: YYYY-MM-DD HH:MM:SS and all values must be in valid range (e.g. month must be in range 1-12, hour in range 0-24'),

        #
    ])
    def test_micromort_endpoint_invalid(self, name, input, expected):
        client = APIClient()
        # for each test case, read in corresponding json input file
        file = open(base_path + input)
        json_input = file.read()
        request_json = json.loads(json_input)

        # make request to API
        response = client.post('/api/', request_json)


        response_data = response.data
        print(input, response_data)

        # check that correct output was produced
        assert response.status_code == 400 and response_data['error'] == expected
    
