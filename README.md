# Flicks Documentation

This demo utilizes:

* [Django](https://www.djangoproject.com/) (1.11)
* [Django Rest Framework](http://www.django-rest-framework.org/) (3.6.3)
* [Docker](https://www.docker.com/)
* [Alpine Linux](https://www.alpinelinux.org/)

## Django Admin

URL: http://{url}:{port}/

Username: admin
Password: 123qweasd

## API endpoints

URL: http://{url}:{port}/api/

### Registration

`POST /api/users/create`

args:

* field: username
* field: password

return:

* User OK: http 201 + Token
* User Exists: http 409 + Error msg
* Error: http 400 + Error msg

### Log in

`POST /api/users/login`

args:

* field: username
* field: password

return:

* Login OK: http 200 + Token
* Login BAD: http 401 + Error msg
* User not enabled: http 403 + Error msg

### Log out

`POST /api/users/logout`

args:

* auth token

return:

* http 202 + Friendly msg

### List Films

`GET /api/films`
`GET /api/films/{id}`
`GET /api/films/[?title={abc}&year={1234}]`

args:

*

return:

* http 200 + Data

### Create Film

`POST /api/films`

args:

* header: auth token
* field: title
* field: year

return:

* http 200 + Data

### Update Film

`PUT /api/films/{id}`

args:

* header: auth token
* field: title
* field: year

return:

* http 200 + Data

### Delete Film

`DELETE /api/films/{id}`

args:

* header: auth token

return:

* http 204

### List People

`GET /api/people`
`GET /api/people/{id}`
`GET /api/people/[?name={abc}&alias={def}]`

args:

*

return:

* http 200 + Data

### Create Person

`POST /api/people`

args:

* header: auth token
* field: first_name
* field: last_name
* field: alias (string array)
* field: as_actor (film id array)
* field: as_director (film id array)
* field: as_producer (film id array)

return:

* http 200 + Data

### Update Person

`PUT /api/people/{id}`

args:

* header: auth token
* field: first_name
* field: last_name
* field: alias (string array)
* field: as_actor (film id array)
* field: as_director (film id array)
* field: as_producer (film id array)

return:

* http 200 + Data

### Delete Person

`DELETE /api/people/{id}`

args:

* header: auth token

return:

* http 204
