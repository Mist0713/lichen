'''
lichenAddPoints 1.0.0 ver
'''

from tabulate import tabulate #출력 형식
import csv                    #csv 변환

'''
lichens = [
    [1	Anaptychia	톱니작은그리마지의
    [2	Anaptychia	돌기작은그리마지의
    [3	Anaptychia	작은그리마지의
    [4	Anzia	유사개발바닥지의
    [5	Anzia	개발바닥지의
    [6	Caloplaca	회색백분단추지의
    [7	Caloplaca	주황산호단추지의
    [8	Caloplaca	흑테방울주황단추지의
    [9	Caloplaca	로코스단추지의
    [10	Caloplaca	좀주황단추지의
    [11	Caloplaca	회색방울단추지의
    [12	Caloplaca	황국화단추지의
    [13	Caloplaca	느슨주황단추지의
    [14	Caloplaca	해변레몬단추지의
    [15	Candelaria	촛농지의
    [16	Canoparmelia	알갱이잿빛매화나무지의
    [17	Canoparmelia	노랑알갱이잿빛매화나무지의
    [18	Canoparmelia	잿빛매화나무지의
    [19	Cetraria	갈퀴지의
    [20	Cetrelia	돌기조개지의
    [21	Cetrelia	과립조개지의
    [22	Cetrelia	나플나플조개지의
    [23	Cetrelia	유사적염과립조개지의
    [24	Cetreliopsis	전복지의
    [25	Cladia	가시묶음지의
    [26	Coccocarpia	기와지의
    [27	Collema	연한김지의
    [28	Cladonia	뿔사슴지의
    [29	Cladonia	짚사슴지의
    [30	Cladonia	좀막대꽃지의
    [31	Cladonia	가시사슴지의
    [32	Cladonia	깔대기지의
    [33	Cladonia	분말창끝사슴지의
    [34	Cladonia	분말뿔사슴지의
    [35	Cladonia	촛대지의
    [36	Cladonia	가락붉은열매지의
    [37	Cladonia	산사슴지의
    [38	Cladonia	분말깔대기지의
    [39	Cladonia	자루꽃지의
    [40	Cladonia	갈래사슴지의
    [41	Cladonia	점갈래사슴지의
    [42	Cladonia	마디꽃지의
    [43	Cladonia	꾀꼬리사슴지의
    [44	Cladonia	작은깔대기지의
    [45	Cladonia	긴사슴지의
    [46	Cladonia	터번사슴지의
    [47	Cladonia	연꽃사슴지의
    [48	Cladonia	잔꽃지의
    [49	Cladonia	연한사슴지의
    [50	Cladonia	사슴지의
    [51	Cladonia	잔사슴지의
    [52	Cladonia	지팡이사슴지의
    [53	Cladonia	좁쌀비늘꽃지의
    [54	Cladonia	유사작은깔대기지의
    [55	Cladonia	민꽃사슴지의
    [56	Cladonia	넓은잎사슴지의
    [57	Cladonia	넓은사슴지의
    [58	Dermatocarpon	민바위버섯지의
    [59	Dirinaria	유사메달지의
    [60	Dirinaria	메달지의
    [61	Flavoparmelia	노란매화나무지의
    [62	Fuscopannaria	알갱이작은꽃잎지의
    [63	Fuscopannaria	유사산호꽃잎지의
    [64	Fuscopannaria	방석작은꽃잎지의
    [65	Fuscopannaria	검은둘레꽃잎지의
    [66	Fuscopannaria	돌작은꽃잎지의
    [67	Fuscopannaria	작은꽃잎지의
    [68	Fuscopannaria	가루검은둘레꽃잎지의
    [69	Fuscopannaria	흰방석작은꽃잎지의
    [70	Heterodermia	가죽그리마지의
    [71	Heterodermia	흰배면그리마지의
    [
    [72	Heterodermia	검은발그리마지의
    [
    [73	Heterodermia	작은돌기그리마지의
    [
    [74	Heterodermia	노란배그리마지의
    [75	Heterodermia	산그리마지의
    [76	Hypogymnia	작은리본지의
    [77	Hypotrachyna	돌기쌍분지지의
    [78	Karoowia	갯바위국화잎지의
    [79	Leptogium	잿빛김지의
    [80	Leptogium	돌기냇물잿빛김지의
    [81	Leptogium	깊은산나무잿빛김지의
    [82	Leptogium	잎돌기잿빛김지의
    [83	Leptogium	건조잿빛김지의
    [84	Leptogium	청건조잿빛김지의
    [
    [85	Leptogium	낱알잿빛김지의
    [86	Lobaria	밤색가죽옷지의
    [87	Lobaria	푸석푸석맨들지의
    [88	Lobaria	얇은투구지의
    [89	Lobaria	윤나는잎투구지의
    [
    [90	Lobaria	주걱모양투구지의
    [91	Menegazzia	천공지의
    [92	Myelochroa	너덜너덜노란속매화나무지의
    [93	Myelochroa	아시아노란속매화나무지의속
    [94	Myelochroa	하야치네노란속매화나무지의
    [95	Myelochroa	알갱이노란속매화나무지의
    [96	Myelochroa	음지노란속매화나무지의
    [
    [97	Neocatapyrenium	신구멍비늘지의
    [98	Nephroma	유사뒷손톱지의
    [
    [99	Nephromopsis	노란속큰전복지의
    [
    [100	Nipponoparmelia	나플나플동아시아당초무늬지의]
]
'''

