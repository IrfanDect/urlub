#!/usr/bin/python3
# -- name_tool : faceinfo
# -- version  : 0.1.1

from bs4 import BeautifulSoup
import requests
import re
import json
from rich import print, box
from rich.table import Table  

def HB():
    return {
    "user-agent" : "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36",                                                  "referer": "https://www.facebook.com/",
    "host": "business.facebook.com",
    "origin": "https://business.facebook.com",
    "upgrade-insecure-requests" : "1",
    "accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control" : "max-age=0",
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "content-type":"text/html; charset=utf-8",
    }
def HA():
    return {
    'hostname':'facebook.com',
    'port' : '443',
    'path': None,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
    'accept': 'text/html,application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

# // Graph_ url 
class Graph_:
    """ 
    : url_graph
    -------------
    1. link_pertemanan -> default
    2. link_pengikut 
    3. link_informasi
    """
    @classmethod
    def link_pertemanan(self, query: "me" , limit_count: int, token: None , fields_: None ):
        self.query = query
        self.limit_count = limit_count
        self.token = token
        self.fields_ = fields_ 
        if self.fields_ == 'default':
            return str(f"https://graph.facebook.com/v14.0/{query}?fields=friends.fields(id,name).limit({limit_count})&access_token={token}")
        else:
            return str(f"https://graph.facebook.com/v15.0/{query}?fields=friends.fields({fields_}).limit({limit_count})&access_token={token}")
    @classmethod
    def link_pengikut(self, query: "me" , limit_count: int , token: None):
        self.query = query
        self.limit_count = limit_count
        self.token = token 
        return str(f"https://graph.facebook.com/{query}/subscribers?limit={limit_count}&access_token={token}")
    @classmethod
    def link_informasi(self, query : "me", token : None):
        self.query = query
        self.token = token
        return str(f"https://graph.facebook.com/{query}?access_token={token}")
    @classmethod
    def link_post(self, query : "me", limit_count : int ,token : None):
        self.query = query
        self.token = token
        self.limit_count = limit_count
        return str(f"https://graph.facebook.com/{query}?fields=name,likes.fields(id,name).limit({limit_count})&access_token={token}")

# Mbasic url 
class Mbasic:
    @classmethod
    def link_aplikasi(self, type_check : "active" ):
        self.type_check = type_check
        return str(f"https://mbasic.facebook.com/settings/apps/tabbed/?tab={type_check}")
    @classmethod
    def link_pertemanan(self, query):
        self.query = query
        return str(f"https://mbasic.facebook.com/profile.php?id={self.query}&v=friends")

# file _check
class Fields:
        fil = [
            "id",
            "about",
            "birthday",
            "education",
            "favorite_teams",
            "first_name",
            "gender",
            "hometown",
            "last_name",
            "link",
            "location",
            "locale",
            "middle_name",
            "name",
            "relationship_status",
            "sports",
            "quotes",
            "timezone",
            "updated_time",
            "username",
            "work",
        ]

# ambil Token ..
class Get_token:
    type_tokens = {
            'EAAG' : 'G',
            'EAAB' : 'B', #segera datang
            'EAAA' : 'A', #segera datang
            'all' : 'all' #segera datang
            }
    def __init__(self , cookies: None , type_token : None = type_tokens['EAAG'] ):
        self.respone = requests.get(
                'https://business.facebook.com/business_locations',
                headers={
                    'user-agent': HB()['user-agent'],
                    'host': HB()['host'],
                    'origin': HB()['origin'],
                    'upgrade-insecure-requests': HB()['upgrade-insecure-requests'],
                    'accept-language': HB()['accept-language'],
                    'cache-control': HB()['cache-control'],
                    'accept': HB()['accept'],
                    'content-type': HB()['content-type'],
                    'cookie': cookies
                }
            ) 
        self.type_token = type_token
        self.cookies = cookies
    def __repr__(self):
        if self.type_token == self.type_tokens['EAAG']:
            return str(re.search(r'(\["EAAG\w+)', self.respone.text).group(1).replace('["',''))
        else:
            raise SystemExit(1)

# dump info 
class Get_info:
    def __init__(self, url_ : None , headers : None) -> Graph_:
        with requests.Session() as resp:
            self.js = json.loads(resp.get(url_ , headers=headers).text)
        self.url_ = url_
        self.headers = headers
    def __repr__(self):
        return str(self.js)

# dump id pertemanan 
class Get_friends:
    def __init__(self, url_: None , headers: None ) -> Graph_:
        with requests.Session() as resp:
            self.js = json.loads(resp.get(url_ , headers=headers).text)
        self.url_ = url_
        self.headers = headers
    def __repr__(self):
        return str(self.js)# [data] **kwargs

# dump id pengikut
class Get_followers:
    def __init__(self, url_: None , headers: None ) -> Graph_:
        with requests.Session() as resp:
            self.js = json.loads(resp.get(url_ , headers=headers).text)
        self.url_ = url_
        self.headers = headers
    def __repr__(self):
        return str(self.js)# [data] **kwargs

# // find id facebook 
class Find_username: 
    def __init__(self, link_profile : str ):
        resp = BeautifulSoup(
                requests.Session().get(
                    link_profile,
                    headers={
                        'hostname': HA()['hostname'],
                        'port': HA()['port'],
                        'path': link_profile,
                        'user-agent': HA()['user-agent'],
                        'Accept-Language': HA()['Accept-Language'],
                        'accept': HA()['accept']
                        } 
                    ).content, features='html.parser'
                )
        self.link_profile = link_profile
        self.get_ = resp.find_all('a')[2:3]
    def __repr__(self):
        for super_get in self.get_:
            return super_get['href'].split('=')[4].replace('&refid','')

# dump aplikasi
class Get_application:
    apk_save = []
    def __init__(self, url_: None , headers: None ):
        with requests.Session() as respone:
            r = BeautifulSoup(respone.get(url_, headers=headers).content,features='html.parser')
            for get_ap in r.find_all('h3'):
                bagi_ = get_ap.text.replace(f"{headers['status']}", f"≈{headers['status']}≈")
                createing_dict = bagi_.split('≈')
                self.apk_save.append(
                        {
                            "$aplikasi" : createing_dict[0],
                            "$status": createing_dict[1],
                            "$tahun": createing_dict[2],
                            },
                        )
            for get_fu in r.find_all('a',string='Lihat Lainnya'):
                Get_application("https://mbasic.facebook.com/"+get_fu['href'],headers=headers)
        self.url_ = url_
        self.headers = headers

# replace aplikasi
class Replace_application:
    def __init__(self, text: str, type_replace : None):
        self.text = text 
        self.type_replace = type_replace
    def __repr__(self):
        if self.type_replace == 'kedaluwarsa':
            return str(self.text.replace('Kedaluwarsa',' Kedaluwarsa'))
        elif self.type_replace == 'ditambahkan':
            return str(self.text.replace('Ditambahkan',' Ditambahkan'))
        elif self.type_replace == 'dihapus':
            return str(self.text.replace('Dihapus',' Dihapus'))
        else:
            return str(self.text)

# // dumps pertemanan mbasic with cookies -> note : belum selesai 
class Get_friends_mbasic:
    pertemanan_save = []
    def __init__(self, url_ : None, headers : None ):
        filt = open(headers['file_name'],'a+')
        with requests.Session() as respone:
            r = BeautifulSoup(respone.get(url_ , headers=headers).content , features='html.parser')
            get_friends = r.find_all("td", attrs={"style": "vertical-align: middle"})
            try:
                for banzo in get_friends:
                    for super_get in banzo.find_all('a'):
                        if '/profile.php?id' in super_get['href']:
                            nama_none_replace = (super_get.text.replace('Tambah Teman',''))
                            id_ = (super_get['href'].split('=')[1].replace('&eav',''))
                            nama_ = (nama_none_replace.split('=')[0])
                            self.pertemanan_save.append(
                                {
                                    '$id': id_,
                                    '$name': nama_,
                                    }
                                )
                            filt.write(f"{id_}" +headers['spliter']+ f"{nama_}"+"\n")
                            if 'yes' in (headers['view_progress']):
                                self.view_progress_dumps(idz=id_ , name=nama_ , href_=super_get['href'])
                            else:
                                pass
                for get_fuf in r.find_all("a",string="Lihat Teman Lain"):
                    Get_friends_mbasic("https://mbasic.facebook.com/"+get_fuf['href'],headers)
            except (KeyError): 
                print('[red bold]✘ error...[white] -> ([green]headers[white] : spliter, view_progress, file_name)')
        self.url_ = url_
        self.headers = headers
    @staticmethod
    def view_progress_dumps(idz : str, name : str , href_ : str):
        table = Table(
                "id", "username", "href" ,
                highlight=True,
                box=box.SQUARE_DOUBLE_HEAD,
                header_style="green bold",
                border_style="blue bold"
                )
        table.add_row(f"{idz}", f"[white bold]{name}[reset]", f"{href_}")
        print(table)

