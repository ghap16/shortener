# Shortener
REST API to shorten a URL

This project is done with **Python 3.8** and the **FastAPI 0.75.0** framework.

It has two endpoints, one to create the shortcode and one to get the original url.

### Requeriments
- Docker
- docker-compose

### Run
```
$ docker-compose up
```

**Open swagger**
[http://localhost:8000/docs](http://localhost:8000/docs)

**Run tests**
```
$ docker-compose run shortener pytest
```

### Example

**Open Swagger**
[https://8zxck2mgei.execute-api.us-east-1.amazonaws.com/dev/docs](https://8zxck2mgei.execute-api.us-east-1.amazonaws.com/dev/docs)

**Open ReDoc**
[https://8zxck2mgei.execute-api.us-east-1.amazonaws.com/dev/redoc](https://8zxck2mgei.execute-api.us-east-1.amazonaws.com/dev/redoc)
