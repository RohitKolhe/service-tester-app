# Service Tester Application

This project is a **Service Tester** application that allows you to verify the connectivity of various services (PostgreSQL, Redis, Kafka) from a FastAPI backend, which serves a React frontend. The application is designed to be deployed in a Kubernetes cluster.

## Features

- Test connections to PostgreSQL, Redis, and Kafka services.
- Frontend built with React.
- Backend built with FastAPI.
- Serve static files from the React build.

## Project Structure
.
├── Dockerfile
├── README.md
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── services.py
├── frontend
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   └── src
│       ├── App.css
│       ├── App.js
│       ├── components
│       │   ├── ResultDisplay.js
│       │   └── ServiceForm.js
│       └── index.js
└── kubernetes-deployment.yml


## Prerequisites

- Docker
- Docker Compose (optional for local development)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/xxx/service-tester-app.git
cd service-tester-app
```

### 2. Build the Docker Image
```
docker build -t service-tester:latest .
```

### 3. Clone the Repository
```
docker run -p 8000:8000 service-tester:latest
```

### 4. Access the Application
Open your browser and navigate to:

```
http://localhost:8000
```

### 5. Test Connections
You can use the /test-connection endpoint to test the connection to your desired services. Make a POST request with the following JSON payload:

```
{
  "serviceType": "postgres",
  "url": "postgresql://user:password@hostname:port/dbname",
  "username": "your_username",
  "password": "your_password"
}
```
## Kubernetes Deployment

To deploy the application in a Kubernetes cluster, you will need to create the necessary Kubernetes resources. The Kubernetes manifests are provided in the `k8s` directory.

### Kubernetes Manifests

- **`deployment.yaml`**: Defines the deployment for the FastAPI application.
- **`service.yaml`**: Exposes the application.

```
kubectl apply -f kubernetes-deployment.yml
kubectl get svc
```
# 
![alt text](image.png)