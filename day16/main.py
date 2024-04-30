#project 1

import requests
import xml.etree.ElementTree as ET


RSS_FEED_URL = "https://www.geeksforgeeks.org/desktop-notifier-python/"



def loadRSS():

    resp = requests.get(RSS_FEED_URL)

    return resp.text

def parseXML(rss):

    root = ET.fromstring(rss)

    newsitems = []

    for item in root.findall('link'):
        print("item",item.text)
        news = {}

        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    return newsitems


def topStories():
    rss = loadRSS()

    newsitems = parseXML(rss)

    return newsitems


print(loadRSS())



#project 2

import platform

# Get operating system information
print(platform.system())
print(platform.release())

# Get processor information
print(platform.processor())

def get_os():
    """Get the operating system."""
    # Read /etc/os-release file to get OS information
    with open('/etc/os-release') as f:
        for line in f:
            print("line",line)
            if line.startswith('NAME='):
                return line.split('=')[1].strip('" \n')
    return "Unknown"

def get_release():
    """Get the release version."""
    # Read /etc/os-release file to get release version
    with open('/etc/os-release') as f:
        for line in f:
            if line.startswith('VERSION='):
                return line.split('=')[1].strip('" \n')
    return "Unknown"

def get_processor():
    """Get the processor information."""
    # Read /proc/cpuinfo file to get processor information
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.startswith('model name'):
                return line.split(':')[1].strip()
    return "Unknown"

def get_machine():
    """Get the machine type."""
    # Read /proc/cpuinfo file to get machine type
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.startswith('machine'):
                return line.split(':')[1].strip()
    return "Unknown"


print(get_os())