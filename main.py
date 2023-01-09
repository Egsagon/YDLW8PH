'''
    main.py
'''

import core

raw = '''
# Add URLs here



# EOF
'''

verbose = False

for i, url in enumerate([l.strip() for l in raw.split('\n') if l and l[0] != '#']):
    
    if not 'viewkey=' in url:
        print(f'[ SLF ] Invalid URL: \033[91m{url}\033[0m')
        continue
        
    core.download(url, f'./output/{i}.mp4', verbose)

