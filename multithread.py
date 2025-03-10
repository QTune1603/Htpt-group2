import time
from concurrent.futures import ThreadPoolExecutor
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

def crawl_images(task_id):
    """Worker tải ảnh"""
    print(f"Worker {task_id} bắt đầu...")
    crawler = AutoCrawler(**config)
    crawler.do_crawling()
    print(f"Worker {task_id} hoàn thành!")

def run_multithreading():
    """Chạy tải ảnh với đa luồng"""
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(crawl_images, i) for i in range(4)]
        for future in futures:
            future.result()  # Chờ tất cả các luồng hoàn thành
    
    end_time = time.time()
    
    # Ghi log sau khi tất cả luồng hoàn thành
    with open("log.txt", "a") as log_file:
        log_file.write(f"Multithreading - Time Taken: {end_time - start_time:.2f}s\n")

if __name__ == "__main__":
    run_multithreading()
