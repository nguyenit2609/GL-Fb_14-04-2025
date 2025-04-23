try:
    from selenium import webdriver
    import time, os , threading
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os, re, sys, string, random
    import undetected_chromedriver as uc
    from selenium.webdriver.chrome.options import Options
    from datetime import datetime
    from colorama import Fore, Style
    from selenium.webdriver.common.action_chains import ActionChains
except:
    print("Lỗi import thư viện")
frames = ['|', '/', '-', '\\']  # Các icon dùng trong animation

# Hàm delay chung với tham số cho hành động và thời gian
def delay_action(second, action_text, is_error=False):
    for i in range(second * 10, 0, -1):
        icon = frames[i % len(frames)]  # Chọn icon theo bước
        color = RED if is_error else CYAN if i % 2 == 0 else BLUE
        bracket_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"{color}{icon} {action_text} {bracket_color}[{i//10}.{i%10}s]{RESET}", end="\r")
        time.sleep(0.1)
    print(" " * 60, end="\r")  # Xóa dòng sau khi xong

# Hàm delay cho job bình thường
def delay(second):
    delay_action(second, "Đang chạy job")

# Hàm delay khi lấy job
def delay_laplai(second):
    delay_action(second, "Đang lấy job")

# Hàm delay cho khi gặp lỗi job
def delay_die(second):
    delay_action(second, "Job die => Đang bỏ qua", is_error=True)

# Hàm delay cho anti band
def delay_anti(second):
    delay_action(second, "Đang chạy antiband")
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Profile_chrome")

# Đọc danh sách profile từ file profiles.txt
def load_profiles_from_file():
    profiles = []
    if os.path.exists('profiles.txt'):
        with open('profiles.txt', 'r') as file:
            # Lấy phần cuối cùng sau dấu '\\' cho mỗi dòng
            profiles = [line.strip().split("\\")[-1] for line in file.readlines()]
    return profiles
profiles = load_profiles_from_file()

# Lưu danh sách profile vào file profiles.txt
def save_profiles_to_file(profiles):
    with open('profiles.txt', 'w') as file:
        for profile in profiles:
            file.write(f"{profile}\n")

# Tạo mới profile và thêm vào danh sách
def tao_profile_moi():
    index = 1
    while True:
        new_profile_path = os.path.join(base_path, f"chrome_profile_{index}")
        if not os.path.exists(new_profile_path):
            break
        index += 1

    print(f"{CYAN}➡️ Đang tạo profile chrome_profile_{index}, vui lòng đăng nhập GoLike{RESET}")
    driver = create_driver(new_profile_path, headless=False)
    driver.set_window_size(500, 700)
    driver.get("https://app.golike.net/login")
    input("👉 Sau khi đăng nhập xong GoLike, nhấn Enter để tiếp tục...")
    driver.quit()
    print(f"{GREEN}✅ Đã tạo và lưu chrome_profile_{index}{RESET}")
    return new_profile_path  # Trả về để thêm vào danh sách

# Hàm tạo driver với profile
def create_driver(profile_path, headless=False):
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.abspath(profile_path)}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--force-device-scale-factor=0.30")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

    if headless:
        options.headless = True
        options.add_argument("--window-size=1920,1080")

    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver

# Luồng tk chạy
def in_tat_ca_profiles_tu_file(file_path):
    with open(file_path, 'r') as f:
        profiles = f.readlines()
        if profiles:
            for profile in profiles:
                profile = profile.strip()  
                profile_name = profile.split("\\")[-1] 
        else:
            print("Không có profile nào trong file.")
# Kiểm tra đăng nhập GoLike
def kiem_tra_dang_nhap(driver, profile_path, index):
    driver.get("https://app.golike.net/home")
    time.sleep(2)
    while True:
        if driver.current_url == "https://app.golike.net/home":
            print(f"{Fore.GREEN}[Luồng {index}] ✅ Đã đăng nhập GoLike ({profile_path}){Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.YELLOW}[Luồng {index}] ⏳ Đang chờ đăng nhập GoLike ({profile_path}){Style.RESET_ALL}")
            input(f"[Luồng {index}] 🔐 Vui lòng đăng nhập rồi nhấn Enter...")
            driver.get("https://app.golike.net/home")
            time.sleep(2)
def kiem_tra_chon_profile(profiles):
    # Hiển thị danh sách các profile để người dùng chọn
    print(f"{CYAN}===== Danh sách các tài khoản ====={RESET}")
    for idx, profile in enumerate(profiles, start=1):
        print(f"[{idx}] {profile}")

    # Yêu cầu người dùng chọn một profile để kiểm tra
    lua_chon = input(f"[W] Nhập số tài khoản muốn kiểm tra (hoặc nhập 'x' để thoát): ").strip()

    if lua_chon.lower() == 'x':
        return  # Thoát nếu người dùng nhập 'x'
    
    try:
        # Kiểm tra nếu người dùng nhập số hợp lệ
        lua_chon = int(lua_chon)
        if 1 <= lua_chon <= len(profiles):
            profile_path = profiles[lua_chon - 1]
            print(f"{CYAN}➡️ Đang kiểm tra tài khoản: {profile_path}{RESET}")
            driver = create_driver(profile_path, headless=False)
            kiem_tra_dang_nhap(driver, profile_path, lua_chon - 1)
            driver.quit()  # Đóng driver sau khi kiểm tra
        else:
            print(f"{RED}⚠️ Số tài khoản không hợp lệ!{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Vui lòng nhập số hợp lệ!{RESET}")
