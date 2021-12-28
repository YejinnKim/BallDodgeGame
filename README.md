## 공 피하기 게임

### 1. 사용언어  
    Python(pygame)

### 2. 실행화면  
<img width="50%" src="https://user-images.githubusercontent.com/50562634/147556141-227a8142-370b-4a5b-a53f-764fe55ec9b6.png"/>

### 3. 게임 설명 및 주요 기능
#### 3-1. 게임 규칙
    - 방향키로 캐릭터 조종
    - 움직이는 공을 맞으면 score 감소
    - 랜덤으로 생성되는 별을 먹으면 score 20점 증가
    - 스페이스 바를 누르면 공 추가, score 10점 증가
    - 제한시간 30초  
    
    화면 우측 상단의 Game Rule 글씨와 캐릭터가 겹쳐지면 해당 내용(게임 규칙)을 볼 수 있음
    
#### 3-2. 캐릭터
    - 캐릭터의 좌표값을 저장하는 pos_x와 pos_y 변수 선언 (화면의 중앙 값으로 초기화)
    - 좌표에 캐릭터 이미지 load
    - 키가 눌릴 때 마다(get_pressed()가 발생할 때 마다) 해당 방향으로 좌표값 변경(ex. pos_x += 3)
    - 터가 화면을 벗어나지 않도록 조절(ex. if pos_y > screen_height: pos_y -= 3)
    
#### 3-3. 별
    - 별의 좌표값을 저장하는 Class Star 선언
    - 화면 내에서 랜덤으로 좌표값 저장(random 모듈)
    - 좌표에 별 이미지 load
    - 캐릭터 좌표와 별 좌표가 겹칠 때 마다 Star의 새로운 랜덤 좌표를 생성 후 초기화
    
#### 3-4. 타이머
    - 초를 저장하는 time(get_ticks()/1000), 남은 시간을 저장하는 timer(30-time) 변수 선언
    - timer가 0이 되면 게임 종료를 알리는 Game Over 메시지와 최종 Score 노출
