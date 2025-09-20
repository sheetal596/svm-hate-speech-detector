<<<<<<< HEAD
# svm-hate-speech-detector
Interactive Streamlit web app that classifies text as safe or offensive using a TF-IDF + SVM model (94.7 % accuracy) trained on a 24,783-row dataset; includes per-line predictions, safe/offensive percentages, and a pie-chart visualization.
=======
#  Hate Speech Detection App

A **Streamlit web application** that detects abusive or offensive text using a
Support Vector Machine (SVM) model trained on a labeled hate-speech dataset.

---

##  Project Overview
- **Purpose:** Classify text as Safe or Offensive in real time.
- **Interface:** Simple browser app built with [Streamlit](https://streamlit.io/).
- **Visualization:** Displays per-line predictions and a pie chart of safe vs offensive percentages.

---

##  Model Details
- **Algorithm:** Linear SVM (Support Vector Machine)
- **Vectorizer:** TF-IDF (Term Frequency – Inverse Document Frequency)
- **Dataset Size:** **24,783 rows × 7 columns**  
  - Columns include: *text*, *label*, and additional metadata/features.
- **Training/Test Split:** 80 / 20
- **Performance on Test Set:**
  - **Accuracy:** 94.7 %
  - **Precision (Offensive class):** 0.99
  - **Recall (Offensive class):** 0.95
  - **F1 Score (Offensive class):** 0.97
  - **Precision (Safe class):** 0.78
  - **Recall (Safe class):** 0.95
  - **F1 Score (Safe class):** 0.86

The model and vectorizer are bundled together in **`hatespeech.pkl`** for easy loading.

---

## Repository Structure
>>>>>>> 16ae740 (Initial commit: Streamlit hate-speech detection app)
