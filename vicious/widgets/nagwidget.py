#!/usr/bin/python2

# Widget Nagios pour awesome.

import urllib2, base64, re
 
def request(username, password, url):
        req = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('', '') 
        req.add_header("Authorization", "Basic %s" % base64string)   
        return urllib2.urlopen(req)
 
def parse(result):
        warning, critical, unknown = 0, 0, 0
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
 
        return warning, critical, unknown
 
def end(warning, critical, unknown):
        if (warning == 0 and critical == 0 and unknown == 0):
            print "<b><span color='green'>Ok! ;)</span></b>"
        else:
            print "<b><span color='yellow'>WARN: %s</span>||<span color='red'>CRIT: %s</span>||<span color='orange'> UNK: %s</span></b>" % (warning, critical, unknown) 

if __name__ == "__main__":
        username = 
        password = 
        url = 
 
        result = request(username, password, url)
        warning, critical, unknown = parse(result)
        end(warning, critical, unknown)
