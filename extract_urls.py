import sys
from xml.etree import ElementTree as ET

# Read the entire input as a string
input_xml = sys.stdin.read()

# Parse the input string as XML
root = ET.fromstring(f"<root>{input_xml}</root>")

# Find and print all the URLs within <loc> tags
for loc in root.findall('.//loc'):
    print(loc.text)

