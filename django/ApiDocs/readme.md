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
  * domain/community/board/{pk}

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
  * domain/community/posts/{pk}

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
retrieve
{
    "게시글": {
        "id": 1,
        "board_type": 1,
        "title": "test1",
        "creator": "admin",
        "content": "testtest1",
        "created_at": "2021-07-16T16:16:24.408786Z",
        "updated_at": "2021-07-19T15:56:05.379276Z"
    },
    "해당 유저 댓글": {
        "id": 13,
        "post": 1,
        "creator": "admin",
        "content": "test_1_comment",
        "parent": null,
        "childs": [
            {
                "id": 14,
                "creator": "admin",
                "content": "test1_comment_in_comment",
                "parent": 13,
                "childs": [],
                "created_at": "2021-07-19T16:00:57.836930Z",
                "updated_at": "2021-07-19T16:01:35.662624Z"
            },
            {
                "id": 15,
                "creator": "test",
                "content": "test1_comment_in_comment test2",
                "parent": 13,
                "childs": [],
                "created_at": "2021-07-19T16:02:03.059019Z",
                "updated_at": "2021-07-19T16:02:03.059111Z"
            }
        ],
        "created_at": "2021-07-19T16:00:30.581354Z",
        "updated_at": "2021-07-19T16:00:30.581426Z"
    },
    "해당게시글 전체 댓글": [
        {
            "id": 16,
            "post": 1,
            "creator": "test",
            "content": "Test_Comment",
            "parent": null,
            "childs": [],
            "created_at": "2021-07-19T16:02:23.215260Z",
            "updated_at": "2021-07-19T16:02:23.215319Z"
        },
        {
            "id": 13,
            "post": 1,
            "creator": "admin",
            "content": "test_1_comment",
            "parent": null,
            "childs": [
                {
                    "id": 14,
                    "creator": "admin",
                    "content": "test1_comment_in_comment",
                    "parent": 13,
                    "childs": [],
                    "created_at": "2021-07-19T16:00:57.836930Z",
                    "updated_at": "2021-07-19T16:01:35.662624Z"
                },
                {
                    "id": 15,
                    "creator": "test",
                    "content": "test1_comment_in_comment test2",
                    "parent": 13,
                    "childs": [],
                    "created_at": "2021-07-19T16:02:03.059019Z",
                    "updated_at": "2021-07-19T16:02:03.059111Z"
                }
            ],
            "created_at": "2021-07-19T16:00:30.581354Z",
            "updated_at": "2021-07-19T16:00:30.581426Z"
        }
    ]
}
 ```

* **Error Response:**

  * **Code:** 400 <br />

---

댓글 

* **URL**

  * domain/community/comments/
  * domain/community/comments/{pk}

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
