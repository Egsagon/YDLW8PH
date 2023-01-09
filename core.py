'''
    core.py
'''

import os
import youtube_dl as ytdl

WIDTH = os.get_terminal_size().columns

class Log:
    def __init__(self, on_line: callable) -> None: self.cback = on_line
    
    # Write functions
    def flush(*_) -> None: pass
    def write(self, line: str): self.cback(line)

def download(url: str, path: str, verbose: bool = True) -> None:
    '''
    Download a single file.
    '''
    
    token = url.split('viewkey=')[1]
    
    print(f'[ YTDL ] \033[93m{token}\033[0m:')
    
    params = {
        'format': 'best',
        'playliststart:': 1,
        'playlistend': 4,
        'outtmpl': path,
        'nooverwrites': True,
        'no_warnings': True,
        'ignoreerrors': True,
    }
    
    def on_log(line: str) -> None:
        line = line.replace('\n', '|||').replace('\r', '')\
                   .replace('[download]', '').strip()
        
        if 'Hub] ' + token in line:
            line = line.split(token + ': ')[1]
            
        print(f'\r\t \033[93m*\033[0m {line}'.ljust(WIDTH, '¤').rstrip().replace('¤', ' '),
              end = '\n' if verbose else '')
    
    with ytdl.YoutubeDL(params, sf = Log(on_log)) as dl:
        dl.download([url])

# EOF