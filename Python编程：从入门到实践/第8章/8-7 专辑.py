def make_album(singer_name, album, song_number=''):
    singer_album = {'name':str(singer_name), 'album':str(album)}
    if song_number:
        singer_album['number'] = song_number
    return singer_album


print(make_album('周杰伦', '魔杰座', '23'))
print(make_album('周杰伦', '稻香', '24'))
print(make_album('林俊杰', '美人鱼'))