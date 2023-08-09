import typer
from Apps.webz_home_asignment.logging.logger import Logger
from Apps.webz_home_asignment.management.config_reader import ConfigReader
from Apps.webz_home_asignment.management.work_manager import WorkManager
from Apps.webz_home_asignment.workers.worker_crawler import WorkerCrawler

class Bootstrapper:
    """main entry point, handle instance creation of main application components"""

    def __init__(self, config_file: str):
        Logger.log('bootstrapper started')
        config_reader = ConfigReader(config_file)
        self.config_dict = config_reader.config_dict
        self.work_manager = WorkManager(self.config_dict['work_manager'], WorkerCrawler)

    def run(self):
        self.work_manager.start(self.config_dict['web_site_data']['url'])

    def stop(self):
        self.work_manager.stop()

if __name__ == '__main__':
    def main(config_file: str):
        bootstrapper = Bootstrapper(config_file)
        bootstrapper.run()
        input()
        bootstrapper.stop()

    typer.run(main)
