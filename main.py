from devtools.faceinfo import Graph_ , Get_info , Get_token, Get_friends, Find_username
from devtools.input_dengan_readlike import session
from rich import print, box 
from rich.panel import Panel 
from rich.align import Align
from rich.table import Table
import re
from os import system as clear_sreen


def FILE_CHECK_LOGIN():
    return {
            'token_dict': open('.token.log','r').read(),
            'cookies_dict': open('.cookies.log','r').read()
        }

def dumps_data_value(cursor : str):
    data = Get_info(Graph_.link_informasi(query=cursor,token=FILE_CHECK_LOGIN()['token_dict']),
                    headers={
                        'cookie': FILE_CHECK_LOGIN()['cookies_dict']
                        }
                    )
    print(data.js)

def login_data_value():
    COOKIES_FILE = open('.cookies.log','w+') 
    TOKEN_FILE = open('.token.log','w+')
    # // ses...
    prompt = session.prompt_readlike('(cookies) ',completer=[FILE_CHECK_LOGIN()['cookies_dict']], keybind='tab')
    val = Get_token(cookies=prompt, type_token='G')
    COOKIES_FILE.write(str(prompt))
    TOKEN_FILE.write(str(val))
    
def menu_items_value():
    clear_sreen('clear')
    yourlist = ['example login','example get_informasi_target','example finder_id']
    table = Table("#", "description", "token_view", border_style="blue bold", box=box.SQUARE_DOUBLE_HEAD)
    try:
        for count, get_v in enumerate(yourlist,1):
            table.add_row(f"{count}", f"{get_v}", f"[green]{FILE_CHECK_LOGIN()['token_dict']}[reset]")
        print(table)
    finally: pass
    while True:
        prompt = session.prompt_readlike(
                '(select) ',completer=[
                    'number=',
                    'target=',
                    'cookies=',
                    'select_table',
                    ], keybind='tab'
                )
        for datar in re.findall('select_table --number(.*) --target=(.*)',prompt):
            if '2' in datar[0]:
                dumps_data_value(datar[1])
            elif '3' in datar[0]:
                userid = Find_username(datar[1])
                print(userid)
            else:
                print("[red bold]error...")

menu_items_value()
