import win32api
long_file_name='C:\Program Files\I am a file'
short_file_name=win32api.GetShortPathName(long_file_name)