import mlflow

class ModelService:
    def __init__(self):
        self.model_version = "v1.0.0-baseline"

    def predict(self, query: str) -> dict:
        confidence = 0.98
        label = "ACCEPTABLE" if len(query) > 10 else "INSUFFICIENT_CONTEXT"

        with mlflow.start_run(run_name="inference_call", nested=True):
            mlflow.log_param("query_length", len(query))
            mlflow.log_metric("confidence_score", confidence)

        return {
            "status": "success",
            "prediction": label,
            "confidence": confidence,
            "model_version": self.model_version
        }

model_service = ModelService()
