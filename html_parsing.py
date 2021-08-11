import glob
from bs4 import BeautifulSoup
import pandas as pd
import os
import pathlib
from datetime import date
import re
import timeit

file_path = 'd:/데이터교육/vac0810/'

#병원 한개의 정보를 담는 클래스
class host:
    #백신의 경우 디폴트값이 0
    pfizer = 0
    moderna = 0
    AZ = 0
    host_name = ''
    host_dist = ''
    host_addr = ''
    date = ''

#잔여 백신이 발생한 병원 클래스를 저장할 리스트
hospitals = []
hosp_name = []
hosp_dist = []
hosp_addr = []
pfizer = []
moderna = []
AZ = []
times = []
dates = []

#html에서 잔여 백신 데이터를 가져오는 함수
def get_vaccdata(file_name):
    #html읽어오기
    file_path = file_name
    f = open(file_path, encoding = 'utf-8')
    html_source = f.read()
    f.close()
    soup = BeautifulSoup(html_source, 'html.parser')
    #잔여백신 수량
    vacc_quantity = soup.select('div._3sd6u')
    #잔여백신 수량 텍스트 ex)n개, 대기중, 마감
    vaccine_quantity = [vac_quantity.get_text() for vac_quantity in vacc_quantity]

    #html코드를 병원별로 분할
    hosts_data = soup.select('li._1mrr7')

    #잔여 백신이 없는 경우
    not_count = ['0개','대기중','마감']
    #병원의 정보를 가져오기 위한 변수
    i = 0
    #추출한 잔여 백신 수량 하나씩 접근
    for number_of_vaccines in vaccine_quantity:
        #잔여 백신이 없는 경우
        if number_of_vaccines in not_count:
            continue
        #있는 경우
        #임시 클래스 생성
        temp = host()
        #현재 병원의 html태그
        now_host = hosts_data[i]
        #이름 정보를 클래스의 이름 변수에 저장
        temp.host_name = now_host.find('span', attrs={'class':'_2ZThT'}).get_text()
        #백신 정보 리스트
        now_vac = now_host.find_all('span',attrs={'class':'_2DrWY'})

        #백신 정보를 하나씩 가져와 클래스에 저장
        for j in range(len(now_vac)):
            #a : 백신 이름, b : 잔여 수량
            a = now_vac[j].get_text().split("\xa0")[0]
            b = now_vac[j].get_text().split("\xa0")[1]
            #잔여 수량이 있는 경우에만 저장
            if b not in not_count:
                #정수값만 추출
                b = int(re.findall(r'\d+', b)[0])
                #백신 이름에 따라 클래스 내의 해당 백신 변수에 수량 저장
                if a == '화이자': temp.pfizer = b
                elif a == '모더나': temp.moderna = b
                elif a == 'AZ': temp.AZ = b

        #현재 위치부터 거리
        temp.host_dist = now_host.find('span', attrs={'class': '_2IJhC ck59y'}).get_text()[7:]
        #병원 주소
        temp.host_addr = now_host.find('span', attrs={'class': '_19kF1'}).get_text()
        #발생 시간
        temp.date = get_str_date()

        #다음 요소 접근을 위해 +1
        i += 1

        #이중 for문 탈출을 위한 변수
        tf = True

        # 잔여 백신 발생 병원 리스트에 추가
        #병원의 데이터가 이미 저장된 경우
        if temp.host_name in hosp_name:
            #병원 이름 리스트에서 병원의 인덱스들을 모두 반환
            idx = list(filter(lambda e: hosp_name[e] == temp.host_name, range(len(hosp_name))))
            #저장된 병원 데이터에 하나씩 접근
            for k in idx:
                #각 백신들 개수 비교 > 모두 같으면 중복된 데이터이므로 저장하지 않고 다음 반복 진행
                if temp.pfizer == hospitals[k].pfizer and temp.moderna == hospitals[k].moderna and temp.AZ == hospitals[k].AZ:
                    tf = False
                    break
            if not tf:
                continue

        #중복된 데이터가 아닌 경우 저장
        hospitals.append(temp)
        hosp_name.append(temp.host_name)
        times.append(get_time(file_name))

#클래스 리스트에 있는 요소를 하나씩 접근해 개별 리스트에 저장
def mk_hosplist():
    for i in hospitals:
        hosp_dist.append(i.host_dist)
        hosp_addr.append(i.host_addr)
        pfizer.append(i.pfizer)
        moderna.append(i.moderna)
        AZ.append(i.AZ)
        dates.append(i.date)

#데이터의 시간추출
def get_time(str):
    # 10_18_40
    time = str[-12:-4]
    # 10_18_40 -> 10:18:40
    time = time.replace('_', ':')
    return time

#날짜 추출
def get_date():
    # 오늘날짜 추출, 연 월 일
    today = date.today()
    # 월일만 추출 ex)0810
    today_date = '{0:02d}{1:02d}'.format(today.month, today.day)
    return today_date

#날짜 추출
def get_str_date():
    # 오늘날짜 추출, 연 월 일
    today = date.today()
    # 월일만 추출 ex)0810
    today_date = '{0:02d}월{1:02d}일'.format(today.month, today.day)
    return today_date

#데이터 프레임 생성 및 csv 파일로 저장
def save(filepath):
    today_date = get_date()
    #데이터 프레임 생성
    df_vaccine = pd.DataFrame({'hospital':hosp_name, 'AZ':AZ, 'pfizer':pfizer, 'moderna':moderna, 'hospital distance':hosp_dist, 'address':hosp_addr, 'time':times, 'date':dates})
    print(df_vaccine)
    #ex)C:/Users/Administrator/Desktop/잔여백신_raw_data/vaccine_data/
    raw_data_folder = filepath
    #raw_data_folder가 있으면 그냥 통과
    if(os.path.isdir(raw_data_folder)):
        pass
    #없으면 생성
    else:
        pathlib.Path(raw_data_folder).mkdir(parents = True, exist_ok = True)
    #csv파일로 저장
    df_vaccine.to_csv(raw_data_folder+'data'+today_date+'.csv', encoding = 'cp949')

def get_files(file_path):
    txt = file_path+"*.txt"
    png = file_path+"*.png"
    txt_file = glob.glob(txt)
    png_file = glob.glob(png)

    for i in range(len(txt_file)):
        print(i+1,"/",len(txt_file))
        get_vaccdata(txt_file[i])
        os.remove(txt_file[i])
        if (os.path.isfile(png_file[i])):
            os.remove(png_file[i])

    mk_hosplist()
    save(file_path)

start_time = timeit.default_timer()
get_files(file_path)
terminate_time = timeit.default_timer()
print("%f초"%(terminate_time-start_time))
