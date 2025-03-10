import time
import threading
from main import AutoCrawler

# Cấu hình AutoCrawler
config = {
    "skip_already_exist": True,
    "n_threads": 4,  # Sử dụng 4 luồng
    "do_google": True,
    "do_naver": False,
    "download_path": "download",
    "full_resolution": False,
    "face": False,
    "no_gui": True,
    "limit": 10  # Tải 10 ảnh
}

def crawl_images():
    crawler = AutoCrawler(**config)
    crawler.do_crawling()

def run_multithreading():
    start_time = time.time()
    
    threads = []
    for _ in range(4):  # Tạo 4 luồng
        t = threading.Thread(target=crawl_images)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    
    with open("log.txt", "a") as log_file:
        log_file.write(f"Multithreading - Time Taken: {end_time - start_time:.2f}s\n")

if __name__ == "__main__":
    run_multithreading()
