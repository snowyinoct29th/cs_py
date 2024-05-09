import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing
from tqdm import tqdm
import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# 指定 Chromedriver 的安装路径
chrome_driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'


def crawl_buff(page_range, output_file):
    # 你现有的用于爬取buff.163.com的代码
    # 定义伪装的用户代理头和 Cookie
    user_agent = ()
    cookie = ()
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f'--cookie={cookie}')

    # 初始化 Selenium WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开CSV文件
    csv_file_path = 'buff.csv'
    csv_file = open(csv_file_path, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'price_buff'])

    f = True
    flag = 1
    # 循环访问每个页面
    for page in range(1, 749):
        try:
            if not f:
                page = page - 1
                f = True
            url = f"https://buff.163.com/market/csgo#game=csgo&page_num={page}&min_price=0.1&max_price=200&tab=selling"

            driver.get(url)
            # 等待页面加载完成
            wait = WebDriverWait(driver, 10)
            time.sleep(2)
            if page == 1:
                time.sleep(20)
            # 获取页面内容
            html = driver.page_source

            # 使用 BeautifulSoup 解析页面内容
            soup = BeautifulSoup(html, 'html.parser')

            # 循环遍历每个块
            for i in range(1, 20):
                # 提取标题
                title_selector = f'#j_list_card > ul > li:nth-child({i}) > h3 > a'
                title_element = soup.select_one(title_selector)
                title = title_element.get_text(strip=True) if title_element else '未找到'
                # 提取文本
                text_selector = f'#j_list_card > ul > li:nth-child({i}) > p > strong'
                text_element = soup.select_one(text_selector)
                text = text_element.get_text(strip=True) if text_element else '未找到'

                if text == '未找到':
                    f = False

                # 过滤掉不兼容的字符，然后写入CSV文件的新行
                title = title.encode('utf-8', errors='ignore').decode('utf-8')
                text = text.encode('utf-8', errors='ignore').decode('utf-8')
                writer.writerow([title, text])

            print(f"第 {page} 页数据已保存到文件: {csv_file_path}")
            # if page == 615:
            #     page = 1
            #     time.sleep(random.randint(850, 900))
            #     flag = flag + 1
            #     if flag == 10:
            #         break

        except Exception as e:
            print(e)
            print("error in" + str(page))
            continue

    # 关闭CSV文件
    csv_file.close()

    # 关闭浏览器
    driver.quit()


def crawl_c5(page_range, output_file):
    # 你现有的用于爬取c5game.com的代码
    # 定义伪装的用户代理头和 Cookie
    user_agent = ()
    cookie = ()

    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f'--cookie={cookie}')

    # 初始化 Selenium WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    time.sleep(20)

    # 打开CSV文件
    csv_file_path = 'c5.csv'
    csv_file = open(csv_file_path, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'price_c5'])

    # 循环访问每个页面
    for page in range(1, 238):
        try:
            url = f"https://www.c5game.com/csgo?appId=730&page={page}&limit=42&sort=8&changePrice=200&minPrice=0.1&maxPrice=200"
            driver.get(url)
            # 等待页面加载完成
            wait = WebDriverWait(driver, 10)
            # 获取页面内容
            html = driver.page_source

            # 使用 BeautifulSoup 解析页面内容
            soup = BeautifulSoup(html, 'html.parser')

            # 循环遍历每个块
            for i in range(1, 43):
                # 提取标题
                title_selector = f'#market_index > ul > div.el-row > div:nth-child({i}) > a > div > span > span > div > div.li-btm > h4'
                title_element = soup.select_one(title_selector)
                title = title_element.get_text(strip=True) if title_element else '未找到'

                # 提取文本
                text_selector = f'#market_index > ul > div.el-row > div:nth-child({i}) > a > div > span > span > div > div.li-btm > div > div:nth-child(1) > div > div > p'
                text_element = soup.select_one(text_selector)
                text = text_element.get_text(strip=True) if text_element else '未找到'

                # 过滤掉不兼容的字符，然后写入CSV文件的新行
                title = title.encode('utf-8', errors='ignore').decode('utf-8')
                text = text.encode('utf-8', errors='ignore').decode('utf-8')
                writer.writerow([title, text])

            print(f"第 {page} 页数据已保存到文件: {csv_file_path}")
        except Exception as e:
            print(e)
            print("error in" + str(page))
            continue

    # 关闭CSV文件
    csv_file.close()

    # 关闭浏览器
    driver.quit()


def crawl_igxe(page_range, output_file):
    # 你现有的用于爬取igxe.cn的代码
    # 定义伪装的用户代理头和 Cookie
    user_agent = ()
    cookie = ()
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument(f'--cookie={cookie}')

    # 初始化 Selenium WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开CSV文件
    csv_file_path = 'igxe.csv'
    csv_file = open(csv_file_path, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'price_igxe'])

    # 循环访问每个页面
    for page in range(1, 500):
        try:
            url = f"https://www.igxe.cn/market/csgo?price_from=0.1&price_to=200&sort=2&page_no={page}&page_size=20"
            driver.get(url)
            # 等待页面加载完成
            wait = WebDriverWait(driver, 10)
            # 获取页面内容
            html = driver.page_source

            # 使用 BeautifulSoup 解析页面内容
            soup = BeautifulSoup(html, 'html.parser')

            # 循环遍历每个块
            for i in range(1, 20):
                # 提取标题
                title_selector = f'#__layout > div > div.market > div > div.list.list > a:nth-child({i}) > div.name'
                title_element = soup.select_one(title_selector)
                title = title_element.get_text(strip=True) if title_element else '未找到'
                # 提取文本
                text_selector = (f'#__layout > div > div.market > div > div.list.list > a:nth-child({i}) > div.info > '
                                 f'div.price')
                text_element = soup.select_one(text_selector)
                text = text_element.get_text(strip=True) if text_element else '未找到'

                # 过滤掉不兼容的字符，然后写入CSV文件的新行
                title = title.encode('utf-8', errors='ignore').decode('utf-8')
                text = text.encode('utf-8', errors='ignore').decode('utf-8')
                writer.writerow([title, text])

            print(f"第 {page} 页数据已保存到文件: {csv_file_path}")
        except Exception as e:
            print(e)
            print("error in" + str(page))
            continue

    # 关闭CSV文件
    csv_file.close()

    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    # 为每个网站定义页面范围
    buff_pages = range(1, 620)
    c5_pages = range(1, 238)
    igxe_pages = range(1, 556)

    # 定义每个网站的输出文件
    buff_output_file = 'buff_merged.csv'
    c5_output_file = 'c5_merged.csv'
    igxe_output_file = 'igxe_merged.csv'

    # 使用多进程同时运行每个爬取函数
    processes = []

    # Buff.163.com
    buff_process = multiprocessing.Process(target=crawl_buff, args=(buff_pages, buff_output_file))
    processes.append(buff_process)

    # C5game.com
    c5_process = multiprocessing.Process(target=crawl_c5, args=(c5_pages, c5_output_file))
    processes.append(c5_process)

    # Igxe.cn
    igxe_process = multiprocessing.Process(target=crawl_igxe, args=(igxe_pages, igxe_output_file))
    processes.append(igxe_process)

    # 启动所有进程
    for process in processes:
        process.start()

    # 等待所有进程结束
    for process in tqdm(processes, desc="进度"):
        process.join()

    # 如果需要，合并CSV文件
    # 如果需要，你可以在这里编写代码将各个CSV文件合并为一个文件
