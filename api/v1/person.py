from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi_pagination import Page, add_pagination, paginate

from models import Person
from services.person import PersonService, get_person_service
from utils.url_misc import get_params

router = APIRouter()


# Внедряем PersonService с помощью Depends(get_person_service)
@router.get('/{person_id}', response_model=Person)
async def person_details(person_id: str, person_service: PersonService = Depends(get_person_service)) -> Person:
    """
    Предоставляет информацию о персоне по её id
    :param person_id:
    """
    person= await person_service.get_by_id(person_id)
    if not person:
        # Если жанр не найден, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='person not found')

    return person


@router.get('', response_model=Page[Person])
async def persons_list(request: Request, person_service: PersonService = Depends(get_person_service)) -> List[Person]:
    """
    Предоставляет информацию о всех персонах
    Параметры поиска:
    - from: int начиная с какого элемента начинаем показ выдачи
    - size: int количество элементов в выдаче
    - query: str поисковая строка
    """
    # Формируем из параметров запроса словарь.
    search_params = dict(request.query_params.multi_items())
    
    # Формируем перечень полей, в которых будет происхождитть поиск, с весами
    search_fields = {'last_name': 5, 'first_name': 3}
    persons = await person_service.get_all(search_params=search_params, search_fields=search_fields)
    return paginate(persons)


add_pagination(router)