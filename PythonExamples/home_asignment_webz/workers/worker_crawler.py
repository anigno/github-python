import requests
from bs4 import BeautifulSoup
from PythonExamples.home_asignment_webz.data_access.data_access_base import DataAccessBase
from PythonExamples.home_asignment_webz.logging.logger import Logger
from PythonExamples.home_asignment_webz.management.waitable_queue import WaitableQueue
from PythonExamples.home_asignment_webz.workers.crawler_queue_item import CrawlerQueueItem
from PythonExamples.home_asignment_webz.workers.worker_base import WorkerBase

class WorkerCrawler(WorkerBase):
    """specialized worker for a requested site"""
    cookies = None
    headers = None
    data = None

    def __init__(self, unique_name: str, queue: WaitableQueue, data_access: DataAccessBase):
        super().__init__(unique_name, queue, data_access)

    def login(self, login_url: str):
        """login to specific site with credentials extracted from web browser and curl to python site"""
        Logger.log(f'login url: {login_url}')

        cookies = {
            'bpaf-default-filter': '1',
            'wpforo_read_topics': '%7B%221%22%3A%221%22%7D',
            'wpforo_read_forums': '%7B%226%22%3A%222115%22%7D',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'tk_ai': 'jetpack%3AztTeR8qYyIIEVPpxRp0sbqyG',
        }

        headers = {
            'authority': 'foreternia.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'bpaf-default-filter=1; wpforo_read_topics=%7B%221%22%3A%221%22%7D; wpforo_read_forums=%7B%226%22%3A%222115%22%7D; wordpress_test_cookie=WP%20Cookie%20check; tk_ai=jetpack%3AztTeR8qYyIIEVPpxRp0sbqyG',
            'origin': 'https://foreternia.com',
            'referer': 'https://foreternia.com/wp-login.php',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        }

        data = 'log=temp.anigno%40gmail.com&pwd=ugkJy%296W28F%24rsn%24gtrHm*3C&g-recaptcha-response=03ADUVZwCvX1Sh1dwUSF6dqQvi6zUfq6AnMv7M8P8WGBaqAnYOWHu59fUZpce8xq1b7JEKvSzNMdITKpH1Au-CCI1qRJJvabqsIdYkkd_j_F6vPivRZFWA6hGJ0nQa1yN74YlZPLAaud6C_9w91wbTpMq8qeIW0lOF-zIeu67LxucXNlUHNTyOW8JRURYUhcfXToGmBkHgL_rswG0ssOHBrtbbISWI8dQZH8nDDMfTrhLyl2SVELQVYgr82v7Cls1KSmr2rse0c-GoF_OcZeejIzKQgjNfIrHowaWa4lzPQk_9iWydbmxYiRQNLy4QCqOVYSqSX7NB7xC7rA_yYDrJJmGcMYBKV93x4POMExs83Y-KD3y6bVu7vyVRxDs_R4AlYPLOG7iVjOnd63oAfeZzFYNi6xwR5qplYlILY8jFiaN0dOnWFm5FNxLdRfUkjp_q4CKwiAUKMQFWM2uVKe-AwsBeh_Zc_19XeMsj_VKD_0QWVh2dD3BuTFuRcE0-U145vS6SdvT3hU4njlKxYmrBvwiECXyZ5MtQAmSKo4q9glqTDaCobpBY8VFTOheTCX9cCSO9VF5pGKbWn8zKrTg0wk9fI_AX04KJuezXXQ7OwgzdHHaomcyzCzQ&rememberme=forever&wp-submit=Log+In&redirect_to=https%3A%2F%2Fforeternia.com&testcookie=1'

        login_response = requests.post('https://foreternia.com/wp-login.php', cookies=cookies, headers=headers,
                                       data=data)

        WorkerCrawler.cookies = cookies
        WorkerCrawler.headers = headers
        WorkerCrawler.data = data
        Logger.log(f"login response: {login_response.status_code}")

    def target_method(self):
        while self.is_running:
            queue_item = self.queue.get()
            self.crawl(queue_item)

    def crawl(self, queue_item: CrawlerQueueItem):
        """extraction method for requested site"""
        Logger.log(f'{self.unique_name}->crawling url: {queue_item.url}')
        response = requests.post(queue_item.url, cookies=WorkerCrawler.cookies, headers=WorkerCrawler.headers,
                                 data=WorkerCrawler.data)
        WorkerCrawler.soup = BeautifulSoup(response.content, 'html.parser')

        h2_list = WorkerCrawler.soup.findAll('h2', class_='entry-title')
        for h2 in h2_list:
            a = h2.find('a')
            url = a.attrs['href']
            data = 'h1'
            if WorkerCrawler.history_dict.set_item(url):
                self.queue.put(CrawlerQueueItem(url=url, data='h1'))
                Logger.log(f'{self.unique_name}->added url: {url} data: {data}')
        vcards = WorkerCrawler.soup.findAll('div', class_='comment-author vcard')
        for vcard in vcards:
            a = vcard.findNext('a')
            text = a.text
            t = vcard.findNext('time')
            time = t.text
            content = vcard.findNext('div', 'comment-content')
            ps = content.findAll('p')
            sb = ''
            for p in ps:
                sb += p.text + ' '
            data = {"page_link": queue_item.url,
                    "title": text,
                    "published_time": time,
                    "content": sb}
            self.data_access.save_data(self.unique_name, data)
