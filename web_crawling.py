# 필요 라이브러리 import
import pyautogui
from selenium import webdriver as wd
import pygetwindow as gw
from PIL import ImageGrab as Ig
from PIL import ImageChops as Ic
from PIL import ImageStat as Is
import time
import keyboard
from bs4 import BeautifulSoup  # html 소스코드 가져오기 위함
from datetime import datetime
import os

exit_key = 0

# 페이지 로드를 위한 기본 정보
webdriver_path = 'd:/programfiles/chromedriver/chromedriver.exe' #사용자에게 입력받을 정보
vac_add = 'https://m.place.naver.com/rest/vaccine'
file_path = os.getcwd()+'/data/'

pyautogui.FAILSAFE = False

def set_driver(driver):
    global webdriver_path
    webdriver_path = driver

def exit_func():
    global exit_key
    exit_key = 1

def crop_func():
    global exit_key
    options = wd.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = wd.Chrome(webdriver_path, options=options)
    driver.get(vac_add)
    driver.implicitly_wait(5)

    titles = gw.getAllTitles()
    idx = titles.index("네이버 플레이스 - Chrome")
    npwd = gw.getWindowsWithTitle(titles[idx])[0]

    # npwd의 끝점 좌표
    npr = npwd.right
    npl = npwd.left
    npt = npwd.top
    npb = npwd.bottom - 70
    np_crop = (npl, npt, npr, npb)

    refresh = driver.find_element_by_xpath('//*[@id="_list_scroll_container"]/div/div/div[1]/div/div/div[2]/a')
    refresh.click()

    img = Ig.grab(np_crop)
    img.show()

    filename = time.strftime('%H_%M_%S')
    six=datetime.strptime('18:00:00','%H:%M:%S').time()
    html = driver.page_source
    img.save(file_path+ filename + '.png') #첫화면 이미지 저장
    f = open(file_path + filename + '.txt', 'w', encoding='UTF-8') #첫화면 html 소스 저장
    f.write(html)
    f.close()

    while True:
        now = datetime.now().time() #현재 시간
        if keyboard.is_pressed("esc"): #6시에 종료
            exit_key = 1
        if exit_key == 1:
            driver.quit()  # 브라우저 완전종료
            break
        refresh.click()
        driver.implicitly_wait(2)
        temp = Ig.grab(np_crop)  # Ig(대문자 i), ImageGrab, 지정한 이미지 영역만큼만 캡처하여 temp에 저장
        im = Ic.difference(img, temp)  # Ic, ImageChops, 같은 이미지면 difference()의 결과 이미지의 모든 픽셀은 0
        stat = Is.Stat(im)  # ls, ImageStat
        if stat.sum != [0, 0, 0]:
            img = temp
            soup = BeautifulSoup(html, 'html.parser')
            vacc_quantity = soup.select('div._3sd6u')  # 화면상에 나오는 잔여백신 현황 아이콘 태그
            vaccine_quantity = [vac_quantity.get_text() for vac_quantity in vacc_quantity]  # 텍스트만 가져오기
            not_count = ['대기중', '마감', '0개']
            for number_of_vaccines in vaccine_quantity:  # 수량추출한거 하나씩 가져오기
                if number_of_vaccines not in not_count :  # 잔여백신 수량이 나올경우만 png파일, txt파일 저장
                    img.save(file_path + filename + '.png')
                    f = open(file_path + filename + '.txt', 'w', encoding='UTF-8')
                    f.write(html)
                    f.close()


if __name__ == "__main__":
    print(file_path)
    set_driver('d:/programfiles/chromedriver/chromedriver.exe')
    crop_func()