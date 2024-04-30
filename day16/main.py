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



#project 3

import random

def getDigits(num):
    return [int(i) for i in str(num)]



def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False



def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num





def numOfBullsCows(num,guess):
    bull_cow = [0,0]

    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] +=1
            else:
                bull_cow[1] +=1
    return bull_cow




num = generateNum()

tries = int(input("enter number of tries: "))

while tries > 0:
    print("these many tries you have",tries)

    guess = int(input("Enter your guess: "))

    if not noDuplicates(guess):
        print("NUmber should not have repeated digits.try again ")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only try again")
        continue
    bull_cow = numOfBullsCows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1

    if bull_cow[0] == 4:
        print("you guessed right!")
        break
else:
    print(f"you ran out of tries Number was {num}")