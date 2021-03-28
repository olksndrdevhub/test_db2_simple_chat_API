# Simple Chat, Public chat API


## How to test:  
go to `https://simple-chat-api-test-db2.herokuapp.com/swagger-ui/` to see online documentation or test API via Swagger UI

### Also for full testing this API you can use Postman or httpie.
<hr>

## To run local server:
1. Clone this repo,  
2. Activate your virtual environment,
3. Navigate in project folder.
4. In `settings.py` file set DEBUG to True(!),  
5. Create your database in Postgresql,
6. Set your Postgres DB credentials in DATABASE sections in `settings.py` file,  
7. Run `pip install -r local.txt`,
8. Run `python manage.py migrate`,
9. Run `python manage.py runserver`,
10. Open in your browser `localhost:8000` or `localhost:8000/swagger-ui`.
<hr>

## Endpoints for Heroku version:  

`https://simple-chat-api-test-db2.herokuapp.com/` - Index view of project. Return link to Index API view.
<hr>

`https://simple-chat-api-test-db2.herokuapp.com/api/v1/messages/list/` - List of Messages endpoint. Allow to get list of messages (GET method), like this:     

<pre>
{
  "count": 12,
  "next": null,
  "previous": "https://simple-chat-api-test-db2.herokuapp.com/api/v1/messages/list/",
  "results": [
    {
      "id": 11,
      "text": "string11",
      "author_email": "user@example.com",
      "created": "2021-03-28T15:50:47.859086Z",
      "updated": "2021-03-28T15:50:47.859146Z"
    },
    {
      "id": 12,
      "text": "string 12",
      "author_email": "user@example.com",
      "created": "2021-03-28T16:09:08.733248Z",
      "updated": "2021-03-28T16:09:08.733280Z"
    }
  ]
}
</pre>
This endpoint return paginated list of results, 10 messages per page. so it get non-required parammeter "page" with page number, fo example `https://simple-chat-api-test-db2.herokuapp.com/api/v1/messages/list/?page=2`.
<hr>

`https://simple-chat-api-test-db2.herokuapp.com/api/v1/messages/single/<id>/` - Endpoint for Message with `id=message id`. Here you can get, single message.  
Return selected message, for example:  
<pre>
{
  "id": 1,
  "text": "test message",
  "author_email": "test@mail.com",
  "created": "2021-03-28T14:44:21.217134Z",
  "updated": "2021-03-28T14:44:21.217170Z"
}
</pre>
<hr>

`https://simple-chat-api-test-db2.herokuapp.com/api/v1/messages/create/` - Create Message endpoint. Allow to create (POST method) new message.   

To create new EventType just send POST request to this endpoint with `text` and `author_email` in request body.  
For example:  
<pre>
{
  "text": "example text #2"
  "author_email": "user@example.com"
}
</pre>
This endpoint have some validations:  

`text` - must be not emply & not longer than 100 symbols,  
`author_email` - must be valid email address.  

This validations is set on database model scheme level, in `chat_api/models.py`
<hr>
