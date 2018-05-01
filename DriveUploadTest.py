from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

test_file = drive.CreateFile({'title': 'test.csv'})
test_file.SetContentFile('test.csv')
test_file.Upload({'convert': True})
