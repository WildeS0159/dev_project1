
import re
import os
import json
import yaml
import xml.etree.ElementTree as ET

def parseYAML(file):
    with open(file,'r') as yaml_file:
        ouryaml = yaml.safe_load(yaml_file)
    print(ouryaml)
    print("The access token is {}".format(ouryaml['access_token']))
    print("The token expires in {} seconds.".format(ouryaml['expires_in']))
    print("This is a Yaml file!")

def parseJSON(file):
    with open(file,'r') as json_file:
        ourjson = json.load(json_file)
    print("The access token is: {}".format(ourjson['access_token']))
    print("The token expires in {} seconds.".format(ourjson['expires_in']))
    print("This is a JSON file!!")

def parseXML(file):
    xml = ET.parse(file)
    root = xml.getroot()
    ns = re.match('{.*}', root.tag).group(0)
    editconf = root.find("{}edit-config".format(ns))
    defop = editconf.find("{}default-operation".format(ns))
    testop = editconf.find("{}test-option".format(ns))
    print("The default-operation contains: {}".format(defop.text))
    print("The test-option contains: {}".format(testop.text))
    print("This is an XML file!!")

def main ():
    file = input("What file would you like to parse?")

    if not os.path.exists(file):
        print("Error: The specified file does not exist.")
        return

    try:
        if file.endswith('.yaml') or file.endswith('.yml'):
            parseYAML(file)
        elif file.endswith('.json'):
            parseJSON(file)
        elif file.endswith('.xml'):
            parseXML(file)
        else:
            print("Error: Unsupported file type. Please provide a YAML, JSON, or XML file.")
            return

    except Exception as e:
        print("Critical Error!!")

if __name__ == "__main__":
    main()