def lam_nhiem_vu_snapchat(driver, index):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/snapchat")
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/gold.svg")]').click()
        delay(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/snapchat.svg")]').click()
        delay(1)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(1)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(1)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")  
        tongxu += 50
        biendem += 1
        profile = profiles[index] if index < len(profiles) else "Unknown Profile"
        print(f" {YELLOW}[Luồng {index + 1} - Profile: {profile}]{RESET} {CYAN}| {biendem} |  SNAPCHAT  |{GREEN} Hoàn Thành {RESET}| {YELLOW}+50 đ{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        delay_die(1)
        print(f"{GREEN}Bỏ qua xong! Tiếp tục...{RESET}", end="\r")
        print(""*30, end="\r")

def lam_nhiem_vu_thread(driver, index):
    global tongxu, biendem
    try:
        # ko dc pc
        driver.get("https://app.golike.net/jobs/thread")
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(2)
        kt_job = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/span')
        job_text = kt_job.text 
        kt_job.click()
        delay(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a/div[3]/i').click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/i').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(2)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")
        xu_number = int(job_text.split()[0])
        tongxu += xu_number
        biendem += 1
        profile = profiles[index] if index < len(profiles) else "Unknown Profile"
        print(f" {YELLOW}[Luồng {index + 1} - Profile: {profile}]{RESET} {CYAN}| {biendem} |   THREAD   |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{job_text}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except :
        delay_die(2)
        print(f"{GREEN}Bỏ qua xong! Tiếp tục...{RESET}", end="\r")
        print(""*30, end="\r")
def lam_nhiem_vu_linkedin(driver, index):
    global tongxu, biendem
    try:
        # ko dc pc
        driver.get("https://app.golike.net/jobs/linkedin")
        delay(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(2)
        kt_job = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/span')
        job_text = kt_job.text 
        kt_job.click()
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a/div[3]/i').click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(1)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/i').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(1)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")
        xu_number = int(job_text.split()[0])
        tongxu += xu_number
        biendem += 1
        profile = profiles[index] if index < len(profiles) else "Unknown Profile"
        print(f" {YELLOW}[Luồng {index + 1} - Profile: {profile}] {RESET}{CYAN}| {biendem} |  LINKEDIN  |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{job_text}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        delay_die(1)
        print(f"{GREEN}Bỏ qua xong! Tiếp tục...{RESET}", end="\r")
        print(""*30, end="\r")
# Hàm làm nhiệm vụ Facebook Like cho mỗi profile
def lam_job(profile_path, index=0):
    driver = create_driver(profile_path, headless=False)
    driver.set_window_size(500, 700)
    driver.set_window_position(x=550 * index, y=0 )  # Đặt vị trí cửa sổ khác nhau
    while True:
        lam_nhiem_vu_snapchat(driver, index)
        lam_nhiem_vu_thread(driver, index)
        lam_nhiem_vu_linkedin(driver, index)
def get_all_profiles(base_path):
    return [os.path.join(base_path, f) for f in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, f)) and f.startswith("chrome_profile_")]

# Hàm chạy đa luồng với delay giữa các luồng
def chay_da_luong(profile_paths, delay=5):
    profile_paths = get_all_profiles(base_path)
    if not profile_paths:  # Kiểm tra xem có profile không
        print(f"{RED}⚠️ Không có profile nào để chạy!{RESET}")
        return

    threads = []
    for index, profile_path in enumerate(profile_paths):
        time.sleep(delay * index)  # Đợi 3 giây trước khi khởi động mỗi luồng
        
        if os.path.exists(profile_path):  # Kiểm tra profile có tồn tại không
            print(f"{CYAN}➡️ Đang làm nhiệm vụ với profile {profile_path}{RESET}")
            t = threading.Thread(target=lam_job, args=(profile_path, index))
            t.daemon = True  # Đảm bảo thread tự kết thúc khi chính chương trình kết thúc
            t.start()
            threads.append(t)
        else:
            print(f"{RED}⚠️ Profile không tồn tại: {profile_path}{RESET}")
    time.sleep(4)
    os.system('cls')
    # Đảm bảo tất cả threads hoàn thành trước khi kết thúc
    for t in threads:
        t.join()

    print(f"{GREEN}✅ Tất cả nhiệm vụ đã hoàn thành!{RESET}")

# Menu UI
def ui():
    while True:
        os.system('cls')
        print(f"""
{CYAN}===== MENU ====={RESET}
[1]  Thêm tài khoản
[2]  Kiểm tra đăng nhập
[3]  Làm nhiệm vụ (đồng thời)
[X]  Thoát
        """)
        lua_chon = input("[W] Nhập lựa chọn: ").strip()
        profiles = load_profiles_from_file()  # Đọc lại danh sách profile từ file

        if lua_chon == "1":
            profile_path = tao_profile_moi()
            if profile_path not in profiles:
                profiles.append(profile_path)
                save_profiles_to_file(profiles)  # Lưu lại danh sách profile vào file
        elif lua_chon == "2":
            kiem_tra_chon_profile(profiles)

        elif lua_chon == "3":
            try:
                chay_da_luong(profiles)
            except Exception as e:
                print(e)
                break
        elif lua_chon.lower() == "x":
            break

# Thực thi chương trình
if __name__ == "__main__":
    ui()


