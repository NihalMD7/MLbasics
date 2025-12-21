# MLbasics

Welcome — this repository contains clear, beginner-friendly examples and notes that explain core concepts in Machine Learning (ML) and related fields. The goal is to give students and newcomers practical, hands-on exposure to fundamental algorithms, typical workflows, and small demonstrative projects.

Authored by: Nihal baba Mohammad (from CSU)

---

## Quick overview

- Audience: students, beginners, and anyone learning ML fundamentals.
- Content style: short explanations, Jupyter notebooks, simple implementations, and visualizations.
- Focus: understanding concepts (not production-ready code).

---

## Flowchart: High-level view of AI → ML → subfields

```text
Artificial Intelligence (AI)
│
├── 🤖 Narrow AI (Weak AI)
│   └── Performs specific tasks (e.g., image recognition, translation)
│
├── 🧠 General AI (AGI)
│   └── Human-level intelligence across domains (not yet achieved)
│
└── 💡 Subfields of AI
    │
    ├── 🔍 Machine Learning (ML)
    │   │
    │   ├── 🎯 Supervised Learning
    │   │   ├── Regression (predict continuous values)
    │   │   │   ├── Linear Regression
    │   │   │   └── Polynomial Regression
    │   │   └── Classification (predict categories)
    │   │       ├── Logistic Regression
    │   │       ├── Decision Trees, Random Forests
    │   │       ├── SVM, KNN, Naive Bayes
    │   │       └── Deep Learning (CNNs, RNNs, Transformers)
    │   │
    │   ├── 🔍 Unsupervised Learning
    │   │   ├── Clustering
    │   │   │   ├── K-Means
    │   │   │   ├── Hierarchical
    │   │   │   └── DBSCAN
    │   │   └── Dimensionality Reduction
    │   │       ├── PCA
    │   │       └── t-SNE, UMAP
    │   │
    │   └── 🎲 Reinforcement Learning (RL)
    │       ├── Model-Free (Q-Learning, DQN)
    │       └── Model-Based (MCTS, AlphaGo)
    │
    ├── 🧠 Deep Learning (DL)
    │   ├── Feedforward Neural Networks (MLPs)
    │   ├── Convolutional Neural Networks (CNNs)
    │   ├── Recurrent Neural Networks (RNNs, LSTMs)
    │   └── Transformers (BERT, GPT)
    │
    ├── 🗣️ Natural Language Processing (NLP)
    │   ├── Text Classification, Sentiment Analysis
    │   ├── Machine Translation
    │   ├── Question Answering
    │   └── Large Language Models (LLMs)
    │
    ├── 👁️ Computer Vision (CV)
    │   ├── Image Classification
    │   ├── Object Detection (YOLO, Faster R-CNN)
    │   └── Image Generation (GANs, Diffusion Models)
    │
    └── 🤝 Robotics & Planning
        ├── Motion Planning
        └── Autonomous Agents
```

---

## What you'll find here

- Short explanations of important ML topics (supervised, unsupervised, reinforcement learning).
- Simple implementations (e.g., linear/logistic regression, k-means, PCA).
- Jupyter notebooks with walkthroughs and visualizations.
- Small examples using scikit-learn, NumPy, pandas, and basic PyTorch/TensorFlow where relevant.
- Recipe-style notebooks that show:
  - Problem → Dataset → Model → Training → Evaluation → Interpretation

---

## Getting started (local)

1. Clone the repository:
   - git clone https://github.com/NihalMD7/MLbasics.git
2. Create a virtual environment and install common dependencies:
   - python -m venv venv
   - source venv/bin/activate  (Windows: venv\Scripts\activate)
   - pip install -r requirements.txt
   - If no requirements file exists yet, start with: pip install numpy pandas scikit-learn matplotlib jupyter
3. Open a notebook:
   - jupyter notebook
4. Explore the notebooks in the repository root and subfolders.

---

## Suggested learning path (for this repo)

1. Linear Regression — understand loss, gradient descent, evaluation (MSE, R²).
2. Logistic Regression & Classification — confusion matrix, precision/recall, ROC.
3. Decision Trees & Ensemble Methods — bias/variance intuition.
4. Unsupervised Learning — clustering with k-means, dimensionality reduction with PCA.
5. Intro to Neural Networks — MLPs, then CNN basics for images and simple RNN/LSTM examples for sequences.
6. Small projects: classification on Iris/MNIST/CIFAR-10 subsets, clustering on synthetic and real datasets.

---

Author: Nihal baba Mohammad — GitHub: [NihalMD7](https://github.com/NihalMD7)

---
