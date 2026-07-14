from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Models.Incident import IncidentCreate
from Connection.MongoDB_AsyncPymongo import db
incidentsRouterPymongo = APIRouter(prefix="/pymongo",tags=["PYMONGO"])

@incidentsRouterPymongo.get("/{title}")
async def getIncidentsPymongo(title:str):
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

@incidentsRouterPymongo.post("/")
async def createIncidentPymongo(incident:IncidentCreate):
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