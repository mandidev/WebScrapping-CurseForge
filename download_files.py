from os import makedirs, unlink
from os.path import exists, join
from posixpath import basename
from requests import get
from shutil import make_archive


def download_file(path:str, url:str):
    with open(path, 'wb' ) as f:
        f.write( get(url).content )

def download(data):
    for mod in data.items():
        mod_name = mod[0].replace("/", "-")
        path = join('mods', mod_name)
        
        if not exists( path ):
            makedirs( path )
            
        download_file( #! DESCARGAR AVATAR
            path=join(path, "avatar.jpeg"),
            url=mod[1]['url_avatar'])

        for i in mod[1]['list_screenshots']:
            path_screenshots = join(path, 'screenshots')
            if not exists(path_screenshots):
                makedirs(path_screenshots)
            download_file( join(path_screenshots, basename(i)), i) #! DESCARGAR SCREENSHOTS
            
        for url in mod[1]['dic_list']:
            path_full = join(path, url['game_version'])
            if not exists( path_full ):
                makedirs( path_full )
            
            download_file( #! DESCARGAR MODS
                path=join(path_full, basename(url['url_download'])), 
                url=url['url_download'])
    
            print("DESCARGADO: " + url['url_download'])
        
        make_archive(mod_name, 'zip', path)