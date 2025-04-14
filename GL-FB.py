try:
    from seleniumbase import Driver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver.chrome.options import Options 
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os, re, sys
    from selenium.webdriver.chrome.options import Options
    from datetime import datetime
    from selenium.webdriver.common.action_chains import ActionChains
except ImportError as e:
    missing_package = str(e).split("'")[1]
    print(f"Thư viện {missing_package} chưa được cài đặt. Đang cài đặt lại...")

    try:
        os.system(f"pip install {missing_package}")
        # Sau khi cài đặt, kiểm tra lại xem thư viện đã được cài đặt thành công chưa
        __import__(missing_package)
        print(f"Thư viện {missing_package} đã được cài đặt thành công.")
    except Exception as install_error:
        print(f"Đã xảy ra lỗi khi cài đặt {missing_package}. Lỗi: {install_error}")
        print("Vui lòng quay video và hình ảnh gửi admin để được xử lí")
        print("Zalo Admin: 0359832905")
# xóa full màn hình
os.system('cls')

# Thoát chương trình
def check_exit_input(driver):
    while True:
        user_input = input("Nhập '3' lần nữa để thoát: ")
        if user_input.lower() == '3':
            driver.quit()  # Đóng tất cả tab Selenium
            sys.exit()
# Thu nhỏ trình duyệt đến 50%
def zoom_until_50_percent(driver):
    actions = ActionChains(driver)
    while True:
        # Mô phỏng nhấn Ctrl + -
        actions.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.CONTROL).perform()
        time.sleep(0.1)  # Dừng một chút giữa mỗi lần nhấn phím

        # Kiểm tra zoom
        zoom_level = driver.execute_script("return document.body.style.zoom;")
        # Nếu zoom <= 50%, dừng lại
        if zoom_level and float(zoom_level.strip('%')) <= 30:
            break

