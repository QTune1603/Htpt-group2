import time
from main import AutoCrawler

# Cấu hình AutoCrawler
config = {
    "skip_already_exist": True,
    "n_threads": 1,  # Chạy 1 luồng duy nhất
    "do_google": True,
    "do_naver": False,
    "download_path": "download",
    "full_resolution": False,
    "face": False,
    "no_gui": True,
    "limit": 10  # Tải 10 ảnh
}

def run_single_process():
    start_time = time.time()
    crawler = AutoCrawler(**config)
    crawler.do_crawling()
    end_time = time.time()

    with open("log.txt", "a") as log_file:
        log_file.write(f"Single Process - Time Taken: {end_time - start_time:.2f}s\n")

if __name__ == "__main__":
    run_single_process()
