## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Simple temperature collector API 
	
## Technologies
Project is created with:
* fastapi version: 0.109.1
* fastapi-utils version: 0.2.1
* pydantic version: 1.10.14
* tortoise-orm: 0.20.0
	
## Setup
Create prod.env from sample.env, fill it in.
To run this project, use docker compose:

```
$ docker compose up --build -d
```

## Todo
* Change backend
* Aggregate query results by hour to avoid duplicates
* Write tests
