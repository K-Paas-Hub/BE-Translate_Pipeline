from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import Optional
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

app = FastAPI(
    title="Translate Pipeline API",
    description="번역 파이프라인을 위한 FastAPI 서버",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청/응답 모델
class TranslateRequest(BaseModel):
    text: str
    source_lang: Optional[str] = "auto"
    target_lang: str = "ko"

class TranslateResponse(BaseModel):
    translated_text: str
    source_lang: str
    target_lang: str

# 기본 엔드포인트
@app.get("/")
async def root():
    return {"message": "Translate Pipeline API가 실행 중입니다!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "서버가 정상적으로 작동 중입니다"}

# 번역 엔드포인트 (예시)
@app.post("/translate", response_model=TranslateResponse)
async def translate_text(request: TranslateRequest):
    """
    텍스트를 번역합니다.
    """
    try:
        # 여기에 실제 번역 로직을 구현하세요
        # 현재는 예시 응답을 반환합니다
        translated_text = f"[번역됨] {request.text}"
        
        return TranslateResponse(
            translated_text=translated_text,
            source_lang=request.source_lang,
            target_lang=request.target_lang
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"번역 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
