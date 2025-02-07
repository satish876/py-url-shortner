# 1️⃣ Use a lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy application code to container
COPY app ./app

# 5️⃣ Expose FastAPI port
EXPOSE 5001

# 6️⃣ Run FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]
