#!/usr/bin/python2
 
import urllib2, base64, re
 
 
def request(username, password, url):
        req = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('', '') 
        req.add_header("Authorization", "Basic %s" % base64string)   
        return urllib2.urlopen(req)
 
def parse(result):
        warning, critical, unknow = 0, 0, 0
        res = result.read()
        #print res
        match = re.findall(r'<td class=.*>(.*)</td>', res)
        if match:
                for state in match:
                        if (state == "WARNING"):
                                warning += 1
                        elif (state == "CRITICAL"):
                                critical += 1
                        elif (state == "UNKNOWN"):
                                unknown += 1
 
        return warning, critical, unknow
 
 
if __name__ == "__main__":
        username = ""
        password = ""
        url = "" 
 
        result = request(username, password, url)
        warning, critical, unknow = parse(result)
        print "<b><span color='yellow'>WARNING: %s</span>||<span color='red'>CRITICAL: %s</span>||<span color='orange'> UNKNOWN: %s</span></b>" % (warning, critical, unknow) 

