def make_album(singer_name, album, song_number=''):
    singer_album = {'name':str(singer_name), 'album':str(album)}
    if song_number:
        singer_album['number'] = song_number
    return singer_album


while True:
    singer_name = input("Please input a singer name: ")
    if singer_name == 'Q':
        break
    else:
        album = input("Please input a album name: ")
        print(make_album(singer_name, album))