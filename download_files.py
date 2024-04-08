from os import makedirs, unlink
from os.path import exists, join
from posixpath import basename
from requests import get
from shutil import make_archive, rmtree


def download_file(path:str, url:str):
    with open(path, 'wb' ) as f:
        f.write( get(url).content )


def download(mod, client, message):
    mod_name = mod[0].replace("/", "-")
    path = join('mods', mod_name)
    categories = ""

    for ct in mod[1]['categories']:
        categories += "#" + ct['slug'].replace('-', '_') + " "
    

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
        
    print(f"\33[1;32mDESCARGANDO MOD: \33[35m{mod_name}\33[0m\n")
    
    for count, url in enumerate(mod[1]['dic_list']):
        path_full = join(path, url['game_version'])
        if not exists( path_full ):
            makedirs( path_full )

        print(f"\33[1A\33[1;32m\033[K   - Archivos descargados: \33[33m[{count}]\33[0m")
        
        download_file( #! DESCARGAR MODS
            path=join(path_full, basename(url['url_download'])), 
            url=url['url_download'])


    
    id_chanel = -1002084886563

    make_archive(mod_name, 'zip', path)
    file_zip = mod_name + '.zip'
    client.send_document(
        chat_id=id_chanel, 
        document=file_zip,
        thumb=join(path, "avatar.jpeg"),
        caption=f"__{categories}__\n**__{mod[1]['description']}__**",)
    
    unlink(file_zip)
    rmtree(path)