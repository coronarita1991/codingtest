def solution(h1, m1, s1, h2, m2, s2):
    # 1) 시간 범위 (초 단위), 끝점까지 포함
    start = h1 * 3600 + m1 * 60 + s1
    end   = h2 * 3600 + m2 * 60 + s2

    # 2) 초침-분침 이벤트
    sm_events = []
    per_minute = 3600 / 59
    for hour in range(24):
        base = hour * 3600
        for k in range(59):
            sm_events.append(base + k * per_minute)

    # 3) 초침-시침 이벤트
    sh_events = []
    per_hour = 43200 / 719
    for j in (0, 1):
        base = j * 43200
        for k in range(719):
            sh_events.append(base + k * per_hour)

    # 4) 합치고 정렬
    events = sm_events + sh_events
    events.sort()

    # 5) 중복 시간(정각 중복)을 하나로 묶어 세기, 끝점 포함
    tol = 1e-6
    count = 0
    last_t = -1.0
    for t in events:
        if t < start or t > end:
            continue
        # 이전 이벤트와 같은 시간대가 아니면 새로 세기
        if last_t < 0 or t - last_t > tol:
            count += 1
            last_t = t

    return count