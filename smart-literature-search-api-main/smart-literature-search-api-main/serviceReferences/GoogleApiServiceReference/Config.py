from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BASE_URL: str = "https://www.googleapis.com/customsearch/v1"
    #muhammedalimutlu@gmail.com
    #API_KEY: str = "AIzaSyCU48QzS4-hvIR4OkFXmm6JrAadAWBSKik"
    #SEARCH_ENGINE_KEY: str = "8801f8ac817f1c33d"
    #rabiabykshn@gmail.com
    API_KEY: str = "AIzaSyAxbVXBIx2Y3pZkRpY_WJaY9KHzcx5xeHw"
    SEARCH_ENGINE_KEY: str = "2257fb9d5f720b582"

settings = Settings()