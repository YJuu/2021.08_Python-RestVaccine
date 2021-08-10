import glob
from bs4 import BeautifulSoup
import pandas as pd
import os
import pathlib
from datetime import date
import re
import timeit

file_path = 'd:/데이터교육/'
file_name = '10_02_26.txt'

#병원 한개의 정보를 담는 클래스
class host:
    #백신의 경우 디폴트값이 0
    pfizer = 0
    moderna = 0
    AZ = 0
    host_name = ''
    host_dist = ''
    host_addr = ''

#잔여 백신이 발생한 병원 클래스를 저장할 리스트
hospitals = []
hosp_name = []
hosp_dist = []
hosp_addr = []
pfizer = []
moderna = []
AZ = []

def get_vaccdata(file_path):
    #html읽어오기
    file_path = file_path
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
        print(number_of_vaccines)
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
        #다음 요소 접근을 위해 +1
        i += 1
        #잔여 백신 발생 병원 리스트에 추가
        hospitals.append(temp)

#클래스 리스트에 있는 요소를 하나씩 접근해 개별 리스트에 저장
def mk_hosplist():
    for i in hospitals:
        hosp_name.append(i.host_name)
        hosp_dist.append(i.host_dist)
        hosp_addr.append(i.host_addr)
        pfizer.append(i.pfizer)
        moderna.append(i.moderna)
        AZ.append(i.AZ)

#데이터 프레임 생성 및 csv 파일로 저장
def save(filepath,filename):
    # 10_18_40
    time=filename[-12:-4]
    # 10_18_40 -> 10:18:40
    time = time.replace('_', ':')
    # 오늘날짜 추출, 연 월 일
    today = date.today()
    # 월일만 추출 ex)0810
    today_date = '{0:02d}{1:02d}'.format(today.month,today.day)

    #데이터 프레임 생성
    df_vaccine = pd.DataFrame({'hospital':hosp_name, 'AZ':AZ, 'pfizer':pfizer, 'moderna':moderna, 'hospital distance':hosp_dist, 'address':hosp_addr, 'time':time, 'date':today_date[:2]+'/'+today_date[2:4]})
    print(df_vaccine)
    #ex)C:/Users/Administrator/Desktop/잔여백신_raw_data/vaccine_data/
    raw_data_folder = filepath+'vaccine_data/'
    #raw_data_folder가 있으면 그냥 통과
    if(os.path.isdir(raw_data_folder)):
        pass
    #없으면 생성
    else:
        pathlib.Path(raw_data_folder).mkdir(parents = True, exist_ok = True)
    #csv파일로 저장
    df_vaccine.to_csv(raw_data_folder+'data'+today_date+'.csv', encoding = 'cp949')
    return df_vaccine

start_time = timeit.default_timer()

get_vaccdata(file_path+file_name)

terminate_time = timeit.default_timer()
print("%f초"%(terminate_time-start_time))

mk_hosplist()
save(file_path,file_name)
