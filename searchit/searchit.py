#!/usr/bin/python3
import webbrowser,sys
from time import sleep
from getpass import getuser

def main():
    #check user
    if getuser() == 'root':
        print('This script won\'t run in \'root\' user due to security issues.\nExiting...')
        sys.exit()

    #supported platforms
    platforms = {'google':'https://www.google.com/search?q=',
                 'Google':'https://www.google.com/search?q=',
                 '-g':'https://www.google.com/search?q=',
                 'youtube':'https://www.youtube.com/results?search_query=',
                 'Youtube':'https://www.youtube.com/results?search_query=',
                 'yt':'https://www.youtube.com/results?search_query=',
                 '-yt':'https://www.youtube.com/results?search_query=',
                 '-y':'https://www.youtube.com/results?search_query=',
                 'bing':'https://www.bing.com/search?q=',
                 'Bing':'https://www.bing.com/search?q=',
                 '-b':'https://www.bing.com/search?q=',
                 'amazon':'https://www.amazon.com/s?k=',
                 'Amazon':'https://www.amazon.com/s?k=',
                 '-a':'https://www.amazon.com/s?k=',
                 'facebook':'https://www.facebook.com/search/top/?q=',
                 'fb':'https://www.facebook.com/search/top/?q=',
                 'Facebook':'https://www.facebook.com/search/top/?q=',
                 '-f':'https://www.facebook.com/search/top/?q=',
                 'yandex':'https://yandex.com/search/?text=',
                 'Yandex':'https://yandex.com/search/?text=',
                 '-ya':'https://yandex.com/search/?text=',
                 'Taskbar':'',
                 'taskbar':'',
                 '-tb':'',
                 '-t':''
                 }

    #Take the search query from user
    if len(sys.argv) == 1:
        print('\n\nSearchIt v.1.0 (https://karthikuj.github.io/)\n')
        print('Usage:\tsearchit [platform] [search query]\n')
        print('PLATFORMS SUPPORTED:')
        print('\tSearch in taskbar [Taskbar, taskbar, -tb]')
        print('\tGoogle [Google, google, -g]')
        print('\tYoutube [Youtube, youtube, -yt, yt, -y]')
        print('\tBing [Bing, bing, -b]')
        print('\tFacebook [Facebook, facebook, fb, -f] (you need to be logged in for this)')
        print('\tAmazon [Amazon, amazon, -a]')
        print('\tYandex [Yandex, yandex, -ya]')
        platform = input('\nEnter the platform:  ')
        searchQuery = input('Enter search query:  ')
        if platform not in platforms.keys():
            platform = 'google'
            print('Platform not found! Proceeding with google...\n')
            sleep(2)
    else:
        if sys.argv[1] not in platforms.keys():
            print('Platform not found! Proceeding with google...\n')
            sleep(2)
            platform = 'google'
            searchQuery = ' '.join(sys.argv[1:])
        else:
            platform = sys.argv[1]
            searchQuery = ' '.join(sys.argv[2:])

    #Form a URL
    url = platforms[platform] + searchQuery

    #Open the URL in the browser
    webbrowser.open(url)

