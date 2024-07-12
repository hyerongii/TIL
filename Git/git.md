
# GIT
## 버전관리
변화를 기록하고 추적하는 것
- 중앙 집중식: 버전은 중앙서버에 저장되고 중앙 서버에서 파일을 가져와 중앙에 업로드
- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리

    → 작업 하기 전에 서버의 버전과 비교하여 항상 최신으로 업데이트 할 것
## git의 영역
- Working Directory

    실제 작업 중인 파일들이 위치하는 영역
- Staging Area
    
    워킹 디렉토리에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository
    
    버전 이력과 파일들이 영구적으로 저장되는 영역
    모든 버전과 변경 이력이 기록됨
## git의 문자
- git init
    
    로컬 저장소 설정(초기화) 
    
    → git의 버전 관리를 시작할 디렉토리에서 진행
- git add
    
    변경사항이 있는 파일을 staging area에 추가
    
    파일, 폴더 관계없음
    ```cli
    git add a.txt, b.txt 
    git add *.txt 
    (txt 확장자 파일 전부 올리고 싶을 때)
    git add . 
    (디렉토리 내 모든 파일 전부 올리고 싶을 때)
    ```
- git commit

    staging area에 있는 파일들을 저장소에 기록
    
    변경이력 생성
    
    **주의!! git add를 통해 satging area에 꼭 올리기!**

    ```cli
    git commit -m “설정할 커밋 이름”
    ```
- git status

    현재 git이 커밋된 것이 있는지 현재 상태 출력해줌
- git rm —cached
    
    stage에 올라간 파일을 디렉토리로 이동하고 싶을 때

- git config --global
    레포지토리 같이 사용할 때
    ID 먼저 입력 해주고 commit 할 수 있음
    사용자 설정
    ```cli
    git config --global user.email "이메일 입력"
    git config --global user.name "닉네임 입력" 
    ```
- git log

    commit 목록 확인

    작성자, 날짜, 메세지 나옴
    
- git log --oneline 
    
    한줄로 각 커밋 정보 간략하게 보여줌
    
- HEAD 는 최신의 commit를 따라감
