query_es_create_films_documents = '''{"index": {"_index": "movies", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb3"}}
{"title": "Movie title: 16", "description": "Plot of movie 16", "creation_date": "2021-08-04", "rating": 9.0, "type": "movie", "genres": ["Genre_17", "Genre_3", "Genre_7"], "actors": ["Last name11 First name11", "Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24"], "writers": ["Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24", "Last name4 First name4"], "directors": ["Last name11 First name11", "Last name13 First name13", "Last name24 First name24", "Last name29 First name29", "Last name4 First name4"]}
{"index": {"_index": "movies", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb4"}}
{"title": "Movie title: 17", "description": "Plot of movie 17", "creation_date": "2021-08-04", "rating": 9.0, "type": "movie", "genres": ["Genre_17", "Genre_3", "Genre_7"], "actors": ["Last name11 First name11", "Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24"], "writers": ["Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24", "Last name4 First name4"], "directors": ["Last name11 First name11", "Last name13 First name13", "Last name24 First name24", "Last name29 First name29", "Last name4 First name4"]}
{"index": {"_index": "movies", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb5"}}
{"title": "Movie title: 18", "description": "Plot of movie 18", "creation_date": "2021-08-04", "rating": 9.0, "type": "movie", "genres": ["Genre_17", "Genre_3", "Genre_7"], "actors": ["Last name11 First name11", "Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24"], "writers": ["Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24", "Last name4 First name4"], "directors": ["Last name11 First name11", "Last name13 First name13", "Last name24 First name24", "Last name29 First name29", "Last name4 First name4"]}
{"index": {"_index": "movies", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb6"}}
{"title": "Movie title: 19", "description": "Plot of movie 19", "creation_date": "2021-08-04", "rating": 9.0, "type": "movie", "genres": ["Genre_17", "Genre_3", "Genre_7"], "actors": ["Last name11 First name11", "Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24"], "writers": ["Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24", "Last name4 First name4"], "directors": ["Last name11 First name11", "Last name13 First name13", "Last name24 First name24", "Last name29 First name29", "Last name4 First name4"]}
{"index": {"_index": "movies", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb7"}}
{"title": "Movie title: 20", "description": "Plot of movie 120", "creation_date": "2021-08-04", "rating": 9.0, "type": "movie", "genres": ["Genre_17", "Genre_3", "Genre_7"], "actors": ["Last name11 First name11", "Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24"], "writers": ["Last name13 First name13", "Last name16 First name16", "Last name22 First name22", "Last name24 First name24", "Last name4 First name4"], "directors": ["Last name11 First name11", "Last name13 First name13", "Last name24 First name24", "Last name29 First name29", "Last name4 First name4"]}
'''

query_es_create_genres_documents = '''
{"index": {"_index": "genres", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb3"}}
{"name":"Genre 1"}
{"index": {"_index": "genres", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb4"}}
{"name":"Genre 2"}
{"index": {"_index": "genres", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb5"}}
{"name":"Genre 3"}
'''

query_es_create_persons_documents = '''
{"index": {"_index": "persons", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb3"}}
{"actor":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"],  "birth_date": "2021-08-05", "director":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "first_name": "First name4",  "last_name": "Last name4", "producer":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "screenwriter":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"]}
{"index": {"_index": "persons", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb4"}}
{"actor":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"],  "birth_date": "2021-08-05", "director":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "first_name": "First name5",  "last_name": "Last name5", "producer":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "screenwriter":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"]}
{"index": {"_index": "persons", "_id": "ead9b449-734b-4878-86f1-1e4c96a28bb5"}}
{"actor":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"],  "birth_date": "2021-08-05", "director":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "first_name": "First name6",  "last_name": "Last name6", "producer":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"], "screenwriter":["02365fab-bfdf-4f3b-8282-862d990ef293", "02365fab-bfdf-4f3b-8282-862d990ef294"]}
'''