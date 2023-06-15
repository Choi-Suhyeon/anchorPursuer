from requests.exceptions import ConnectionError
from requests import Response
from bs4 import BeautifulSoup
from threading import Thread

import requests
import atexit
import sys
import io


@atexit.register
def save_result():
    with open('./result.txt', 'wt') as f:
        f.write(output.getvalue())
        
    output.close()


def parse_argv() -> tuple[str, int] | None:
    if len(sys.argv) != 3:
        print(f'syntax: {sys.argv[0]} <ip or domain> <depth>')
        print(f'sample: {sys.argv[0]} www.naver.com 3')
        sys.exit(1)
    
    target, depth = sys.argv[1:]
    
    if not depth.isdecimal() or (depth := int(depth)) not in range(1, 4):
        print('error: depth must be an integer between 1 and 3')
        sys.exit(1)
        
    return target, depth


def start_getting_anchor_addrs(target: str, depth: int):
    get_anchor_addrs(target, depth, (), frozenset())


def get_anchor_addrs(target: str, depth: int, direct_line: tuple[str], ancestors: frozenset[str]):
    def send_output(direct_line: tuple[str], result: frozenset[str]):
        print(f'[{direct_line[-1]} :: {" >> ".join(direct_line[:-1])}]', file=output)
         
        for h, _, _ in result: print('\t|', h, file=output)
            
        print('', file= output)
        
    
    def get_res_only_200(url: str) -> Response | None:
        return res if (res := requests.get(url)).status_code == 200 else None
    
    
    if not depth: return
    
    res: Response
    
    try:                    res = get_res_only_200(target)
    except ConnectionError: return
    else:                   res.close()
    
    if not res: return
    
    new_direct_line = direct_line + (target,)
    result          = frozenset(
        (ahref, depth - 1, new_direct_line) 
            for a in BeautifulSoup(res.text, 'html.parser').find_all('a') 
            if (
                True
                and not (ahref := a.get('href', '')).isspace() 
                and ahref not in ancestors 
                and ahref.startswith('http')
            )
    )
    rslt_only_href  = frozenset(href for href, _, _ in result)
    threads         = tuple(Thread(target=get_anchor_addrs, args=r + (ancestors | rslt_only_href,)) for r in result)
    
    send_output(new_direct_line, result)
    
    for f in (Thread.start, Thread.join):
        for t in threads: f(t)


if __name__ == '__main__':
    output = io.StringIO()

    start_getting_anchor_addrs(*parse_argv())
    
    