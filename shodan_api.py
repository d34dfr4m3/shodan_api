#!/usr/bin/python3
import json, shodan, sys

key='[CENSURADO]'
api=shodan.Shodan(key)

def search():
    if len(sys.argv) < 1:
        what=input("Search: ")
    else:
        what=sys.argv[1]
    try:
        results = api.search(what)
        for result in results['matches']:
            print('------------------------')
            '''
            print('IP: %s' % result['ip_str'], ' Hostname:', result['hostnames'] )
            print('OS: ', result['os'])
            print(' ')
            '''
            hostsearch(result['ip_str'])
        print(results['total'])
    except Exception as error:
        print("Error: ", error)
def hostsearch(target):
    host =  api.host(target)
    print('''IP: %s
                Organization: %s
                OS:  %s ''' % (host['ip_str'],host.get('org','n/a'), host.get('os', 'n/a' ))) 
    for item in host['data']:
        print("Port: "+str(item['port'])+"\nBanner :"+str(item['data']))
def main():
    print("Come on") 
    search()
main()
