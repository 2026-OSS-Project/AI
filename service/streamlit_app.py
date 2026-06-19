import json
import base64
from io import BytesIO

import os
import streamlit as st
from PIL import Image
from inference import predict_image

st.set_page_config(
    page_title="분리수거 이미지 안내 서비스",
    page_icon="♻️",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
    <style>
    @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css");

    html, body, [class*="css"], .stApp {
        font-family: "Pretendard", -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, #DFF7E8 0, transparent 32%),
            radial-gradient(circle at top right, #E8F4FF 0, transparent 28%),
            linear-gradient(180deg, #F7FBF8 0%, #FFFFFF 48%, #F6FAF7 100%);
    }

    .block-container {
        padding-top: 2.2rem;
        padding-bottom: 4rem;
        max-width: 1380px;
    }

    .hero {
        padding: 42px 54px;
        border-radius: 32px;
        background: linear-gradient(135deg, #1F7A43 0%, #35B86B 56%, #85DDA6 100%);
        color: white;
        box-shadow: 0 18px 48px rgba(31, 122, 67, 0.22);
        margin-bottom: 42px;
    }

    .hero-badge {
        display: inline-block;
        padding: 9px 16px;
        border-radius: 999px;
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.32);
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 850;
        letter-spacing: -2px;
        line-height: 1.15;
        margin-bottom: 22px;
        white-space: nowrap;
    }

    .hero-desc {
        font-size: 18px;
        line-height: 1.7;
        color: rgba(255,255,255,0.94);
        white-space: nowrap;
    }

    .card {
        background: rgba(255,255,255,0.92);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(220, 232, 224, 0.95);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 12px 34px rgba(30, 60, 40, 0.08);
        margin-bottom: 26px;
    }

    .card-title {
        font-size: 24px;
        font-weight: 850;
        letter-spacing: -0.7px;
        color: #1F2A24;
        margin-bottom: 10px;
    }

    .card-sub {
        font-size: 15px;
        color: #6A756E;
        line-height: 1.65;
        margin-bottom: 0;
    }

    .preview-empty {
        margin-top: 26px;
        padding: 44px 28px;
        border-radius: 24px;
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FBF9 100%);
        border: 1px solid #E5EFE8;
        text-align: center;
        color: #7A857D;
    }

    .preview-icon {
        font-size: 40px;
        opacity: 0.45;
        margin-bottom: 12px;
    }

    .preview-title {
        font-size: 16px;
        font-weight: 800;
        color: #5F6963;
        margin-bottom: 8px;
    }

    .preview-sub {
        font-size: 14px;
        color: #8A948D;
        line-height: 1.6;
    }

    .image-title {
        font-size: 22px;
        font-weight: 850;
        color: #1F2A24;
        margin-top: 8px;
        margin-bottom: 8px;
    }

    .image-sub {
        font-size: 14px;
        color: #6A756E;
        margin-bottom: 16px;
    }

    .uploaded-image-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(220, 232, 224, 0.95);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 12px 34px rgba(30, 60, 40, 0.08);
        margin-top: 26px;
        margin-bottom: 26px;
    }

    .uploaded-image-box {
        margin-top: 20px;
        border-radius: 22px;
        overflow: hidden;
        border: 1px solid #E5EFE8;
        background: #F8FBF9;
    }

    .uploaded-image-box img {
        width: 100%;
        max-height: 420px;
        object-fit: contain;
        display: block;
    }

    .flow-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(220, 232, 224, 0.95);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 12px 34px rgba(30, 60, 40, 0.08);
        margin-bottom: 26px;
    }

    .flow-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }

    .flow-icon {
        font-size: 24px;
    }

    .flow-title {
        font-size: 24px;
        font-weight: 850;
        letter-spacing: -0.7px;
        color: #1F2A24;
    }

    .flow-sub {
        font-size: 15px;
        color: #6A756E;
        line-height: 1.65;
        margin-bottom: 26px;
    }

    .flow-steps {
        display: grid;
        grid-template-columns: 1fr 20px 1fr 20px 1fr;
        align-items: stretch;
        gap: 12px;
    }

    .flow-step {
        padding: 30px 18px;
        border-radius: 22px;
        background: #FFFFFF;
        border: 1px solid #E5EFE8;
        text-align: center;
        min-height: 130px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .flow-step-icon {
        font-size: 36px;
        margin-bottom: 18px;
    }

    .flow-step-title {
        font-size: 16px;
        font-weight: 850;
        color: #1F2A24;
        margin-bottom: 0;
        white-space: nowrap;
        word-break: keep-all;
    }

    .flow-arrow {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #8A948D;
        font-size: 24px;
        font-weight: 700;
    }

    .tip-box {
        margin-top: 28px;
        padding: 18px 20px;
        border-radius: 20px;
        background: #F1FAF4;
        border: 1px solid #CFE9D8;
        color: #303833;
    }

    .tip-title {
        font-size: 15px;
        font-weight: 850;
        color: #1F7A43;
        margin-bottom: 8px;
    }

    .tip-desc {
        font-size: 14px;
        color: #5F6963;
        line-height: 1.6;
    }

    .prediction-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(220, 232, 224, 0.95);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 12px 34px rgba(30, 60, 40, 0.08);
        margin-bottom: 26px;
    }

    .prediction-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
        margin-top: 22px;
    }

    .prediction-box {
        padding: 24px 26px;
        border-radius: 22px;
        background: #FFFFFF;
        border: 1px solid #E5EFE8;
    }

    .prediction-label {
        font-size: 15px;
        color: #6A756E;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .prediction-value {
        font-size: 32px;
        color: #1F7A43;
        font-weight: 850;
        letter-spacing: -1px;
    }

    .prediction-bar-wrap {
        margin-top: 22px;
        height: 12px;
        background: #E9F2EC;
        border-radius: 999px;
        overflow: hidden;
    }

    .prediction-bar {
        height: 12px;
        background: linear-gradient(90deg, #35B86B, #1F7A43);
        border-radius: 999px;
    }

    .guide-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(220, 232, 224, 0.95);
        border-radius: 28px;
        padding: 30px;
        box-shadow: 0 12px 34px rgba(30, 60, 40, 0.08);
        margin-bottom: 26px;
        min-height: 420px;
    }

    .guide-list-box {
        margin-top: 18px;
        padding: 20px 22px;
        border-radius: 22px;
        background: #FFFFFF;
        border: 1px solid #E5EFE8;
        min-height: 260px;
    }

    .guide-line {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 11px 0;
        color: #303833;
        font-size: 15px;
        line-height: 1.55;
        border-bottom: 1px solid #EEF4F0;
    }

    .guide-line:last-child {
        border-bottom: none;
    }

    .check {
        flex: 0 0 auto;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: #E4F7EA;
        color: #1F7A43;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 850;
        margin-top: 1px;
    }

    .warning-box {
        padding: 16px 18px;
        border-radius: 18px;
        background: #FFF7E6;
        border: 1px solid #FFE0A3;
        color: #6A4A00;
        margin-top: 16px;
        line-height: 1.6;
    }

    div[data-testid="stFileUploader"] {
        padding: 18px;
        border-radius: 22px;
        background: #F9FEFA;
        border: 1px dashed #9ED8B0;
        margin-bottom: 28px;
    }

    div[data-testid="stFileUploader"] section {
        border: none;
        background: transparent;
    }

    img {
        border-radius: 22px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# guide data
# -----------------------------
with open(os.path.join(os.path.dirname(__file__), "guide.json"), "r", encoding="utf-8") as f:
    guide_data = json.load(f)

# -----------------------------
# hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">AI Image Recycling Guide</div>
        <div class="hero-title">♻️ 분리수거 이미지 안내 서비스</div>
        <div class="hero-desc">
            분리수거가 헷갈리는 물건 사진을 업로드하면 AI가 이미지를 분석해 분류 결과와 올바른 배출 방법을 안내합니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# main layout
# -----------------------------
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">이미지 업로드</div>
            <div class="card-sub">
                분리수거할 물건이 잘 보이도록 촬영한 이미지를 업로드해주세요.<br>
                JPG, JPEG, PNG 파일을 지원합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "이미지를 업로드해주세요.",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        uploaded_image_html = (
            '<div class="uploaded-image-card">'
            '<div class="image-title">업로드한 이미지</div>'
            '<div class="image-sub">현재 선택한 이미지입니다.</div>'
            '<div class="uploaded-image-box">'
            f'<img src="data:image/png;base64,{img_base64}" alt="uploaded image">'
            '</div>'
            '</div>'
        )

        st.markdown(uploaded_image_html, unsafe_allow_html=True)

    else:
        st.markdown(
            """
            <div class="preview-empty">
                <div class="preview-icon">🖼️</div>
                <div class="preview-title">아직 업로드된 이미지가 없습니다.</div>
                <div class="preview-sub">
                    물건 사진을 업로드하면<br>
                    분석 결과가 이곳에 표시됩니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

with right:
    if uploaded_file is not None:
        # 임시 예측 결과 — 나중에 실제 AI 모델 연결 시 변경
        predicted_class, confidence = predict_image(image)
        class_name = guide_data[predicted_class]["name"]
        confidence_percent = confidence * 100

        prediction_html = (
            '<div class="prediction-card">'
            '<div class="card-title">AI 예측 결과</div>'
            '<div class="card-sub">업로드된 이미지를 기반으로 예측한 결과입니다.</div>'
            '<div class="prediction-grid">'
            '<div class="prediction-box">'
            '<div class="prediction-label">분류 결과</div>'
            f'<div class="prediction-value">{class_name}</div>'
            '</div>'
            '<div class="prediction-box">'
            '<div class="prediction-label">신뢰도</div>'
            f'<div class="prediction-value">{confidence_percent:.2f}%</div>'
            '</div>'
            '</div>'
            '<div class="prediction-bar-wrap">'
            f'<div class="prediction-bar" style="width: {confidence_percent}%;"></div>'
            '</div>'
            '</div>'
        )

        st.markdown(prediction_html, unsafe_allow_html=True)

        guide_html = (
            '<div class="guide-card">'
            '<div class="card-title">분리배출 방법</div>'
            '<div class="card-sub">예측된 카테고리에 따른 배출 안내입니다.</div>'
            '<div class="guide-list-box">'
        )

        for guide in guide_data[predicted_class]["guide"]:
            guide_html += (
                '<div class="guide-line">'
                '<div class="check">✓</div>'
                f'<div>{guide}</div>'
                '</div>'
            )

        guide_html += (
            '</div>'
            '</div>'
        )

        st.markdown(guide_html, unsafe_allow_html=True)

        if confidence < 0.6:
            warning_html = (
                '<div class="warning-box">'
                '예측 신뢰도가 낮습니다. 흰색 또는 단색 배경에서 물체가 더 크게 보이도록 다시 촬영한 이미지를 업로드해 주세요.'
                '</div>'
            )
            st.markdown(warning_html, unsafe_allow_html=True)

    else:
        flow_html = (
            '<div class="flow-card">'
            '<div class="flow-header">'
            '<div class="flow-icon">✦</div>'
            '<div class="flow-title">사용 방법</div>'
            '</div>'
            '<div class="flow-sub">서비스 사용 흐름은 아래와 같습니다.</div>'
            '<div class="flow-steps">'
            '<div class="flow-step">'
            '<div class="flow-step-icon">☁️</div>'
            '<div class="flow-step-title">이미지 업로드</div>'
            '</div>'
            '<div class="flow-arrow">›</div>'
            '<div class="flow-step">'
            '<div class="flow-step-icon">🧠</div>'
            '<div class="flow-step-title">AI 분류</div>'
            '</div>'
            '<div class="flow-arrow">›</div>'
            '<div class="flow-step">'
            '<div class="flow-step-icon">🌿</div>'
            '<div class="flow-step-title">배출 안내</div>'
            '</div>'
            '</div>'
            '<div class="tip-box">'
            '<div class="tip-title">TIP</div>'
            '<div class="tip-desc">더 정확한 분석을 위해 물건이 선명하고 전체가 보이도록 촬영해주세요.</div>'
            '</div>'
            '</div>'
        )

        st.markdown(flow_html, unsafe_allow_html=True)
