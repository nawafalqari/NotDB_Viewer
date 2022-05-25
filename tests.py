import notdb

db = notdb.NotDBClient(password='123')

# db.files.appendFile('testImage.png', name='logo')
# db.files.removeFile({'name':'license'})
db.files.appendFile('test.txt', name='t')
# db.files.appendFile('testVideo.mp4', name='video')
# db.files.appendFile('testAudio1.m3u', name='audio1')
# db.files.appendFile('testAudio2.mp3', name='audio2')