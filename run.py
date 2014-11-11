#!/usr/bin/python
import gdata.photos.service
import random
import subprocess
import configobj

config = configobj.ConfigObj("config")
email=config["google_login_email"]
password=config["google_login_password"]
other_email=config["google_photos_login_email"]

gd_client = gdata.photos.service.PhotosService()
gd_client.email = email
gd_client.password = password
gd_client.ProgrammaticLogin()

albums = gd_client.GetUserFeed(user=other_email)
count = 0
for album in albums.entry:
  album.count = count
  count += int(album.numphotos.text)

n = random.randint(0, count-1)
for album in albums.entry:
  start = album.count
  end = start + int(album.numphotos)-1
  if n >= start and n <= end:
    chosen_album = album
    break

n = random.randint(0, int(album.numphotos)-1)

photos = gd_client.GetFeed(
    '/data/feed/api/user/%s/albumid/%s?kind=photo&imgmax=d' % (
        other_email, chosen_album.gphoto_id.text))

chosen_photo = photos.entry[n]
photo_url = chosen_photo.content.src
process = subprocess.call(["./set-wallpaper.sh", photo_url])
