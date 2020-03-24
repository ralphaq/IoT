import pushbullet
pb = pushbullet.Pushbullet("access token")

pb.push_note("title", "message")

# to send a file :

with open("file_path", "r")  as f :
  file = pb.upload_file(f, "file.ext")
pb.push_file(**file)
