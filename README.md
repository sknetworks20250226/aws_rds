# AWS RDS Django 프로젝트 배포 가이드

Django 웹 애플리케이션을 Docker를 사용하여 AWS EC2에 배포하는 과정

## 프로젝트 구조
```
AWS_RDS/
  ├── aws_rds/          # Django 프로젝트 디렉토리
  ├── board/            # Django 앱 디렉토리
  ├── static/           # 정적 파일 디렉토리
  ├── templates/        # 템플릿 디렉토리
  ├── docker-compose.yml
  ├── Dockerfile
  └── requirements.txt
```

## 배포 과정

### 1. Docker 이미지 빌드
로컬 환경에서 Docker 이미지를 빌드합니다:
```bash
docker build -t <도커허브아이디>/aws_rds:latest .
```

### 2. Docker Hub에 이미지 푸시
빌드된 이미지를 Docker Hub에 푸시합니다:
```bash
# Docker Hub 로그인
docker login

# 이미지 푸시
docker push <도커허브아이>/aws_rds:latest
```

### 3. AWS EC2 서버 설정

#### 3.1 필요한 파일 준비
EC2 서버에 다음 파일들을 복사합니다:
- `.env` 파일 (환경 변수 설정)
- `docker-compose.yml` 파일

#### 3.2 .env 파일 설정
`.env` 파일에는 다음과 같은 환경 변수들이 포함되어야 합니다:

```
NAME=데이터베이스 이름
USER=RDS 데이터베이스 계정명
PASSWORD=RDS 데이터베이스 패스워드
HOST=RDS DNS(엔드포인트)
PORT=3306
```

### 4. EC2에서 Docker 설치
EC2 서버에 Docker와 Docker Compose를 설치합니다:
```bash
# Docker 설치
sudo apt-get update
sudo apt-get install docker.io

# Docker Compose 설치
sudo apt-get install docker-compose
```

### 5. 애플리케이션 실행
EC2 서버에서 다음 명령어로 애플리케이션을 실행합니다:
```bash
sudo docker-compose up    #  종료하면 자동으로 컨터이너 중지 -- 테스트는 이걸로
sudo docker-compose up -d # 백그라인드로 실행(컨터이너 중지 따로 해야 함)
```

### 6. 배포 확인
- 웹 브라우저에서 `http://[EC2-PUBLIC-IP]:8000` 접속하여 애플리케이션 실행을 확인합니다.
- 로그 확인: `sudo docker-compose logs -f`

## 주의사항
- EC2 보안 그룹에서 포트 8000이 열려있는지 확인하세요.