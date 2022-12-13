from devtools.faceinfo import Get_friends_mbasic , Mbasic

cookies = open('.cookies.log','r').read()

Get_friends_mbasic(
        Mbasic.link_pertemanan(query='100052999001915'),
        headers={
            'cookie' : cookies,
            'view_progress': 'yes',
            'spliter': '<=>',
            'file_name': 'dumps.json'
            }
        )

