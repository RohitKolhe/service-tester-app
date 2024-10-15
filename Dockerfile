# Stage 1: Build React frontend
FROM node:16-alpine as frontend-build
WORKDIR /app

# Copy package.json and install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy the rest of the frontend source code
COPY frontend/ ./

# Build the React app
RUN npm run build

# Stage 2: Build Python backend
FROM python:3.10-slim as backend-build

# Install dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY backend/ ./

# Copy frontend build files to the backend directory
COPY --from=frontend-build /app/build ./frontend/build

# Expose the backend port
EXPOSE 8000

# Command to run the backend
CMD ["python", "main.py"]
