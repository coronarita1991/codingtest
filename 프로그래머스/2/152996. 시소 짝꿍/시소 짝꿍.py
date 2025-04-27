from collections import Counter

# 최적화된 시소 짝꿍 솔루션
# weights: 몸무게 리스트를 받아, 균형을 이루는 짝의 수를 반환합니다.
def solution(weights):
    # 몸무게 빈도 계산
    freq = Counter(weights)
    answer = 0

    # 1) 같은 거리(p1 == p2)인 경우: 같은 몸무게끼리만 균형
    #    f개라면 조합으로 f*(f-1)//2쌍
    for w, f in freq.items():
        answer += f * (f - 1) // 2

    # 2) 서로 다른 거리(p1 > p2)인 경우만 처리하여 중복 방지
    #    가능한 거리 비율 (p1, p2): (3,2), (4,2), (4,3)
    ratios = [(3, 2), (4, 2), (4, 3)]
    for p1, p2 in ratios:
        for w1, f1 in freq.items():
            # 상대편 몸무게 w2 = w1 * p1 / p2 이어야 정수
            num = w1 * p1
            if num % p2 != 0:
                continue
            w2 = num // p2
            # w2가 존재하고, w2 > w1 (중복 피하기)
            f2 = freq.get(w2, 0)
            if f2 and w2 > w1:
                # w1의 경우의 수 × w2의 경우의 수
                answer += f1 * f2

    return answer
