import json
import os
import unittest

from PythonExamples.home_asignments.home_asignment_webz.management.config_reader import ConfigReader

class ConfigReaderTesting(unittest.TestCase):
    def setUp(self):
        # create sample json file
        self.json_file = 'test.json'
        config_dict = {
            "persons": [
                {"person": {"name": "someone", "id": 123456}},
                {"person": {"name": "someone else", "id": 654321}}
            ]}
        with open('test.json', 'w') as json_file:
            json.dump(config_dict, json_file, indent=4)

    def tearDown(self):
        # clean test json file
        os.remove(self.json_file)

    def test_read(self):
        # prepare
        # run
        reader = ConfigReader(self.json_file)
        # test
        self.assertEqual(len(reader.config_dict["persons"]), 2)
        self.assertEqual(reader.config_dict["persons"][1]["person"]["id"], 654321)
