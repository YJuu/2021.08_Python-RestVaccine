# 필요 라이브러리 import
from selenium import webdriver as wd
import pygetwindow as gw
import pyautogui as pg
from PIL import ImageGrab as Ig
from PIL import ImageChops as Ic
from PIL import ImageStat as Is
from PIL import Image
import time
import keyboard
from bs4 import BeautifulSoup  # html 소스코드 가져오기 위함
import pathlib
from datetime import date, datetime
import os

# 페이지 로드를 위한 기본 정보
webdriver_path = 'C:/chromedriver.exe' #사용자에게 입력받을 정보
vac_add = 'https://m.place.naver.com/rest/vaccine'

# 텍스트 파일 및 이미지 파일 저장 폴더 생성
today = date.today()
str_today = str(today).replace('-', '')
today_month_day = str_today[-4:]
txt_png_data_folder = 'C:/Program Files/잔여백신/vac' + today_month_day + '/'  # 파일 경로는 뭐로 정하지, 우리가 정해야해
if (os.path.isdir(txt_png_data_folder)):
    pass
else:
    pathlib.Path(txt_png_data_folder).mkdir(parents=True, exist_ok=True)

# webdriver를 이용해서 잔여백신 페이지 로드
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(webdriver_path, options=options)
driver.get(vac_add)
time.sleep(5)

# 잔여 백신 예약 사이트가 켜져있는 창 정보를 불러와 npwd에 저장
titles = gw.getAllTitles()
idx = titles.index("네이버 플레이스 - Chrome")
npwd = gw.getWindowsWithTitle(titles[idx])[0]

# npwd의 끝점 좌표
npr = npwd.right
npl = npwd.left
npt = npwd.top
npb = npwd.bottom - 70

# 새로고침 아이콘의 x,y좌표
click_x = npr - 50
click_y = npb + 20

# 캡쳐할 이미지 영역(=잔여 백신 창 전체 영역)
np_crop = (npl, npt, npr, npb)

# 새로고침 아이콘 클릭
pg.click(click_x, click_y)
# 이미지 캡쳐 및 출력
img = Ig.grab(np_crop)


def crop_func(img):
    filename = time.strftime('%H_%M_%S')
    six=datetime.strptime('18:00:00','%H:%M:%S').time()
    html = driver.page_source
    img.save(txt_png_data_folder + filename + '.png') #첫화면 이미지 저장
    f = open(txt_png_data_folder + filename + '.txt', 'w', encoding='UTF-8') #첫화면 html 소스 저장
    f.write(html)
    f.close()
    while True:
        now = datetime.now().time() #현재 시간
        if keyboard.is_pressed("esc") or (now.hour == six.hour): #6시에 종료
            driver.quit() #브라우저 완전종료
            break
        pg.click(click_x, click_y)
        time.sleep(2)
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
                    img.save(txt_png_data_folder + filename + '.png')
                    f = open(txt_png_data_folder + filename + '.txt', 'w', encoding='UTF-8')
                    f.write(html)
                    f.close()



crop_func(img)