from fastapi import FastAPI
from Routes.Incidents_Motor import incidentsRouterMotor
from Routes.Incidents_Pymongo import incidentsRouterPymongo
import threading
app = FastAPI()


@app.get("/debug/threads")
async def debug_threads():
    return {
        "count": threading.active_count(),
        "threads": [
            thread.name
            for thread in threading.enumerate()
        ]
    }
app.include_router(incidentsRouterMotor)
app.include_router(incidentsRouterPymongo)
