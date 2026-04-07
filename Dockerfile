# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install streamlit pandas plotly matplotlib seaborn scikit-learn

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "segmentation.py", "--server.port=8501", "--server.address=0.0.0.0"]


