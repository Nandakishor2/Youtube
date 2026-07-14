from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Models.Incident import IncidentCreate
from Connection.MongoDB_Motor import db
incidentsRouterMotor = APIRouter(prefix="/motor",tags=["MOTOR"])

@incidentsRouterMotor.get("/{title}")
async def getIncidentsMotor(title:str):
    incidentDetails : dict = await db["Incidents"].find_one({"title" : title})
    incidentDetails.pop("_id")
    if incidentDetails != None:
        return JSONResponse(
            status_code=200,
            content={
                "message" : "Incident fetched successfully",
                "incidentDetails" : dict(incidentDetails)
            }
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "message" : "Incident not found"
            }
        )

@incidentsRouterMotor.post("/")
async def createIncidentMotor(incident:IncidentCreate):
    try:
        await db["Incidents"].insert_one(incident.dict())
        return JSONResponse(
            status_code=201,
            content={
                "message" : "Incident created successfully"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message" : "Some unknown error occoured."
            }
        )