# 🚀 Customer Segmentation using K-Means | Streamlit • Docker • Hugging Face

An end-to-end Machine Learning project that segments customers using **K-Means clustering**, visualizes insights with **PCA**, and provides a **Streamlit web app** for real-time predictions. Fully containerized with **Docker** and deployed on **Hugging Face Spaces**.

---

## 📌 Overview

Customer segmentation enables businesses to group customers based on behavior and demographics to drive better marketing and product strategies.

This project:

* Applies **K-Means clustering** for segmentation
* Uses **feature scaling** for better model performance
* Visualizes clusters using **PCA (2D projection)**
* Provides an **interactive Streamlit app**
* Supports **Docker-based deployment**
* Hosted on **Hugging Face Spaces**

---

## 🧠 Machine Learning Pipeline

* Algorithm: **K-Means Clustering**
* Preprocessing: **StandardScaler**
* Visualization: **PCA**
* Model Selection: **Elbow Method**

---

## 📊 Features Used

* Age
* Income
* Total Spending
* Number of Store Purchases
* Number of Web Purchases
* Number of Web Visits per Month

---

## 🎯 Customer Segments

| Cluster | Segment             |
| ------- | ------------------- |
| 0       | Budget Customers    |
| 1       | Premium Customers   |
| 2       | Loyal High Spenders |
| 3       | Regular Customers   |
| 4       | Occasional Buyers   |
| 5       | VIP Customers       |

---

## 🖥️ Streamlit App

The app allows users to:

* Enter customer details
* Predict customer segment
* Get business recommendations

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/Vaibhavv526/Customer_Segmentation.git
cd Customer_Segmentation
```

---

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Run Locally

```bash
streamlit run segmentation.py
```

👉 Open in browser:

```
http://localhost:8501
```

---

## 🐳 Docker Usage (Recommended)

### 🔹 Build Docker Image

```bash
docker build -t customer-segmentation .
```

---

### 🔹 Run Container

```bash
docker run -p 8501:8501 customer-segmentation
```

👉 Access:

```
http://localhost:8501
```

---

### 🔹 Use Prebuilt Image (Faster)

```bash
docker pull vaibhav526/customer-segmentation
docker run -p 8501:8501 vaibhav526/customer-segmentation
```

---

## 🤗 Hugging Face Deployment

👉 **Live Demo:**
https://huggingface.co/spaces/Vaibhavv09/CustomerSegmentation

---

## 📦 Project Structure

```
Customer_Segmentation/
│── segmentation.py
│── kmeans_model.pkl
│── scaler.pkl
│── requirements.txt
│── Dockerfile
│── README.md
```

---

## 💡 Business Insights

* Identify high-value customers (VIP, Premium)
* Target budget customers with discounts
* Improve retention strategies
* Optimize marketing campaigns

---

## 🚀 Why This Project Stands Out

* End-to-end ML pipeline
* Real-world business use case
* Interactive web application
* Docker containerization
* Cloud deployment (Hugging Face)

---

## 🔮 Future Improvements

* Add recommendation system
* Use advanced clustering algorithms
* Add analytics dashboard
* Integrate real-time data

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve this project.

---

## 📧 Contact

**Vaibhav**
GitHub: https://github.com/Vaibhavv526

---

## ⭐ If you found this useful, give it a star!
