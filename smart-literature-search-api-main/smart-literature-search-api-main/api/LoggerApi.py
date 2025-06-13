from typing import List

from fastapi import APIRouter
from schemas import LoggerSchema
from services.LoggerService import LoggerService

api_logger_router = APIRouter()

@api_logger_router.post("/logger/log", response_model = LoggerSchema.LoggerResponse, tags=["Logger API"])
async def logger_log(body: LoggerSchema.Logs):
    loggerResponse = LoggerService.logTrainData(body)
    return loggerResponse
