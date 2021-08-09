import aiohttp
import pytest
import json

from elasticsearch import AsyncElasticsearch

from ..settings import BODY_STRING, HTTPResponse, SERVICE_URL, TestSettings


@pytest.fixture(scope='session')
async def es_client():
    client = AsyncElasticsearch(hosts=TestSettings.es_host)
    yield client
    await client.close()


@pytest.fixture(scope='session')
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture
def make_get_request(session):
    async def inner(method: str, params: dict = None) -> HTTPResponse:
        params = params or {}
        url = SERVICE_URL + '/api/v1' + method  # в боевых системах старайтесь так не делать!
        async with session.get(url, params=params) as response:
          return HTTPResponse(
            body=await response.json(),
            headers=response.headers,
            status=response.status,
          )
    return inner


@pytest.mark.asyncio
async def test_search_detailed(es_client, make_get_request):
    # Заполнение данных для теста
    await es_client.bulk(body=json.dumps(BODY_STRING))

    # Выполнение запроса
    response = await make_get_request('/films/fc258fa6-886f-4997-a498-556a8f208ac2')

    # Проверка результата
    assert response.status == 200
    assert response.body['id'] == 'fc258fa6-886f-4997-a498-556a8f208ac2'

    response = await make_get_request('/films')

    # Проверка результата
    assert response.status == 200
    assert response.body['total'] == 95
