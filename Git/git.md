
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


## Remote Repository (원격 저장소)

    코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

    ex) gitlab, github, bitbucket

### 1. 로컬 & 원격 저장소
---

#### - 로컬 저장소에 원격 저장소 추가
```cli
git remote add origin(닉네임) remote_repo_url(github 레포지토리 주소)
```

origin : 추가하는 원격 저장소 별칭

별칭을 사용해 로컬저장소에 여러개 연결할 수 있음

#### - 로컬 저장소에 원격 저장소 주소 등록

```cli
git remote add origin(다른이름이어도 상관 없음) 레포지토리 주소

잘 연결 되어 있는지 확인 
git remote -v 
```
![alt text](./images/image-4.png)

#### - push / pull & clone
- push

```cli
git push origin master
```
원격 저장소에 commit 목록을 업로드
-> git 아 origin이라는 이름의 원격 저장소에 master branch를 push해줘

!! 주의 !! 
파일 수정 후 저장후 커밋찍고 push 할 것

![alt text](./images/image-5.png)

local에 있는 branch인 master, 원격에 있는 branch인 origin/master 의 가장 최신 commit은 HEAD

#### !! 원격 저장소에는 commit이 올라가는 것!!

- pull & clone
```cli
git pull origin master
```
원격 저장소의 변경사항만을 받아옴(업데이트)

```cli
git clone remote_repo_url
```
원격 저장소 전체를 복제(다운로드)

!! branch 표시 없을 때 깃 클론 할 수 있다.

!! 이미 git init 되어있다.

@@ 참고 @@ 파일명 cli로 변경하고 싶을 때
```cli
mv -f 변경하고싶은파일명 변경할파일명
```

@@ 참고 @@

다른 인원 레포지토리 수정 원한다면 레포지토리 - 세팅 - 콜라보레이터 에서 인원 추가하고 레포지토리 주소 공유하기 그 후 참여자가 메세지 승인해야 함께 작업할 수 있음!!

## gitignore

Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일

예시)

    .gitignore 파일 생성 (확장자 없음)
    a.txt와 b.txt 파일 생성
    gitignore 파일 안에 a.txt 작성
    git init
    git status

git init 전에 gitignore 사용할 것!!

* 목록 생성 서비스 

https://www.toptal.com/developers/gitignore

에서 운영체제, 사용 언어 입력 후 복사하여 gitignore 파일에 복붙

-rm -r .git 

.git 삭제

## GitHub 활용

#### - TIL

    Today I Learned
    매일 내가 배운 것을 마크다운으로 정리해서 문서화 하는 것

문서화 하는 것 개발자로서 매우 중요하다!

![alt text](./images/image-6.png)