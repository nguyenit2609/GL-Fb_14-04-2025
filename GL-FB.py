from seleniumbase import Driver
import time, os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Màu sắc terminal
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

os.system("")  # Kích hoạt màu terminal cho Windows

current_dir = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(current_dir, "chrome_profile")
os.makedirs(profile_path, exist_ok=True)

tongxu = 0
biendem = 0

def kiemtra():
    print("Đang mở Chrome để kiểm tra đăng nhập...")
    driver = Driver(
        uc=True,
        headed=True,
        user_data_dir=profile_path
    )
    driver.set_window_size(500, 700)
    driver.get("https://app.golike.net/login")
    time.sleep(5)
    if driver.current_url == "https://app.golike.net/home":
        print("✅ Đã đăng nhập GoLike.")
        driver.quit()
        return True
    else:
        input("❌ Chưa đăng nhập. Vui lòng đăng nhập xong rồi bấm ENTER...")
        driver.quit()
        return False

def lam_nhiem_vu_snapchat(driver):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/snapchat")
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/gold.svg")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/snapchat.svg")]').click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()

        tongxu += 50
        biendem += 1
        print(f"{CYAN}| {biendem} | SNAPCHAT |{GREEN} Hoàn Thành {RESET}| {YELLOW}+50 đ{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        print(f"{RED}Lỗi Snapchat{RESET} => Bỏ qua...", end="\r")
        print(""*20, end="\r")

def lam_nhiem_vu_thread(driver):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/thread")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        time.sleep(2)
        kt_job = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/span')
        job_text = kt_job.text 
        kt_job.click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a/div[3]/i').click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/i').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()

        xu_number = int(job_text.split()[0])
        tongxu += xu_number
        biendem += 1
        print(f"{CYAN}| {biendem} |  THREAD  |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{job_text}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except :
        print(f"{RED}Lỗi Thread{RESET} => Bỏ qua...", end="\r")
        print(""*20, end="\r")

def lmjob():
    os.system('cls' if os.name == 'nt' else 'clear')
    driver = Driver(uc=True, headed=True, mobile=True, user_data_dir=profile_path)
    driver.set_window_size(500, 700)
    while True:
        lam_nhiem_vu_snapchat(driver)
        lam_nhiem_vu_thread(driver)

# === CHƯƠNG TRÌNH CHÍNH ===
text = """
============================================== MENU =============================================
[1] Đăng nhập GoLike 
[2] Làm nhiệm vụ
"""
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    for char in text :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    print("")
    chon = input("  [X] Chọn: ").strip()
    if chon == "1":
        kiemtra()
    elif chon == "2":
        break
    else:
        print("❗ Nhập sai, vui lòng chọn lại.")
lmjob()


