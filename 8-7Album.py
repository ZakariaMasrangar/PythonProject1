def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('akon', 'mama africa')
print(album)

album = make_album('eminem', 'smack that')
print(album) 

album = make_album('booba', 'saddam haut seine')
print(album)

print("\n")

def make_album(artist, title, tracks=0):

    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('akon', 'mama africa')
print(album)

album = make_album('eminem', 'smack that')
print(album) 

album = make_album('booba', 'saddam haut seine')
print(album)

album = make_album('50 cent', 'if i cant', tracks=8)
print(album)