# BE-Translate_Pipeline

번역 파이프라인을 위한 FastAPI 백엔드 서버입니다.

## 🚀 시작하기

### 필수 요구사항

- Python 3.11+
- pip 또는 poetry

### 설치 및 실행

1. **저장소 클론**

```bash
git clone <repository-url>
cd BE-Translate_Pipeline
```

2. **가상환경 생성 및 활성화**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **의존성 설치**

```bash
pip install -r requirements.txt
```

4. **환경 변수 설정**

```bash
# .env 파일을 생성하고 필요한 환경 변수를 설정하세요
cp config.py .env  # config.py를 참고하여 .env 파일 생성
```

5. **서버 실행**

```bash
# 개발 모드
python main.py

# 또는 uvicorn 직접 실행
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Docker를 사용한 실행

1. **Docker 이미지 빌드 및 실행**

```bash
docker build -t translate-pipeline .
docker run -p 8000:8000 translate-pipeline
```

2. **Docker Compose 사용**

```bash
docker-compose up --build
```

## 📚 API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔧 주요 엔드포인트

- `GET /` - 기본 상태 확인
- `GET /health` - 헬스 체크
- `POST /translate` - 텍스트 번역

## 🛠️ 개발

### 프로젝트 구조

```
BE-Translate_Pipeline/
├── main.py              # FastAPI 메인 애플리케이션
├── config.py            # 설정 관리
├── requirements.txt     # Python 의존성
├── Dockerfile          # Docker 설정
├── docker-compose.yml  # Docker Compose 설정
└── README.md           # 프로젝트 문서
```

### 환경 변수

- `PORT`: 서버 포트 (기본값: 8000)
- `HOST`: 서버 호스트 (기본값: 0.0.0.0)
- `ENVIRONMENT`: 실행 환경 (development/production)
- `DEBUG`: 디버그 모드 활성화 여부

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
