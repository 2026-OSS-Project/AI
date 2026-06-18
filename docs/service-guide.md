# Streamlit 서비스 구현 구조

## 1. 서비스 역할

본 문서는 분리수거 이미지 안내 서비스의 Streamlit 화면 구현 구조를 설명한다.

해당 서비스는 사용자가 이미지를 업로드하면 업로드 이미지를 화면에 표시하고, AI 예측 결과와 카테고리별 분리배출 안내를 제공하는 역할을 한다.

데이터셋 구성, 클래스 기준, 데이터 분할 방식은 별도 문서에서 관리하며, 본 문서에서는 서비스 UI와 추론 연결 구조만 다룬다.

## 2. 서비스 폴더 구조

```text
service/ui/
├── streamlit_app.py
├── guide.json
└── requirements.txt
```

## 3. 파일별 역할

| 파일 | 역할 |
|---|---|
| streamlit_app.py | Streamlit 기반 서비스 화면 구현 |
| guide.json | 클래스별 분리배출 안내 문구 저장 |
| requirements.txt | Colab 및 실행 환경에 필요한 패키지 목록 |

## 4. 현재 구현된 기능

- 이미지 업로드 기능
- 업로드 이미지 미리보기
- AI 예측 결과 표시 영역
- 예측 신뢰도 표시 영역
- guide.json 기반 분리배출 안내 출력
- Colab 환경 실행 지원

## 5. 현재 예측 방식

현재 서비스는 실제 학습 모델 연결 전 단계이므로 임시 예측값을 사용한다.

```python
predicted_class = "plastic"
confidence = 0.91
```

따라서 어떤 이미지를 업로드해도 현재는 동일한 예측 결과가 출력된다.

이 내용은 현재 구현 상태를 설명하기 위한 것이며, 추후 모델 연결 이후에는 실제 inference 결과를 출력하는 방식으로 변경할 예정이다.

## 6. 추후 모델 연결 계획

학습된 모델 파일이 준비되면 별도의 `inference.py` 파일을 추가하여 예측 로직을 분리할 예정이다.

예상 구조는 다음과 같다.

```text
service/ui/
├── streamlit_app.py
├── inference.py
├── guide.json
├── requirements.txt
└── final_model.h5
```

`streamlit_app.py`에서는 업로드된 이미지를 `inference.py`로 전달하고, `inference.py`에서 예측 클래스와 신뢰도를 반환하는 방식으로 연결한다.

모델 연결 이후에는 현재 임시 예측값을 제거하고, 업로드 이미지에 따른 실제 예측 결과가 화면에 표시되도록 수정할 예정이다.

## 7. Colab 실행 관련 주의사항

본 프로젝트는 Colab 기반 실행을 기준으로 하므로, Streamlit 실행 시 localtunnel을 사용해 외부 접속 링크를 생성한다.

Colab에서 실행할 때는 `service/ui` 폴더로 이동한 뒤 `streamlit_app.py`를 실행해야 한다.
