import cv2
import random

def print_progress_bar(frame, frame_gauge, total, length=100):
    """
    화면의 우측 상단에 진행 상황을 나타내는 게이지 바를 그립니다.

    Args:
        frame (numpy.ndarray): 입력 프레임 (이미지)
        frame_gauge (int): 현재 진행 상황 값
        total (int): 전체 진행 상황 값 (최대 값)
        length (int, optional): 게이지 바의 길이. 기본값은 100입니다.
    Returns:
        numpy.ndarray: 게이지 바가 그려진 프레임
    """
    # 백분율 계산
    percent = min(100 * frame_gauge // total, 100)


    # 색상 선택
    if  0 <= percent <= 20:
        color = (0, 0, 255)  # 빨간색
    elif 20 < percent <= 40:
        color = (0, 100, 100)  # 청록색
    elif 40 < percent <= 60:
        color = (255, 200, 0)  # 파란색
    elif 60 < percent <= 80:
        color = (0, 255, 255)  # 노란색
    elif 80 < percent <= 100:
        color = (0, 255, 0)  # 녹색

    # 채워진 게이지 바의 길이 계산
    filled_length = int(length * percent // 100)

    # 화면의 우측 상단에 게이지 바 그리기
    cv2.rectangle(frame, (frame.shape[1] - length - 10, 10), (frame.shape[1] - 10, 30), (255, 255, 255), -1)
    cv2.rectangle(frame, (frame.shape[1] - length - 10, 10), (frame.shape[1] - 10 - length + filled_length, 30), color, -1)

    # 백분율을 표시하는 텍스트 추가
    cv2.putText(frame, f'{percent}%', (frame.shape[1] - length - 10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    return frame

# 기본 카메라 열기
cap = cv2.VideoCapture(0)

# 머리, 몸통, 오른팔, 왼팔, 오른 다리, 왼 다리, 오른 팔꿈치, 왼 팔꿈치 일치 함수
def head():
    return random.randint(0, 1)

def body():
    return random.randint(0, 1)

def R_arm():
    return random.randint(0, 1)

def L_arm():
    return random.randint(0, 1)

def R_leg():
    return random.randint(0, 1)

def L_leg():
    return random.randint(0, 1)

def R_elbow():
    return random.randint(0, 1)

def L_elbow():
    return random.randint(0, 1)



while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gauge = (head() + body() + R_arm() + L_arm() + R_leg() + L_leg() + R_elbow() + L_elbow()) / 8 * 100

    # 프레임 표시
    
    frame = print_progress_bar(frame, frame_gauge, 100)  # 예: progress=50, total=100
    cv2.imshow('Frame', frame)

    # 'q' 키가 눌리면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# VideoCapture 객체 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
