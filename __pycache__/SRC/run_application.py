import SRC.main as app
import uvicorn


try:
    uvicorn.run(app)
except Exception as error:
    print(f"Error: {error}")
    