#지역 번호, 지역명

regions=[
    [0, "없음"],
    [1, "설악산"],
    [2, "지리산"],
    [3, "오대산"],
    [4, "한라산"],
    [5, "속리산"],
    [6, "덕유산"],
    [7, "소백산"],
    [8, "태백산"],
    [9, "조계산"],
    [10, "내장산"],
    [11, "주왕산"],
    [12, "계룡산"],
    [13, "백운산"],
    [14, "경기도/서울/인천 "],
    [15, "경기도/서울/인천 "],
    [16, "강원도 산지"],
    [17, "강원도 해안"],
    [18, "경상도 산지"],
    [19, "경상도 해안"],
    [20, "충청도(대전, 세종) 산지"],
    [21, "충청도(대전, 세종) 해안"],
    [22, "전라도(광주) 산지"],
    [23, "전라도(광주) 해안"],
    [24, "경상도(대구, 부산, 울산) 산지"],
    [25, "경상도(대구, 부산, 울산) 해안"],
    [26, "제주도 해안"],
    [27, "남해 일대"],
    [28, "욕지도"],
    [29, "속리산"],
    [30, "백아산"],
    [31, "가야산"],
    [32, "황병산"]
]


print(tabulate(regions, headers=["regionNumber", "regionName"], tablefmt='firstrow'))

print("Notice | 지역 번호가 없을시 0을 기입해야함.")

region = []
numberOfRegionInput = 0
def regionInput():
    global numberOfRegionInput
    try:
        if not numberOfRegionInput>=4:
            print(numberOfRegionInput+1,"번째 지역 번호를 입력하세요 : ", sep=" ", end='')
            numberOfRegionInput += 1
            regioninput = int(input())
            if 0<=regioninput<=33:
                region.append(regioninput)
            else:
                numberOfRegionInput -= 1
                print("Notice | 지역값의 범위는 0 이상 33 이하입니다.")
            regionInput()
        else:
            return
    except ValueError:
        print("Notice | 지역 번호가 없을시 0을 기입해야함. 다시시도하시오.")
        numberOfRegionInput -= 1
        regionInput()

def checkRegionInput(): # boolean 반환
    global numberOfRegionInput
    try:
        print("지금 이 값으로 지역을 정할까요? [y/n]", end=" ")
        checkYesOrNoRegion = input()
        checkYesOrNoRegion.lower()
        if checkYesOrNoRegion == "y":
            return True
        elif checkYesOrNoRegion == "n":
            numberOfRegionInput = 0
            return False
        else:
            print("Notice | 올바른 값을 입력해주세요")
            checkRegionInput()
    except:
        print("Notice | 올바른 값을 입력해주세요")
        checkRegionInput()

def checkAltitudeInput(): # boolean 반환
    try:
        print("지금 이 값으로 고도를 정할까요? [y/n]", end=" ")
        checkYesOrNoAltitude = input()
        checkYesOrNoAltitude.lower()
        if checkYesOrNoAltitude == "y":
            return True
        elif checkYesOrNoAltitude == "n":
            return False
        else:
            print("Notice | 올바른 값을 입력해주세요")
            checkAltitudeInput()
    except:
        print("Notice | 올바른 값을 입력해주세요")
        checkAltitudeInput()

def altitudeInput():
    global altitude
    try:
        print("모든 고도에 분포할 경우 -1을 입력하십시오.")
        print("현재 고도를 입력해 주세요 : ", end = " ")
        altitude = int(input())
        if altitude == -1:
            return
        elif altitude<0:
            print("Notice | 고도는 0보다 크거나 같아야합니다.")
            return altitudeInput
        else:
            return
    except:
        print("Notice | 잘못된 입력입니다.")
        return altitudeInput

#---------------------------------------    입력   ------------------------------------

regionInput()
print("입력된 지역 : ", *region)
while True:
    if checkRegionInput():
        break
    else:
        region = []
        regionInput()
        print("입력된 지역 : ", *region)
print("Notice | 고도는 한 곳만 입력해주세요")
altitudeInput()
if altitude == -1:
    print("입력된 고도 : 전역")
else:
    print("입력된 고도 : ", altitude)
while True:
    if checkAltitudeInput():
        break
    else:
        region = []
        altitudeInput()
        if altitude == -1:
            print("입력된 고도 : 전역")
        else:
            print("입력된 고도 : ", altitude)

#------------------------    처리    --------------------------------
# 3, 4, 5, 6
file = open('lichenList.csv','r')
read = csv.reader(file)

lichenList = []

for i in range(len(region)):
    region[i] = str(region[i])
altitude = str(altitude)

for line in read:
    lichenList.append(line)
AddPoints = [[False]*5 for _ in range(100)]
for i in range(len(lichenList)):
    if lichenList[i][3] in region:
        AddPoints[i][0] = True
    if lichenList[i][4] in region:
        AddPoints[i][1] = True
    if lichenList[i][5] in region:
        AddPoints[i][2] = True
    if lichenList[i][6] in region:
        AddPoints[i][3] = True
    if lichenList[i][7] == 0 and int(altitude)!=-1:
        lst = list(str(lichenList[i][8]).split(","))
        if altitude in lst:
            AddPoints[i][4] = True
# print(lichenList)
print(tabulate(AddPoints, headers=["regionA", "regionB", "regionC", "regionD", "altitude"], tablefmt='firstrow'))