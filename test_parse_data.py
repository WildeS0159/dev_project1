import unittest
from parse_data import  *
import json
import yaml
import xml.etree.ElementTree as ET
from io import StringIO

#Okay, admittedly, all of these unit tests failed spectacularly, I have no idea how to write them, I thought I could do something cute but I was running low on time. I'm sorry.
class parse_data_test(unittest.TestCase):
    def testYAML(self):
        output = parseYAML("C:\VSC_Coding_projects\dev_project1\YAML_Example.yaml")
        self.assertIn("This is a Yaml file!", output)

    def testJSON(self):
        output = parseJSON("C:\VSC_Coding_projects\dev_project1\JSON_Example.json")
        self.assertIn("This is a JSON file!!", output)

    def testXML(self):
        output = parseXML("C:\VSC_Coding_projects\dev_project1\XML_example.xml")
        self.assertIn("This is an XML file!!", output)
if __name__ == "__main__":
    unittest.main()