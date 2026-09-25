# Secure MLOps Guardrail & Inference Pipeline

![CI/CD Pipeline](https://github.com/shoboyz-arch/secure-mlops-guardrail-pipeline/actions/workflows/ci.yml/badge.svg)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Production%20Ready-009688.svg)
![Security Guardrails](https://img.shields.io/badge/Security-Deterministic%20Sanitization-red.svg)

A production-grade machine learning inference architecture built with deterministic input guardrails, dynamic experiment telemetry via MLflow, containerized isolation, and automated CI/CD validation.

---

## Key Architectural Features

- **Deterministic Security Guardrails:** Regex and schema-driven input validation using **Pydantic** to reject adversarial prompt injections and malformed payloads before inference execution.
- **FastAPI Model Microservice:** High-performance REST API with asynchronous execution, automatic OpenAPI documentation, and health endpoints.
- **MLflow Operational Observability:** Dynamic logging of request telemetry, query lengths, and model confidence scores.
- **Hardened Containerization:** Non-root execution in a lightweight Debian-slim **Docker** container adhering to CIS security benchmarks.
- **Automated CI/CD:** **GitHub Actions** workflow performing static code analysis (Flake8) and automated test-suite verification (PyTest) on every push.

---

## Directory Architecture

```text
secure-mlops-guardrail-pipeline/
├── .github/workflows/
│ └── ci.yml # GitHub Actions CI/CD automation
├── src/
│ ├── api/
│ │ ├── routes.py # FastAPI health and inference endpoints
│ │ └── schemas.py # Pydantic input/output schemas & guardrails
│ └── services/
│ └── inference.py # Model inference engine & MLflow telemetry
├── tests/
│ └── test_guardrails.py # Unit & adversarial prompt injection tests
├── Dockerfile # Production-hardened container spec
├── requirements.txt # Pinned dependency manifest
└── README.md # Systems architecture & deployment guide

