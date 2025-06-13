from typing import List

from fastapi import APIRouter
from schemas import SorterSchema
from services.SorterService import SorterService
from services.Trainer.TrainerService import trainModel
from services.Trainer.RetrainService import retrainModel


api_sorter_router = APIRouter()

@api_sorter_router.post('/sorter/sort', response_model = SorterSchema.SortData, tags=["Sorting Api"])
async def sort_results(body : SorterSchema.SortData):
    sortingResponseList = SorterService.sort(body)
    return sortingResponseList

@api_sorter_router.get('/sorter/train' , response_model = str, tags=["Sorting Api"])
async def train_sorter():
    try:
        trainModel()
        return "Success"
    except Exception as e:
        print(e)
        return "Error"

@api_sorter_router.get('/sorter/retrain' , response_model = str, tags=["Sorting Api"])
async def retrain_sorter():
    try:
        retrainModel()
        return "Success"
    except Exception as e:
        print(e)
        return "Error"

@api_sorter_router.post('/sorter/model', response_model = SorterSchema.SortData, tags=["Sorting Api"])
async def sort_results_with_model(body : SorterSchema.SortData):
    sortingResponseList = SorterService.sortWithModel(body)
    return sortingResponseList