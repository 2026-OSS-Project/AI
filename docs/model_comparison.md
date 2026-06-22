# 모델 성능 비교표
### 데이터셋 구성 (V3 기준)

| 클래스 | 이미지 수 |
| --- | ---: |
| can | 281 |
| paper | 514 |
| plastic | 432 |
| vinyl | 347 |
| **총합** | **1,574** |

---

## PyTorch 모델 성능 비교

| 버전 | 개선 내용 | 정확도 (Accuracy) | 증감 |
| :---: | --- | :---: | :---: |
| V3 | 데이터 추가 수집 | 0.8286 | - |
| V4 | Batch Normalization 적용 | 0.7746 | ▼ 0.0540 |
| V5 | Learning Rate 조정 | 0.8381 | ▲ 0.0635 |
| V6 | Weight Decay 적용 | 0.8444 | ▲ 0.0063 |
| V7 | Data Augmentation 강화 | 0.8444 | - |
| V8 | Conv Layer 추가 | 0.8540 | ▲ 0.0096 |
| V9 | MobileNetV2 적용 | **0.9778** | ▲ 0.1238 |

## TensorFlow 모델 성능 비교

| 버전 | 개선 내용 | 정확도 (Accuracy) | 증감 |
| :---: | --- | :---: | :---: |
| V1 | 기본 CNN | 0.5199 | - |
| V2 | Data Augmentation 적용 | 0.4200 | ▼ 0.0999 |
| V3 | 데이터 추가 수집 | 0.5900 | ▲ 0.1700 |
| V4 | Batch Normalization 적용 | 0.5255 | ▼ 0.0645 |
| V5 | Learning Rate 조정 | 0.8153 | ▲ 0.2898 |
| V8 | MobileNetV2 적용 | **0.9204** | ▲ 0.1051 |

---

## 전체 성능 비교

| 개선 단계 | TensorFlow | PyTorch |
| --- | :---: | :---: |
| 기본 CNN (V1) | 0.5199 | - |
| Data Augmentation (V2) | 0.4200 | - |
| 데이터 추가 수집 (V3) | 0.5900 | 0.8286 |
| Batch Normalization (V4) | 0.5255 | 0.7746 |
| Learning Rate 조정 (V5) | 0.8153 | 0.8381 |
| Weight Decay (V6) | - | 0.8444 |
| Data Augmentation 강화 (V7) | - | 0.8444 |
| Conv Layer 추가 (V8) | - | 0.8540 |
| MobileNetV2 적용 (V9) | **0.9204** | **0.9778** |

---

## 주요 결과 분석

- 데이터 추가 수집 이후 두 프레임워크 모두 성능이 향상되었다.
- Batch Normalization 적용 시 두 프레임워크 모두 정확도가 감소하였다.
- Learning Rate 조정은 가장 큰 성능 향상을 보인 하이퍼파라미터 튜닝 요소였다.
- PyTorch에서는 Weight Decay와 Conv Layer 추가를 통해 추가적인 성능 개선이 이루어졌다.
- MobileNetV2 전이학습 적용 결과, TensorFlow와 PyTorch 모두 기존 CNN 모델 대비 큰 폭의 성능 향상을 보였다.
- 최종 모델 기준 PyTorch MobileNetV2가 **97.78%**의 최고 정확도를 기록하였다.