import time
import multiprocessing
from main import AutoCrawler

# Cấu hình AutoCrawler
config = {
    "skip_already_exist": True,
    "n_threads": 4,  # Chạy với nhiều tiến trình
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

def run_multiprocessing():
    start_time = time.time()
    
    processes = []
    for _ in range(2): 
        p = multiprocessing.Process(target=crawl_images)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    
    with open("log.txt", "a") as log_file:
        log_file.write(f"Multiprocessing - Time Taken: {end_time - start_time:.2f}s\n")

if __name__ == "__main__":
    run_multiprocessing()
