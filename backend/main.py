from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import test_postgres, test_redis, test_kafka
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve the React build folder
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

print("Starting the application...")

@app.get("/")
async def serve_index():
    return FileResponse('frontend/build/index.html')

class ServiceDetails(BaseModel):
    serviceType: str
    url: str
    username: str
    password: str
    ssl: bool

@app.post("/test-connection")
async def test_connection(details: ServiceDetails):
    try:
        if details.serviceType == "postgres":
            # Pass the SSL parameter to the PostgreSQL testing function
            result = test_postgres(details.url, details.username, details.password, details.ssl)
        elif details.serviceType == "redis":
            # Pass the SSL parameter to the Redis testing function
            result = test_redis(details.url, details.password, details.ssl)
        elif details.serviceType == "kafka":
            # Pass the SSL parameter to the Kafka testing function
            result = test_kafka(details.url, details.ssl)
        else:
            raise HTTPException(status_code=400, detail="Unsupported service type")
        
        return {"success": True, "message": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
