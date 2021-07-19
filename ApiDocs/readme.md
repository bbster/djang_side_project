**Api Docs**
---

회원가입

* **URL**

  * domain/account/signup/

* **Method:**

   * `POST` 
   
* **Data Params**
```
  data: {
    "eamil": "admin@admin.com",
    "username": "admin",
    "password": "password" 
   }
```
* **Success Response:**

  * **Code:** 201 <br />
  * **Content:** `{ username }님 회원가입을 축하합니다.`
 
* **Error Response:**

  * **Code:** 400 <br />
  * **Content:** `{"msg": "serializer.is_valid error"}`
  
---

로그인 

* **URL**

  * domain/account/login/

* **Method:**

   * `POST` 
   
* **Data Params**
```
  data: {
    "email": "admin@admin.com",
    "password": "password"
   }
```

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `{
    "msg": "admin님 환영합니다.",
}`
 
* **Error Response:**

  * **Code:** 401 <br />
  * **Content:** `{
    "msg": "로그인 정보가 옳지 않습니다"
}`
---

로그아웃 

* **URL**

  * domain/account/logout/

* **Method:**

   * `POST` 
   
* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `{"msg": "로그아웃 되었습니다."}`
 
* **Error Response:**

  * **Code:** 400 <br />
  * **Content:** `{"msg": "로그인 되어 있지 않습니다."}`

---

게시판 Type 

* **URL**

  * domain/community/board/

* **Method:**

   * `GET`|`POST`|`PUT`|`DELETE`

* **Data Params**
```
  data: {
    "type": "notice",
   }
```

   
* **Success Response:**

  * **Code:** 201 <br />
  * **Content:** `{
        "id": 1,
        "type": "NOTICE"
    },`
 
* **Error Response:**

  * **Code:** 400 <br />

---

게시글 

* **URL**

  * domain/community/posts/

* **Method:**

   * `GET`|`POST`|`PUT`|`DELETE` 

* **Data Params**
```
  data: {
    "board_type": 1, 
    "title": "test_title",
    "creator": login_user, 
    "content": "test_content",
    "created_at": auto_now,
    "updated_at": auto_now,
   }
```

   
* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** 
 ```
  {
        "id": 1,
        "board_type": 1,
        "title": "test",
        "creator": "admin",
        "content": "test",
        "created_at": "2021-07-16T16:16:24.408786Z",
        "updated_at": "2021-07-16T16:16:24.408856Z"
    }
 ```

* **Error Response:**

  * **Code:** 400 <br />

---

댓글 

* **URL**

  * domain/community/comments/

* **Method:**

   * `GET`|`POST`|`PUT`|`DELETE` 

* **Data Params**
```
  data: {
    {
        "post": 1,
        "creator": "admin",
        "content": "testsetset",
        "parent": null,
        "childs": [
            {
                "id": 7,
                "post": 1,
                "creator": "admin",
                "content": "test",
                "parent": 6,
                "childs": [],
                "created_at": "2021-07-19T13:35:27.234398Z",
                "updated_at": "2021-07-19T13:35:27.234509Z"
            }
        ],
        "created_at": "2021-07-19T13:34:33.679162Z",
        "updated_at": "2021-07-19T13:34:33.679250Z"
    }
```

   
* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** 
 ```
    {
        "id": 6,
        "post": 1,
        "creator": "admin",
        "content": "testsetset",
        "parent": null,
        "childs": [
            {
                "id": 7,
                "post": 1,
                "creator": "admin",
                "content": "test",
                "parent": 6,
                "childs": [],
                "created_at": "2021-07-19T13:35:27.234398Z",
                "updated_at": "2021-07-19T13:35:27.234509Z"
            }
        ],
        "created_at": "2021-07-19T13:34:33.679162Z",
        "updated_at": "2021-07-19T13:34:33.679250Z"
    }
 ```

* **Error Response:**

  * **Code:** 400 <br />

---
