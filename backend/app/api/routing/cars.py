from typing import Dict
from typing import List
from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_cars() -> List[Dict[str, Union[str, float]]]:
    return [
        {"id": 1, "color": "red", "wheels": 4, "top_speed": 144.00},
        {"id": 2, "color": "blue", "wheels": 3, "top_speed": 72.00},
    ]
