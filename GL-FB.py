try:
    from seleniumbase import Driver
    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os, re, sys
    from selenium.webdriver.chrome.options import Options
    from datetime import datetime
    from selenium.webdriver.common.action_chains import ActionChains
except:
    print("Lỗi import thư viện")

# Màu sắc terminal
CYAN = '\033[96m'      # Snapchat label
GREEN = '\033[92m'     # Trạng thái thành công
YELLOW = '\033[93m'    # Xu
MAGENTA = '\033[95m'   # Tổng xu
BLUE = '\033[94m'      # Time
RED = '\033[91m'       # Lỗi
RESET = '\033[0m'

current_dir = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(current_dir, "chrome_profile")
os.makedirs(profile_path, exist_ok=True)

os.system("")  # Bật màu cho terminal (Windows)

# Thêm biến điều khiển để thoát khỏi vòng lặp
logged_in = False

while not logged_in:
    da_login = input("❓ Bạn mới chạy tool lần đầu thì bấm n mấy lần sau chỉ cần bấm y (y/n): ").strip().lower()
    if da_login == "n":
        try:
            # nếu thêm thì thêm acc vào đây
            def kiemtra():
                print("Đang mở profile Chrome chờ 5-10p tùy vào cấu hình máy")
                current_dir = os.path.dirname(os.path.abspath(__file__))
                profile_path = os.path.join(current_dir, "chrome_profile")
                os.makedirs(profile_path, exist_ok=True)
                driver = Driver(
                    uc=True,
                    headed=True,
                    user_data_dir=profile_path
                )
                driver.set_window_size(500, 700)
                print("Đang chạy kiểm tra đăng nhập")
                time.sleep(5)
                driver.get("https://app.golike.net/login")
                time.sleep(5)
                if driver.current_url == "https://app.golike.net/home":
                    print("Đã đăng nhập golike")
                    return True  # Trả về True nếu đã đăng nhập
                else:
                    input("Chưa đăng nhập golike vui lòng đăng nhập lại rồi bấm enter...")
                    return False  # Trả về False nếu chưa đăng nhập
                driver.quit()

        finally:
            if kiemtra():  # Nếu đã đăng nhập, thoát vòng lặp
                logged_in = True
            continue
    else:
        os.system('cls')
        def lmjob():
            # Khởi tạo driver
            print("Đang mở profile Chrome chờ 5-10p tùy vào cấu hình máy", end="\r")
            driver = Driver(
                uc=True,
                headed=True,
                mobile=True,
                user_data_dir=profile_path
            )
            print(""*50, end="\r")
            driver.set_window_size(500, 700)
            tongxu = 0
            time.sleep(2)
            driver.get("https://app.golike.net/jobs/snapchat")

            biendem = 1
            while True:
                try:
                    time.sleep(2)
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
                    time.sleep(1)
                    kt_job = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[4]/div[2]')
                    job_text = kt_job.text 
                    driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/gold.svg")]').click()
                    time.sleep(2)

                    # Bấm vào để mở tab mới
                    driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/snapchat.svg")]').click()
                    time.sleep(2)
                    
                    # Chờ tab mới xuất hiện
                    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

                    # Lấy danh sách tất cả các tab
                    all_windows = driver.window_handles
                    first_window = all_windows[0]

                    # Chuyển sang tab mới
                    new_window = all_windows[-1]
                    driver.switch_to.window(new_window)
                    driver.close()

                    # Quay lại tab ban đầu
                    driver.switch_to.window(first_window)
                    time.sleep(2)

                    # Tiếp tục thao tác trên tab đầu
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
                    ).click()
                    time.sleep(2)

                    # Cộng xu và in thông tin
                    tongxu += 50
                    biendem += 1
                    current_time = datetime.now().strftime("%H:%M:%S")
                    print(f"{CYAN}| {biendem} | Snapchat |{GREEN} Succeeded {RESET}| {YELLOW}+50{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {current_time}{RESET} | {CYAN}Job: {job_text}{RESET}")

                except Exception as e:
                    print(f"{RED}Lỗi xảy ra: {e}{RESET} => Đang tiếp tục chạy, không cần để ý lỗi trên ....")
                    continue

        lmjob()  # Gọi hàm lmjob() nếu đã đăng nhập GoLike
        logged_in = True  # Dừng vòng lặp sau khi đã đăng nhập

