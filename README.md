# OSS Project : recycle-ai-project

## ♻️ AI 분리수거 이미지 안내 서비스

AI 이미지 분류 모델을 활용하여 사용자가 업로드한 쓰레기 사진을 분석하고, 올바른 분리배출 방법을 안내합니다.


## 📖 프로젝트 소개

분리수거는 일상생활에서 반드시 필요한 활동이지만, 재활용 가능 여부와 배출 방법을 정확히 알기 어려운 경우가 많습니다.

본 프로젝트는 이미지 분류 AI 모델을 활용하여 사용자가 촬영하거나 업로드한 이미지를 분석하고, 품목을 자동으로 분류하여 올바른 분리배출 방법을 제공합니다.


## ✨ 주요 기능

### 📷 이미지 업로드

사용자가 분리수거 대상 물품 사진을 업로드하거나 직접 촬영합니다.

### 🤖 AI 이미지 분류

학습된 AI 모델이 이미지를 분석하여 다음 4개 품목 중 하나로 분류합니다.

* Can (캔)
* Paper (종이)
* Plastic (플라스틱)
* Vinyl (비닐)

### 📊 예측 결과 제공

* 분류 결과
* 예측 신뢰도(Confidence Score)

를 함께 제공합니다.

### ♻️ 분리배출 방법 안내

분류된 품목에 따라 올바른 분리배출 방법을 제공합니다.


## 🖥️ 서비스 화면

### 메인 화면


사용자는 이미지를 업로드하고 AI 분류 결과를 확인할 수 있습니다.

![메인화면](<docs/main.png>)

### 예측 결과 화면


업로드한 이미지를 기반으로 AI가 품목을 분류하고 신뢰도를 제공합니다.

![alt text](<docs/result.png>)



## 🧠 모델 개발 과정

### 데이터셋 구성

| 클래스       |     이미지 수 |
| --------- | --------: |
| Can       |       282 |
| Paper     |       514 |
| Plastic   |       431 |
| Vinyl     |       347 |
| **Total** | **1,574** |

### 모델 개선 과정

TensorFlow와 Pytorch 두 가지의 성능을 비교하여 모델을 개선했습니다. 

## 모델 성능 개선 과정

| 버전 | 주요 변경 사항 | 데이터셋 규모 | TensorFlow Validation Accuracy | PyTorch Validation Accuracy | 결과 |
|--------|----------------|----------------|-------------------------------|----------------------------|------|
| v1 | 기본 CNN 모델 학습 | Can 135 / Paper 125 / Plastic 114 / Vinyl 128 | 0.5200 | - | 기준 모델 |
| v2 | 데이터 증강 적용, Early Stopping 적용 | 동일 | 0.5900 | - | 성능 향상 확인 |
| v3 | 데이터 추가 수집, PyTorch 모델 실험 시작 | Can 282 / Paper 514 / Plastic 431 / Vinyl 347 | 0.4200 | 0.8286 | 데이터 증가만으로 성능 향상 실패 |
| v4 | Batch Normalization 추가 | 동일 | 0.5255 | 0.7746 | 효과 미미, 최종 모델에서 제외 |
| v5 | Learning Rate 조정 (0.0005) | 동일 | 0.8153 | 0.8381 | 큰 폭의 성능 향상 |
| v6 | Weight Decay 적용 | 동일 | - | 0.8444 | 성능 소폭 향상 |
| v7 | Data Augmentation 강화 | 동일 | - | 0.8444 | 성능 변화 없음 |
| v8 | MobileNetV2 전이학습 적용 | 동일 | **0.9204** | **0.9778** | 최고 성능 달성 |
### 최종 모델

#### MobileNetV2 Transfer Learning

Pytorch 기반 MobileNetV2 모델을 활용하여 이미지 분류 성능을 향상시켰습니다.

**적용 기법**

* Transfer Learning
* Data Augmentation
* Early Stopping
* Learning Rate Tuning

**학습 환경**

| 항목            | 값           |
| ------------- | ----------- |
| Framework     | Pytorch     |
| Model         | MobileNetV2 |
| Input Size    | 224 × 224   |
| Optimizer     | Adam        |
| Learning Rate | 0.0005      |
| Dropout       | 0.3         |



## 🏗️ 시스템 아키텍처

```text
사용자
   │
   ▼
이미지 업로드
   │
   ▼
이미지 전처리
(Resize, Normalize)
   │
   ▼
MobileNetV2
   │
   ▼
품목 예측
(Can / Paper / Plastic / Vinyl)
   │
   ▼
분리배출 방법 안내

```


## 👥 역할 분담

| 이름 | 담당 역할 | 주요 업무 |
|--------|--------|--------|
| 최서아 | TensorFlow 기반 모델 학습 및 성능 비교 | 데이터 수집, Tensorflow 모델 학습, Confusion Matrix 시각화 |
| 박영서 | 데이터셋 구축 및 PyTorch 모델 개발 | 데이터 수집, Pytorch 모델 학습, 모델별 성능 비교 |
| 박지수 | Streamlit 서비스 구현 및 모델-UI 연결 | 데이터 수집, Streamlit 구현, 모델 연동 |



## 📂 프로젝트 구조

```text
AI
│
├── docs
│   ├── class-standard.md
│   ├── dataset-collection-guide.md
│   ├── dataset-split.md
│   ├── dataset-statistics.md
│   ├── dataset-structure.md
│   ├── model_comparison.md
│   └── service-guide.md
│
├── model
│   └── best_model_mobilenetv2.pth
│
├── notebooks
│   └── final_model.ipynb
│
├── service
│   ├── guide.json
│   ├── inference.py
│   ├── best_model_mobilenetv2.pth
│   ├── requirements.txt
│   └── streamlit_app.py
│
├── src
    ├── data_rename.ipynb
    └── dataset.py

```

### 폴더 설명

| 폴더 | 설명 |
|--------|--------|
| docs | 프로젝트 문서 및 데이터셋 관리 문서 |
| model | 학습 완료된 최종 모델 저장 |
| notebooks | 모델 학습 및 실험 코드 |
| service | Streamlit 기반 웹 서비스 |
| src | 데이터 처리 및 유틸리티 코드 |




## 🚀 실행 방법

### 저장소 클론

```bash
git clone https://github.com/your-repository/recycle-ai.git
cd recycle-ai
```

### 패키지 설치

```bash
pip install -r requirements.txt
```

### 서비스 실행

```bash
streamlit run service/streamlit_app.py
```



## 🛠️ 사용 기술

### AI / Machine Learning

* TensorFlow
* Pytorch
* MobileNetV2

### Web

* Streamlit

### Data Processing

* NumPy
* Pandas
* Matplotlib


## 💡 기대 효과

* 올바른 분리배출 문화 정착
* 재활용률 향상
* 환경 보호 인식 개선
* AI 기반 환경 교육 서비스로 확장 가능


