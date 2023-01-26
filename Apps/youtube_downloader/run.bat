set /p url=youtube URL:
set /p output=output folder:
python youtube_downloader.py -u "%url%" -o "%output%"
