#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : ________ 이름 : ______

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

print("----Q.1----")

my_string = input("my_string를 입력하시오 : ") # 해당 내용을 출력한 뒤 사용자로부터 문자열을 입력받아 my_string에 저장
target = input("target를 입력하시오 : ") # 해당 내용을 출력한 뒤 사용자로부터 문자열을 입력받아 target에 저장

def solution(my_string, target): # my_string과 target를 매개변수로 하는 solution 함수 정의
    if target in my_string: # my_string문자열에 target문자열에 해당하는 내용이 있다면 실행
        return 1 # 함수의 결과를 1로 반환
    else: # my_string문자열에 target문자열에 해당하는 내용이 없다면 실행
        return 0 # 함수의 결과를 0으로 반환

print("answer : %d" % solution(my_string, target))

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

print("----Q.2----")

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = '' # 해독된 문자를 저장할 문자열
    list = letter.split() # split()을 사용하여 문자열을 공백을 기준으로 문자열을 나누어서 리스트로 반환
    for word in list: # list의 첫번째 요소부터 마지막 요소까지 차례대로 word에 대입
        if word in morse: # morse 딕셔너리에 word와 동일한 'key'가 있다면 if문 실행
            answer += morse[word] # answer 문자열 뒷부분에 morse 딕셔너리의 'key'가 word에 해당하는 'value' 값을 추가
        else: # morse 딕셔너리에 word와 동일한 key가 없다면 실행
            answer += '#'

    return answer

letter = ".-.. .. ..-. . .. ... - --- --- ... .... --- .-. -" # lifeistooshort
print(solution(letter))

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

print("----Q.3----")

def solution(age):
    answer = '' # 행성의 나이를 알파벳으로 표현한 값을 저장하는 문자열
    code = "abcdefghij" # a는 0번째, b는 1번째, ..., j는 9번째 위치하는 것을 이용하여 정보 저장
    for ch in str(age): # int형 age를 문자열로 바꾸고 해당 문자열의 길이만큼 for문 실행, age의 값을 차레대로 ch에 저장
        answer += code[int(ch)] # 정수형 ch를 int형으로 바꾸고 code 문자열의 ch위치에 해당하는 값을 answer의 뒤에 이어서 작성

    return answer

print(solution(51))

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

print("----Q.4----")

def solution(r1, r2):
    answer = 0
    # 원의 방정식은 x^2 + y^2 = r^2으로 x^2 + y^2 <= r^2이 성립하는 x, y는 원 내부의 점
    for x in range(-r2, r2 + 1): # 반지름이 r2인 원이 더 큰 원이므로 -r2 ~ r2까지 값을 1씩 증가시키면 반복문 실행
        for y in range(-r2, r2 + 1): # y의 값도 동일하게 증가시키며 반복문을 실행시켜 모든 점에 대하여 계산
            if x*x + y*y <= r2*r2: # 원의 방정식을 이용하여 해당 조건문이 성립하면 점(x, y)는 반지름이 r2인 원 내부에 존재
                if x*x + y*y >= r1*r1: # 해당 조건문이 성립하면 점(x, y)는 반지름이 r1인 원 내부에 존재하지 않음
                    answer += 1 
    return answer

print(solution(2,4))

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

print("----Q.5----")

def solution(numbers):
    answer = '' # 정수를 이러 붙여 만들 수 있는 큰 수를 저장할 문자열
    num_str = list(map(str, numbers)) # numbers의 요소들을 순서대로 문자열로 바꾸어서 num_str리스트에 저장
    num_str.sort(key=lambda a: a * 3) # num_str을 정렬. 단, 정렬조건이 num_str의 각 요소들을 3배한 뒤에 정렬계산
    # numbers = [8, 30, 17, 2, 23]인 경우 [888, 303030, 171717, 222, 232323]으로 변환하여 정렬
    # 위에서 numbers을 문자열로 변환시켰으므로 정렬은 왼쪽부터 각 숫자를 ASCII로 변환하여 정렬하여 계산됨
    # lambda는 일회성 함수로 해당 식에서만 사용가능함
    for i in num_str: # num_str의 문자열의 구성 요소 개수만큼 반복문 실행
        answer = i + answer # num_str을 정렬할 때 오름차순 정렬이므로 answer에 값을 넣을때는 반대로 계산

    return answer

numbers = [8, 30, 17, 2, 21]
print(solution(numbers))