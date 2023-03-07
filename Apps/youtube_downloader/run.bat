set /p url=youtube URL:
set /p output=output folder:
' python youtube_downloader.py -u "%url%" -o "%output%"
set pythonpath=D:\DEV\GIT\github-python\
python.exe D:\DEV\GIT\github-python\Apps\youtube_downloader\youtube_downloader.py  -u "%url%"  -o "%output%"
pause
