"""getFiles.py - given a url, downloads it and all it's linked files """
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"


import sys
import re
import urllib

def readURL(f):
    pass

def dealWithDots(mainURL,subURL):
    dirList = mainURL.strip().split("/")
    dirList.reverse()
    #count the number of .. in the subURL
    c = 1
    subURLFolders = subURL.strip().split("/")
    subFile = subURLFolders[-1]
    for folder in subURLFolders:
        if folder == "..":
            c = c + 1
    
    subURLList = []
    subURLList.append(subURLFolders[-1])
    theList = dirList[c:]
    theList.reverse()
    theList.append(subURLFolders[-1])
    output = ""
    for item in theList:
        output = output + '/' + item 
    output = output[1:]
    return output

    
def getFileList(s):
    hrefList = re.findall(re.compile("<a.href=.*/a>"),text)
    hrefDic = {} #url:name
    for href in hrefList:
        #print href
        #<a href="../../index.html">NetworkX Home </a>
        url = href.strip().split('href=\"')[1].strip().split('\">')[0]
        if '..' in url:
            url = dealWithDots(mainURL,url)
        #print url
        name = href.strip().split('</a>')[0].strip().split('\">')[1].strip()
        #print url,name
        if url in hrefDic:
            pass
        else:
            hrefDic[url] = name
    return hrefDic

def getFile(url,outFile):
    oF = open(outFile,"w")
    oF.write(urllib.urlopen(url).read())
    oF.close()
    
    

mainURL = "http://networkx.lanl.gov/examples/3d_drawing/mayavi2_spring.html"


f = open(sys.argv[1],'r')
text = f.read()
#print text

fileList = getFileList(text)

for url in fileList:
    print "now saving ...", fileList[url] , " from ", url
    getFile(url,fileList[url])

