import typer
from PythonExamples.home_asignment_webz.logging.logger import Logger
from PythonExamples.home_asignment_webz.management.config_reader import ConfigReader
from PythonExamples.home_asignment_webz.management.work_manager import WorkManager
from PythonExamples.home_asignment_webz.workers.worker_crawler import WorkerCrawler

class Bootstrapper:
    """main entry point, handle instance creation of main application components"""

    def __init__(self, config_file: str):
        Logger.log('bootstrapper started')
        config_reader = ConfigReader(config_file)
        self.config_dict = config_reader.config_dict
        self.work_manager = WorkManager(self.config_dict['work_manager'], WorkerCrawler)

    def run(self):
        url = self.config_dict['web_site_data']['url']
        login_url = self.config_dict['web_site_data']['login_url']
        self.work_manager.start(url, login_url)

    def stop(self):
        self.work_manager.stop()

if __name__ == '__main__':
    def main(config_file: str):
        bootstrapper = Bootstrapper(config_file)
        bootstrapper.run()
        input()
        bootstrapper.stop()

    typer.run(main)
