-임시- 
### Api
회원가입 \
```
POST domain/account/signup/
data: {
    eamil: (CharField), 
    username: (CharField), 
    password: (CharField)
Success: 201
Fail: 400
```

로그인 \
`POST domain/account/login/` \
`data: email(CharField), password(CharField)` \
`Success: 200` \
`Fail: 401`

로그아웃 \
`POST domain/account/logout/` \
`Success: 200` \
`Fail: 400` 

게시판 Type \
`게시판의 목적 분류`
`POST domain/community/board/` \
`data: type(CharField)` \
`Success: 201 ` \
`Fail: 400`