import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# ---------- Load the trained vectorizer and model ----------
@st.cache_resource
def load_artifacts():
    with open("hate_speech_model.pkl", "rb") as f:
        model_data = pickle.load(f)
    vectorizer = model_data["vectorizer"]
    svm_model = model_data["model"]
    return vectorizer, svm_model

vectorizer, svm_model = load_artifacts()

# ---------- App UI ----------
st.title("🛡️ Abusive Comment Detector")
st.caption("Enter one or more comments (one per line). We'll classify each comment and show overall safe/offensive percentages.")

user_text = st.text_area(
    "Comments:",
    height=180,
    placeholder="One comment per line...\nI love this place\nYou are horrible\nHave a nice day",
)

if st.button("Analyze"):
    if not user_text.strip():
        st.warning("Please enter at least one comment.")
    else:
        # Split input into non-empty lines
        lines = [line.strip() for line in user_text.splitlines() if line.strip()]
        X = vectorizer.transform(lines)
        preds = svm_model.predict(X)  # assumes 1 = Offensive, 0 = Safe

        total = len(preds)
        offensive = int(np.sum(preds))
        safe = total - offensive
        offensive_pct = round(offensive / total * 100, 1)
        safe_pct = round(100 - offensive_pct, 1)

        # Per-line predictions
        st.subheader("Predictions")
        for text, p in zip(lines, preds):
            label = "🚫 Offensive" if p == 1 else "✅ Safe"
            st.write(f"{label} — {text}")

        # Overall analysis
        st.subheader("Overall Content Analysis")
        col1, col2 = st.columns(2)
        col1.metric("Safe content", f"{safe_pct}%", f"{safe}/{total}")
        col2.metric("Offensive content", f"{offensive_pct}%", f"{offensive}/{total}")

        # Pie chart
        fig, ax = plt.subplots()
        ax.pie([safe, offensive], labels=["Safe", "Offensive"],
               autopct="%1.1f%%", startangle=90, colors=["#4CAF50", "#FF5252"])
        ax.axis("equal")
        st.pyplot(fig)
