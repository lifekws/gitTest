# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:46:02 2023

@author: USER
"""
import pandas as pd
import operator

# 레벤슈타인 거리 구하기
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
    # matrix 초기화의 예 : [[0, 1, 2, 3], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    # [0, 1, 2, 3]
    # [1, 0, 0, 0]
    # [2, 0, 0, 0]
    # [3, 0, 0, 0] 
    matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # 표 채우기 --- (※2)
    # print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
            # print(matrix)
        # print(matrix,'----------끝')
    return matrix[a_len][b_len]
# "가나다라"와 "가마바라"의 거리 --- (※3)

# 사용자 질문과 레벤슈타인거리가 가장 적은 답변 추출
def ans_find(base):       
    ''' 사용자 질문과 레벤슈타인거리가 가장 적은 답변 추출 '''
    q_dic = {} # 딕셔너리 초기화
    
    # 사용자 질문과 대한 챗봇 데이타 전체 질문의 레벤슈타인 거리 계산
    for n in questions:       
        r = calc_distance(base, n)    # 레벤슈타인 거리 구하기
        q_index = questions.index(n)  # 질문의 인덱스 저장
        q_dic[q_index]=r              # 딕셔너리에 레벤슈타인 거리와 질문의 인덱스 저장           
    
    # 정상적인 실행을 위해 operator 모듈을 import 해야 한다.
    r = sorted(q_dic.items(),key=operator.itemgetter(1)) # 레벤슈타인 거리가 작은 순으로 sort
    q_ind = r[0][0]                                      # sort 된 데이타의 첫번째 인덱스 저장            
    return answers[q_ind] # 

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'
data = pd.read_csv(filepath)

questions = data['Q'].tolist()  
answers = data['A'].tolist()


# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    input_sentence = input('You: ') 
        
    if input_sentence.lower() == '종료':
        break
    response = ans_find(input_sentence)
    print('Chatbot:', response)