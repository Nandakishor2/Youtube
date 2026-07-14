from pydantic import BaseModel


class IncidentCreate(BaseModel):
    title: str
    service: str
    severity: str
    blame_target: str
    developer_statement: str
    status: str
