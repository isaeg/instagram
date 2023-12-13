# instagram
인스타 자동 좋아요/댓글/팔로우 

# 개발 환경
* python 3.9 
* Mysql
    * host : db.isaegad.gabia.io : 3306
    * database: dbisaegad
    * user : isaegad
    * pwd : dltorrhkdrh2023 (이색광고2023)

# 프로세스 
1. main.py ->tkinter 이용 한 gui 창
2. 창에 필요 한 값 입력
   댓글 및 금지단어는 a/b/c로 입력 => split을 / 기준으로 자름 
3. web_followers_db.workStart 로 로직 파라미터 넘겨 시작 ->tb_time_log 에 시작 시간 기록 
4. instagram 페이지 접속 -> 로그인
5. setp.1 에서 입력한 방문할 계정명으로 이동
6. 팔로워 창 클릭
7. setp.1에서 입력한 방문할 횟수 만큼 스크롤하면서 배열에 append
8. 7 에서 가져온 배열에서 진짜로 방문할 계정 거름  
   8-1. 공개 계정 일 것  
   8-2. 팔로잉 안한 계정일 것  
   8-3. 공개 계정이고 게시물이  1개 이상 일 것  
9. 8 에서 생성한 계정 링크를 하나 씩 방문  
  9-1. setp.1 에서 설정한 금지단어가 소개글에 있으면 그 계정은 pass  
10. setp.9 에서 거른 계정의 게시글 링크를 얻음
11. 이전에 들렀던 기록이 남아있는 게시글이면 패스 
12. 30일 이내 게시글 방문  
  12-1. setp.1 에서 설정한 댓글 중 랜덤으로 하나뽑아서 댓글담  
  12-2. 만약 댓글달기가 막혀있으면 다음 게시글이 아닌 다음 계정으로 이동 (setp.9으로 이동)  
13.  setp.1 에서 좋아요 체크 되어있으면 좋아요 누름
14.  setp.1 에서 팔로우 눌렀으면 팔로우 누름  
    14-1. 팔로우 눌렀으면 setp.11 에 해당하는 방문기록 기록 ( tb_visited_account / tb_content_link)   
15. setp.9 으로 이동해 계정목록 다 돌 때까지 반복
16. 종료 --> tb_time_log 에 종료 시간 기록 
## 사용자 전달 
1. pyinstaller   .\instaToDB.spec  
2. pyinstaller   .\start.sepc
3. 해당 폴더 -> dist 폴더 진입
4. instaToDB.exe / start.exe / version 파일 zip 으로 묶어서 전달


## 주의사항
1. version 파일 수정 시 예전 버전으로 인식합니다.
2. main 창에 '업데이트 버전이 존재합니다' 라는 문구가 떠있다면  
  최신버전이 있다는 정보입니다.(version 파일로 구분)
3. 큰 문제가 없다면 사용해도 무방하나 start.exe 로 업데이트 이 후 사용하길 권장합니다.
4. 업데이트 하려면  릴리즈에  파일 업로드  
   (pyinstaller   .\instaToDB.spec   이 후 생긴 .exe 파일 zip으로 묶어서 업로드)


## 참고사항 
1. 기본적으로 css Selector 로 진행함
2. 인스타에서 종종 페이지 구조 바꾸는데 테스트 돌려서 어디 바뀐지 확인해야함..  
2-1. 안 바뀌었는데 안되면 time.sleep 늘려보기 (대부분 셀렉터 변경)

