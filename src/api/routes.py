from fastapi import FastAPI, HTTPException
from src.api.schemas import InferenceRequest, InferenceResponse
from src.services.inference import model_service

app = FastAPI(
    title="Secure MLOps Guardrail Pipeline",
    description="Production API with input sanitization and MLOps logging",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "inference-engine"}

@app.post("/v1/predict", response_model=InferenceResponse)
def run_inference(payload: InferenceRequest):
    try:
        return model_service.predict(payload.query)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal inference failure")
