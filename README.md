## Сервис YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Список категорий может быть расширен администратором.

- ✨Magic ✨Python

## Технологии

- Django rest_framework
- Django rest_framework_simplejwt
- Django django_filters
- Git

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/Margarita-pyth/api_yamdb/
cd api_yamdb
```


Cоздать и активировать виртуальное окружение:

```sh
python3 -m venv env
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```sh
python3 manage.py migrate
```

Запустить проект:

```sh
python3 manage.py runserver
```

После запуска сервера можно ознакомится с документацией по проекту, в которой описана основная логика приложения, документация доступна по ссылке: http://127.0.0.1:8000/redoc/

### Пользовательские роли
 - Аноним — может просматривать описания произведений, читать отзывы и комментарии.
 - Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
 - Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
 - Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
 - Суперюзер Django должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

### Алгоритм регистрации пользователей
 - Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/.
 - Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.
 - Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
 - В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.
 - После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт /api/v1/users/me/ и заполнить поля в своём профайле (описание полей — в документации по ссылке: http://127.0.0.1:8000/redoc/).
 
### Создание пользователя администратором
 - Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт api/v1/users/ (описание полей запроса для этого случая — в документации). 
 - - В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой email и username на эндпоинт /api/v1/auth/signup/ , в ответ ему должно прийти письмо с кодом подтверждения.
 - Далее пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен), как и при самостоятельной регистрации.

 ## | Ресурсы сервиса API YaMDb |
 
| AUTH | аутентификация] [/api/v1/auth/signup/] |
| USERS | [пользователи] [/api/v1/users/] |
| TITLES | [произведения] [/api/v1/titles/] |
| CATEGORIES | [категории произведений] [/api/v1/categories/] |
| GENRES | [жанры произведений] [/api/v1/genres/] |
| REVIEWS | [отзывы на произведения] [/api/v1/titles/{title_id}/reviews/] |
| COMMENTS | [комментарии к отзывам] [/api/v1/titles/{title_id}/reviews/{review_id}/comments/] |

## License
**Подготовлено командой разработчиков: 

evgenlit,
Aleksandr-Fedotov,
Margarita-pyth
**

___________________________________________________________________________________________

## YamDB Service

The YaMDb project collects user reviews of works. 
The works are divided into categories: "Books", "Films", "Music". 
The list of categories can be expanded by the administrator.

- ✨Magic ✨Python

## Technologies

- Django rest_framework
- Django rest_framework_simplejwt
- Django django_filters
- Git

## How to launch a project:

Clone the repository and go to it on the command line:
```sh
git clone https://github.com/Margarita-pyth/api_yamdb/
cd api_yamdb
```


Create and activate a virtual environment:

```sh
python3 -m venv env
source venv/Scripts/activate
```

Install dependencies from a file requirements.txt:

```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Perform migrations:

```sh
python3 manage.py migrate
```

Launch a project:

```sh
python3 manage.py runserver
```

After starting the server, you can get acquainted with the project documentation, which describes the main logic of the application, the documentation is available at the link: http://127.0.0.1:8000/redoc/

### User roles
 - Anonymous — can view descriptions of works, read reviews and comments.
 - Authenticated user (user) — can read everything, as well as Anonymous, can publish reviews and rate works (films / books / songs), can comment on reviews; can edit and delete their reviews and comments, edit their ratings of works. This role is assigned by default to each new user.
 - Moderator — the same rights as an Authenticated User, plus the right to delete and edit any reviews and comments.
 - Admin — full rights to manage all the content of the project. Can create and delete works, categories and genres. Can assign roles to users.
 - The Django superuser must always have administrator rights, a user with admin rights. Even if you change the user role of the superuser, it will not deprive him of administrator rights. A superuser is always an administrator, but an administrator is not necessarily a superuser.

### User registration algorithm
 - The user sends a POST request with the email and username parameters to the endpoint /api/v1/auth/signup/.
 -The YaMDB service sends an email with a confirmation code (confirmation_code) to the specified email address.
 - The user sends a POST request with the username and confirmation_code parameters to the endpoint /api/v1/auth/token/, in response to the request he receives a token (JWT token).
 - As a result, the user receives a token and can work with the project API by sending this token with each request.
 - After registering and receiving the token, the user can send a PATCH request to the endpoint /api/v1/users/me/ and fill in the fields in his profile (the description of the fields is in the documentation at the link: http://127.0.0.1:8000/redoc /).
 
### Creating a user by an administrator
 - The user can be created by an administrator — through the site's admin zone or through a POST request to a special api endpoint/v1/users/ (the description of the request fields for this case is in the documentation).
 - - At this point, the user does not need to send an email with a confirmation code.
After that, the user must independently send his email and username to the endpoint /api/v1/auth/signup/, in response he should receive an email with a confirmation code.
 - Next, the user sends a POST request with the username and confirmation_code parameters to the endpoint /api/v1/auth/token/, in response to the request, he receives a token (JWT token), as with self-registration.

 ## | Resources of the YaMDb API service |
 
| AUTH | authentication] [/api/v1/auth/signup/] |
| USERS | [users] [/api/v1/users/] |
| TITLES | [works] [/api/v1/titles/] |
| CATEGORIES | [categories of works] [/api/v1/categories/] |
| GENRES | [genres of works] [/api/v1/genres/] |
| REVIEWS | [reviews of works] [/api/v1/titles/{title_id}/reviews/] |
| COMMENTS | [comments on reviews] [/api/v1/titles/{title_id}/reviews/{review_id}/comments/] |

## License
**Prepared by the development team: 

evgenlit,
Aleksandr-Fedotov,
Margarita-pyth
**