# chính
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
        try:
            driver.get("https://app.golike.net/login")
            time.sleep(5)
            if driver.current_url == "https://app.golike.net/home":
                print("Đã đăng nhập golike")
            else:
                input("Chưa đăng nhập golike vui lòng đăng nhập lại rồi bấm enter...")
            driver.execute_script("window.open('https://m.facebook.com/login');")
            time.sleep(2)
            tabs = driver.window_handles
            driver.switch_to.window(tabs[-1])
            driver.get("https://www.facebook.com/friends")
            if driver.current_url == "https://www.facebook.com/friends":
                print("Đăng nhập fb thành công")
                time.sleep(2)
                #driver.close()
            else:
                input("Vui lòng đăng nhập fb, khi đăng nhập xong thì bấm enter...")
                time.sleep(10)
        finally:
            print("Đã có đầy đủ các tài khoản đang tiến hành làm việc")
            driver.quit()
        time.sleep(5)
    # xóa full màn hình
        os.system('cls')
    # làm nhiệm vụ
    def lamjob():
        try:
            print("Đang làm nhiệm vụ")
            os.system('cls')
            current_dir = os.path.dirname(os.path.abspath(__file__))
            profile_path = os.path.join(current_dir, "chrome_profile")
            os.makedirs(profile_path, exist_ok=True)
            driver = Driver(
                uc=True,  
                headed=True, 
                user_data_dir=profile_path 
            )
            driver.set_window_size(500, 700)
            while True:
                try:
                    time.sleep(10)
                    driver.get("https://app.golike.net/jobs/facebook?load_job=true")
                    time.sleep(2)
                    driver.refresh()
                    time.sleep(5)
                finally:
                    print("| Nhiệm vụ |  Trạng thái   | Xu  | Tổng xu |")
                    print("| Facebook | Đang nhận job | ... |   ...   |", end="\r")
                # check job + nhận job 
                try:
                    driver.execute_script("document.body.style.zoom='60%'")
                    kt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]/div/div/div/div/div[1]/h6/span/span')
                    text = kt.text.strip() # check job bao nhiêu xu
                    xu = int(text) if text.isdigit() else 0
                    kt_job_like = driver.find_element(By.XPATH, "//img[@src='../../assets/images/icons-gif/like.gif']")
                    kt_job_sad = driver.find_element(By.XPATH, "//img[@src='../../assets/images/icons-gif/sad.gif']")
                    kt_job_anry = driver.find_element(By.XPATH, "//img[@src='../../assets/images/icons-gif/angry.gif']")
                    kt_job_tt = driver.find_element(By.XPATH, "//img[@src='../../assets/images/icons-gif/care.gif']")
                    kt_job_tim = driver.find_element(By.XPATH, "//img[@src='../../assets/images/icons-gif/love.gif']")
                    if kt_job_like.is_displayed():
                        print(f"| Facebook | Job Like       | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_sad.is_displayed():
                        print(f"| Facebook | Job Buồn 😢    | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_anry.is_displayed():
                        print(f"| Facebook | Job ANGRY       | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_tt.is_displayed():
                        print(f"| Facebook | Job Thương 💗   | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_tim.is_displayed():
                        print(f"| Facebook | Job Tim 💗      | +{xu:<4} |   ...   |", end="\r")
                    else:
                        print(f"| Facebook | Không rõ job gì  |    +0    |   ...   |", end="\r")
                    time.sleep(2)
                    kt.click()
                        # Nhận job khác snapchat hay linkedin ở đây
                except Exception as e:
                    print("\nError: Không thể nhận dạng job hoặc lấy xu. Chi tiết:", e)
                time.sleep(5)
                # Làm job + tìm nút bấm
                try:
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[3]').click()
                        time.sleep(5)
                        driver.switch_to.window(driver.window_handles[-1])
                        zoom_until_50_percent(driver)
                    except:
                        try:
                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[2]').click()
                            time.sleep(5)
                            driver.switch_to.window(driver.window_handles[-1])
                            zoom_until_50_percent(driver)
                        except:
                            try:
                                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[1]').click()
                                time.sleep(5)
                                driver.switch_to.window(driver.window_handles[-1])
                                zoom_until_50_percent(driver)
                            except:
                                print("Không tìm thấy nút bấm")
                                time.sleep(2)
                                continue # Làm lại từ While 
                finally:
                    try:
                        print("| Facebook | Đang làm job  | {xu:<4}  |   ...   |", end="\r")
                    except:
                        print("| Facebook | Job lỗi       |  ...     |   ...   |", end="\r")
            # Thời gian chờ load trang
                    time.sleep(10)
            # Làm joob
                try:
                    if kt_job_like.is_displayed():
                        print(f"| Facebook | Đang Like      | +{xu:<4} |   ...   |", end="\r")
                        try:
                            # test like 1
                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]').click()
                            time.sleep(2)
                        except:
                            print("job lỗi")
                            continue
                            # nếu gặp lỗi thì qualai báo cáo và continue để bắt đầu lại 
                        driver.close()
                        time.sleep(2)
                        # bấm nút hoàn thành
                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
                        time.sleep(5)
                        driver.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[1]').click()
                        continue
                    elif kt_job_sad.is_displayed():
                        print(f"| Facebook | Đang Buồn 😢   | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_anry.is_displayed():
                        print(f"| Facebook | Đang ANGRY      | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_tt.is_displayed():
                        print(f"| Facebook | Đang Thương 💗  | +{xu:<4} |   ...   |", end="\r")
                    elif kt_job_tim.is_displayed():
                        print(f"| Facebook | Đang Tim 💗     | +{xu:<4} |   ...   |", end="\r")
                    else:
                        print(f"| Facebook | Job lỗi          |    +0    |   ...   |", end="\r")
                finally:
                    try:
                        print(f"| Facebook | Hoàn thành      | +{xu:<4} |   ...   |", end="\r")
                    except:
                        print("| Facebook | Job lỗi      | +0 |   ...   |", end="\r")
            # Nếu ko thấy nút like thì báo cáo<job lỗi>
        except Exception as e:
            print(e)     
finally:
    print("Trạng thái: Good. Cảm ơn bạn đã sài tool")
    
while True:
    print("| 1 | Kiểm tra tài khoản")
    print("| 2 | Làm nhiệm vụ")
    print("| 3 | Exit")
    n = input("Nhập số: ")
    if n == "1":
        kiemtra()
    if n == "2":
        lamjob()
    if n == "3":
        check_exit_input()
    os.system('cls')