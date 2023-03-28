# 👨🏼‍⚖️ Sellon (Backend)

<img width="955" alt="image" src="https://user-images.githubusercontent.com/71240296/228106099-ce7b7d1c-1f19-4556-8642-e2b76bfa507f.png">


## 🙇‍♂️ contributors

- [👨🏻 이승환](https://github.com/sh981013s)
- [👨🏻 김지형](https://github.com/jihyoung9912)
- [👧🏻 남채원](https://github.com/Chaewon14)
- [👧🏻 양유진](https://github.com/yoojinyang0303)
- [👧🏻 허유라](https://github.com/youra-0526)
- [👨🏻 김신건](https://github.com/shinkeonkim)
- [👨🏻 송경석](https://github.com/songks0922)

## 💁🏻‍♂️ Github for Frontend

https://github.com/bunderLikeLion/sellon_backend

## 📄 Description

`멋쟁이 사자처럼 10기 전체 해커톤` 당시에 현대 사회에서 지속적으로 쌓여가는 잡동사니에 대한 공간적 문제를 해결 하고자 기존 물품과 돈이 거래되는 시장에서 탈피하여
본인에게 현재 필요없는 잡동사니와 잡동사니를 경매식으로 교환하는 플랫폼을 개발하였습니다. `(🥉 약 900 명 참여, 150팀 중 동상 수상)`

* `📑 발표자료:` https://drive.google.com/file/d/1Uwi3p94A6QNPQz38whTSGdtU1dAzWQ5T/view?usp=sharing 

## 🖥 Demo


* `📼 Live Demo viodeo on Youtube:` <a href="https://www.youtube.com/watch?v=ackofamRNHc" target="\_blank">https://www.youtube.com/watch?v=ackofamRNHc </a>

## 🕸 Infrastructure

<img src="./public/readme/infra.png" width="70%" height="60%">


## 🎠 기능


#### 👩‍🌾 User

- [x] **회원 가입**
- [x] **로그인**
- [x] **로그아웃**
- [x] **회원 정보 수정**
- [x] **회원 탈퇴**

#### 🧧 Item

- [x] **아이템 등록**
- [x] **아이템 상세보기**
- [x] **아이템 수정**
- [x] **아이템 삭제**

#### 👨🏼‍⚖️ Auction

- [x] **경매 등록**
- [x] **아이템 묶음 채택**
- [x] **경매 철회**
- [x] **채팅**

#### 🏆 Statistics

- [x] **최다 거래자 및 각종 통계 도출**

## Dev Settings

1. 패키지매니저로 pipenv를 활용합니다.
```sh
# Mac인경우
> brew install pipenv

# Windows인 경우
> pip install pipenv


> cd webapp
> pipenv install
```

2. pre-commit을 설정합니다. (1번 수행 후)
```sh
> pre-commit install
```

## Commands
### nginx reload
```
docker exec -it nginx-dev-container nginx -s reload
```

### 로그 보기
```
## 전체
docker-compose logs -f

## webapp 로그 보기
docker-compose logs -f webapp
```

### 슈퍼 유저 생성
```
docker-compose run --rm webapp python manage.py createsuperuser
```

### 마이그레이션 생성
```
docker-compose run --rm webapp python manage.py makemigrations
```

### erd 생성
```
pipenv install --dev
python ./manage.py graph_models user product file_manager auction dealing --pydot -a -o erd.png
```
