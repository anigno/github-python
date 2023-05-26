import argparse
import logging
import os
from os import path
from typing import Optional
from pytube import YouTube

from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

class YouTubeDownloader:
    def __init__(self):
        LoggingInitiatorByCode()
        # self.logger = logging.getLogger('main_logger')
        self.logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)
        self.logger.info('YouTubeDownloader started')
        self.args: Optional[argparse.Namespace] = None
        self.youtube_downloader: Optional[YouTube] = None
        self.init_argparse()
        self.download()

    def init_argparse(self):
        arg_parser = argparse.ArgumentParser(description='YouTube downloader')
        arg_parser.add_argument('--url', '-u', type=str, required=True, help='youtube video url')
        arg_parser.add_argument('--output', '-o', type=str, required=True, help='output path')
        self.args = arg_parser.parse_args()

    def download(self):
        url_string = self.args.url
        output_folder = self.args.output
        if not path.exists(output_folder):
            os.mkdir(output_folder)
        yt = YouTube(url_string)
        self.logger.debug(f'preparing: {url_string}')
        mp4_files = yt.streams.filter(file_extension='mp4')
        highest_res = mp4_files.get_highest_resolution()
        self.logger.debug(
            f' start download: [{highest_res.default_filename}] '
            f'at resolution: {highest_res.resolution} size: {int(highest_res.filesize / 1024 / 1024)}M')
        highest_res.download(output_path=output_folder, filename=highest_res.default_filename)
        self.logger.debug(f' finished download: [{highest_res.default_filename}]')

if __name__ == '__main__':
    ytd = YouTubeDownloader()
