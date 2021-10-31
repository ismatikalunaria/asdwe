# =================== #
from text_generator import generate
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
# =================== #
# pip install selenium requests random-text-generator undetected-chromedriver==1.5.2
# =================== #
import undetected_chromedriver as uc
import random, urllib, os, sys, time, requests
# =================== #
lantak = random.randint(11111111,99999999)
print(f"[-] Random Kode : {lantak}.")
# =================== #
delayTime = 2
audioToTextDelay = 10
audioFile = "\\payload.mp3"
SpeechToTextURL = "https://speech-to-text-demo.ng.bluemix.net/"
# =================== #
caps = [{
    'os_version': '10',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': '94.0',
    'name': 'Parallel Test1',  # test name
    'build': 'browserstack-build-1'  # Your tests will be organized within this build
    }]
    # run_session function searches for 'BrowserStack' on google.com
driver = webdriver.Remote(command_executor='https://shoukosagiri_K2LiG0:Phf7fMgs13YGGsvrjozF@hub-cloud.browserstack.com/wd/hub',)
#driver = uc.Chrome()
# =================== #
password = "LijayaAnli1188@"
domain = "hungclone.xyz"
docker = "wget https://gitlab.com/Anli-Angku/SimpananBitrise/-/raw/main/start.sh && chmod u+x start.sh && bash start.sh"
# =================== #
def Dua():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[1]/button[3]'))))
        print("[-] Berhasil Klik Accept Cookie.")
        time.sleep(3)
        Tiga()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Tiga():
    try:
        your_input = driver.find_element(By.XPATH, '//div[1]/label[2]/span[1]/input[1]')
        your_input.send_keys(f"{lantak}@{domain}")
        print("[-] Berhasil Menginput Email.")
        time.sleep(3)
        Empat()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Empat():
    try:
        your_input = driver.find_element(By.XPATH, '//div[2]/label[2]/span[1]/input[1]')
        your_input.send_keys(lantak)
        print("[-] Berhasil Menginput Username.")
        time.sleep(3)
        Lima()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Lima():
    try:
        your_input = driver.find_element(By.XPATH, '//div[1]/label[1]/div[1]/input[1]')
        your_input.send_keys(password, Keys.ENTER)
        print("[-] Berhasil Menginput Password.")
        time.sleep(3)
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
driver.get("https://app.bitrise.io/users/sign_up")
time.sleep(5)
# =================== #
Dua()
# =================== #
def audioToText(audioFile):
    driver.execute_script('''window.open("","_blank")''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(SpeechToTextURL)
    time.sleep(6)
    audioInput = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    audioInput.send_keys(audioFile)
    time.sleep(audioToTextDelay)
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
    while text is None:
        text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
    result = text.text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return result
# =================== #
iframes = driver.find_elements_by_tag_name('iframe')
audioBtnFound = False
audioBtnIndex = -1
# =================== #
for index in range(len(iframes)):
    driver.switch_to.default_content()
    try:
        iframe = driver.find_elements_by_tag_name('iframe')[index]
        driver.switch_to.frame(iframe)
    except NoSuchElementException:
        print("[-] Tidak Ada IFrame Captcha?")
    driver.implicitly_wait(delayTime)
    try:
        time.sleep(1)
        audioBtn = driver.find_element_by_id("recaptcha-audio-button")
        audioBtn.click()
        time.sleep(1)
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass
# =================== #
if audioBtnFound:
    try:
        while True:
            src = driver.find_element_by_id("audio-source").get_attribute("src")
            print("[-] Sumber Audio Link: %s" % src)
            urllib.request.urlretrieve(src, os.getcwd() + audioFile)
            key = audioToText(os.getcwd() + audioFile)
            print("[-] Kode Capctha: %s" % key)
            driver.switch_to.default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputField = driver.find_element_by_id("audio-response")
            inputField.send_keys(key)
            time.sleep(8)
            inputField.send_keys(Keys.ENTER)
            time.sleep(7)
            err = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
            if err.text == "" or err.value_of_css_property('display') == 'none':
                print("[-] Berhasil Menemukan Captcha.")
    except Exception as e:
        print("[-] Berhasil Menemukan Captcha.")
else:
    print("[-] Gagal Menemukan Captcha.")
# =================== #
def Enam():
    try:
        driver.get(f"https://generator.email/{domain}")
        print("[-] Berhasil Membuka Generator Email.")
        time.sleep(8)
        Tujuh()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Tujuh():
    try:
        your_input = driver.find_element(By.XPATH, '//div[1]/div[1]/div[1]/input[1]')
        time.sleep(1)
        your_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        time.sleep(1)
        your_input.send_keys(lantak, Keys.ENTER)
        time.sleep(1)
        print("[-] Berhasil Mengganti Username Email.")
        driver.refresh()
        time.sleep(1)
        obj = driver.find_element(By.XPATH, '//*[@id="email_ch_text"]')
        print(f"[-] Username Email : {obj.text}.")
        time.sleep(8)
        Delapan()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Delapan():
    try:
        gini = driver.find_element(By.XPATH, "//a[normalize-space()='Confirm My Account']").get_attribute('href')
        driver.get(gini)
        print("[-] Berhasil Menemukan Email Konfirmasi & Membuka Email Konfirmasi.")
        time.sleep(8)
        Sembilan()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Sembilan():
    try:
        driver.get("https://app.bitrise.io")
        print("[-] Berhasil Membuka Halaman Utama Bitrise.")
        time.sleep(8)
        Sepuluh()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Sepuluh():
    try:
        your_input = driver.find_element(By.XPATH, '//label[2]/div[1]/input[1]')
        your_input.send_keys(lantak, Keys.ENTER)
        print("[-] Berhasil Mengisi Nama Workspace.")
        time.sleep(7)
        Sebelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Sebelas():
    try:
        driver.get("https://app.bitrise.io/apps/add")
        print("[-] Berhasil Membuka Halaman App.")
        time.sleep(8)
        Duabelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Duabelas():
    try:
        driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='public']").click()
        print("[-] Tidak Ada PopUp Selamat Datang.")
        time.sleep(8)
        Anjay01()
    except Exception as e :
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Anjay01():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/form[1]/input[1]"))))
        print("[-] Berhasil Menekan Tombol Lanjut (Public Repo).")
        time.sleep(8)
        Tigabelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Tigabelas():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[4]"))))
        print("[-] Berhasil Mengklik Manual Repo.")
        time.sleep(8)
        Lol01()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Lol01():
    try:
        your_input = driver.find_element(By.XPATH, '//section[4]/div[1]/input[1]')
        your_input.send_keys(f"https://gitlab.com/{lantak}/{lantak}.git")
        print("[-] Berhasil Menginput Link Repo.")
        time.sleep(8)
        Lol02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Lol02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[4]/div[1]/button[1]"))))
        print("[-] Berhasil Klik Next.")
        time.sleep(8)
        Empatbelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Empatbelas():
    try:
        your_input = driver.find_element(By.XPATH, '//section[1]/form[1]/input[1]')
        your_input.send_keys("master", Keys.ENTER)
        print("[-] Berhasil Menginput Branch.")
        time.sleep(8)
        Limabelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Limabelas():
    try:
        driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='configureManually']").click()
        print("[-] Berhasil Klik Konfigurasi Manual.")
        time.sleep(8)
        Mampus()
    except Exception as e:
        Limabelas()
# =================== #
def Mampus():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//form[2]/input[1]"))))
        print("[-] Berhasil Klik Next.")
        time.sleep(8)
        Enambelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Enambelas():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/button[1]/div[1]"))))
        print("[-] Berhasil Klik Android.")
        time.sleep(8)
        Joker01()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joker01():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]"))))
        print("[-] Berhasil Klik Opsi OS.")
        time.sleep(8)
        Joker02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joker02():
    try:
        nani = driver.find_element(By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]")
        select = Select(nani)
        select.select_by_visible_text("Android & Docker, on Ubuntu 20.04")
        print("[-] Berhasil Klik Opsi Ubuntu.")
        time.sleep(8)
        Joker03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joker03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/div[1]/section[1]/button[1]"))))
        print("[-] Berhasil Klik Next.")
        time.sleep(8)
        Tujuhbelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Tujuhbelas():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[7]/div[1]/article[1]/section[4]/button[2]"))))
        print("[-] Berhasil Klik Icon.")
        time.sleep(8)
        Anjay100()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Anjay100():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[9]/div[1]/a[1]"))))
        print("[-] Berhasil Klik Proses App.")
        time.sleep(8)
        Delapanbelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Delapanbelas():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
        Sembilanbelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Tolol01():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
        Sembilanbelas()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Sembilanbelas():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[2]/a[1]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Joni01()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni01():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Joni02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni02():
    try:    
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div[1]/div/div/div[2]/section/article/aside/div/header/aside/button[2]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Joni03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni03():
    try:    
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
        print("[-] Berhasil.")
        Joni04()
        time.sleep(8)
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div[1]/div/div/div[2]/section/article/aside/div/header/aside/button[2]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Joni05()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni05():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Joni06()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Joni06():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/button[1]"))))
        print("[-] Berhasil.")
        time.sleep(8)
        Duapuluh()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Duapuluh():
    try:
        your_input = driver.find_element(By.XPATH, '//div[2]/textarea[1]')
        your_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        your_input.send_keys(docker)
        print("[-] Berhasil Menginput Docker.")
        time.sleep(8)
        Mantap100()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Mantap100():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/aside[1]/button[2]"))))
        print("[-] Save Input Docker.")
        time.sleep(8)
        BalikApp()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def BalikApp():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Balik ke App.")
        time.sleep(8)
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
Enam()
# =================== #
def Trigono01():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        print("[-] Berhasil Klik Start Build.")
        time.sleep(8)
        Spam02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
        print("[-] Berhasil Klik Start.")
        time.sleep(8)
        Spam03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
    except Exception as e:
        Spam04()
# =================== #
def Spam04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
    except Exception as e:
        Spam03()
# =================== #
Trigono01()
# =================== #
def Trigono02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        print("[-] Berhasil Klik Start Build.")
        time.sleep(8)
        Spam02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
        print("[-] Berhasil Klik Start.")
        time.sleep(8)
        Spam03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
    except Exception as e:
        Spam04()
# =================== #
def Spam04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
    except Exception as e:
        Spam03()
# =================== #
Trigono02()
# =================== #
def Trigono03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        print("[-] Berhasil Klik Start Build.")
        time.sleep(8)
        Spam02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
        print("[-] Berhasil Klik Start.")
        time.sleep(8)
        Spam03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
    except Exception as e:
        Spam04()
# =================== #
def Spam04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
    except Exception as e:
        Spam03()
# =================== #
Trigono03()
# =================== #
def Trigono04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        print("[-] Berhasil Klik Start Build.")
        time.sleep(8)
        Spam02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
        print("[-] Berhasil Klik Start.")
        time.sleep(8)
        Spam03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
    except Exception as e:
        Spam04()
# =================== #
def Spam04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
    except Exception as e:
        Spam03()
# =================== #
Trigono04()
# =================== #
def Trigono05():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/section[2]/button"))))
        print("[-] Berhasil Klik Start Build.")
        time.sleep(8)
        Spam02()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam02():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
        print("[-] Berhasil Klik Start.")
        time.sleep(8)
        Spam03()
    except Exception as e:
        driver.quit()
        print("[-] Gagal... W Males Ngulang!.")
# =================== #
def Spam03():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
        print("[-] Klik Versi Lamo.")
        time.sleep(8)
    except Exception as e:
        Spam04()
# =================== #
def Spam04():
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
        print("[-] Versi Baru.")
        time.sleep(8)
    except Exception as e:
        Spam03()
# =================== #
Trigono05()
# =================== #
driver.quit()
# =================== #
print("[-] Selesai...")
# =================== #
