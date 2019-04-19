# Google API (Token Generation)
Api para gerar refresh_token e access_token para o app do Android, OGlobo e GloboMais.
## Fluxo de Token (FLUXO DO GOOGLE)
Para realizar o fluxo de login do app no Android são necessários alguns requests para o Google.
### ACCESS_TOKEN e REFRESH_TOKEN
Esse fluxo retorna o access_token e refresh_token do google
ENDPOINT_GOOGLE: `https://www.googleapis.com/oauth2/v4/token?approval_prompt=force&access_type=offline`
```
    REQUEST TYPE: application/x-www-form-urlencoded
    
    DATA:
        client_id: <CLIENT_ID_APP>
        client_secret: <CLIENT_SECRET_APP>
        code: <AUTHORIZATION_CODE_APP>
        redirect_uri: <REDIRECT_URI_APP>
        grant_type: authorization_code
        access_type: offline
```
Todos os valores entre `<>` são valores recebidos diretamente de um request do APP OGlobo e GloboMais.
RESPONSE (STATUS_CODE - 200) EX:
```
{
    "access_token": "ya29.GlvwBmMqaAlVm7r0YVwbX_a7z2LIpSEiE4DiQSWcMGzDfyObclRO98mHJOG1hSputYrAhd9fvHZUr0tRBqMpAjK9cqKMnYETGK6631pVhPWAngc7D5E3z3KVLmS_",
    "expires_in": 3600,
    "refresh_token": "1/5_vQXaK9bdOYe2oN5yUtIPBWVoFnJqxTLCskAj4G9M4",
    "scope": "https://www.googleapis.com/auth/userinfo.email openid https://www.googleapis.com/auth/userinfo.profile",
    "token_type": "Bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM3ODJkM2YwYmM4OTAwOGQ5ZDJjMDE3MzBmNzY1Y2ZiMTlkM2I3MGUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI2NDU0MDc5NDU4MzItOGtzY25jbmwyM25qZ3I5MTJoMTNocDhpNjRucGpubmYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI2NDU0MDc5NDU4MzItOGtzY25jbmwyM25qZ3I5MTJoMTNocDhpNjRucGpubmYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTM2NzM2MTI3OTI0NzcyNTI2NDciLCJlbWFpbCI6InRlc3RlLnN3Zy5naWdlazNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJhb2laVnlweXdOMVlpTm5oaFFja0tBIiwibmFtZSI6IlRlc3RlIFRlc3RlIiwicGljdHVyZSI6Imh0dHBzOi8vbGg0Lmdvb2dsZXVzZXJjb250ZW50LmNvbS8tdjdISUllT2NpcmcvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQUNIaTNyZkp0ZS1DMm1PeGZXUmdoR2VJUDljbDE1cnF3QS9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiVGVzdGUiLCJmYW1pbHlfbmFtZSI6IlRlc3RlIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE1NTU2NDE5NzQsImV4cCI6MTU1NTY0NTU3NH0.eEXN4crqpyTR3sSsRo_Fy4f0kpYPGsHuKEW03O4qZol0y10gaW8sLk4QpFjf2uzpCb9wORXVk3nQgNBzYEkPTT4xyJD5M5E7mSLrTGsfvQYgH4yyhspA9Kmk7UTRXsN3X5a9lGxcfAganeFFGjHhq1zVwNC1z0VAgsR-s6Lf50FtzAGa0PeBo58PPJbJrjCw9nTJMrojtVWcoOb0Jwb6N52WBJ7a-ItlEHXPUIG1jByBuUviEHRylkxwdLC-Afzs2vmywRHN1yI6_NjKJD1MaQvEqyyPNYVYCa0ZwqSGyVn6TUoicPAusb3oXZODtsVTDF1Hp2ep_9GlOaFuQSmGdQ"
}
```
### GERAR ACCESS_TOKEN COM REFRESH_TOKEN
Para gerar um novo access_token a partir de um refresh_token é necessário realizar um novo request com as seguintes caracteristicas.
ENDPOINT_GOOGLE: `https://www.googleapis.com/oauth2/v4/token`
```
    REQUEST TYPE: application/x-www-form-urlencoded
    
    DATA:
        grant_type: refresh_token
        refresh_token: <REFRESH_TOKEN>
        client_id: <CLIENT_ID_APP>
        client_secret: <CLIENT_SECRET_APP>
```
Todos os valores entre `<>` são valores recebidos diretamente de um request do APP OGlobo e GloboMais.
RESPONSE (STATUS_CODE - 200) EX:
```
{
    "access_token": "ya29.GlvwBmoCi9und61KpDet6Vm8IsFoZsbGOwdCv6gHL4du6us3LyVWl4li-sQcLAOPmQ9mN3AhznGimqg9h63jGiXJAoz_zPL_5sPMJ7GQH5kJn7r6ovc_nHnZ4lMl",
    "expires_in": 3600,
    "scope": "https://www.googleapis.com/auth/userinfo.email openid https://www.googleapis.com/auth/userinfo.profile",
    "token_type": "Bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM3ODJkM2YwYmM4OTAwOGQ5ZDJjMDE3MzBmNzY1Y2ZiMTlkM2I3MGUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI2NDU0MDc5NDU4MzItOGtzY25jbmwyM25qZ3I5MTJoMTNocDhpNjRucGpubmYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI2NDU0MDc5NDU4MzItOGtzY25jbmwyM25qZ3I5MTJoMTNocDhpNjRucGpubmYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTM2NzM2MTI3OTI0NzcyNTI2NDciLCJlbWFpbCI6InRlc3RlLnN3Zy5naWdlazNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJXTHJxVy0xa2RsMERZNHZmU2M2VEpRIiwiaWF0IjoxNTU1NjQxMTY4LCJleHAiOjE1NTU2NDQ3Njh9.T0mcYLdKJ9Q3ab91Sh80TBsPFhWaiJEvweEF2OAh0Lj58rlORzwe8PsJAAwLO5p00wU79U7MARDRW4lXfzYVvpqX19m5RXK_acGR_GgAONpr3_1GpHbVOXr7EWY_k3BS9KQBxi61R3sv9PHeRxal_SPSqezQAr7xNPnPZqjxWfKRU5D9t3pWrqa5VmOvC7N2KHG1JRSHTe6DlwlKjmDWrRJ2idZJW_sTN0HuBRR90PHccwTX866GCzxCO0a6NXprilDtNeTy11MtTPYumUMHy_TXTpBMQQArniSsgTCltBvtlCg-lhyOux1GNGKT050mwqZYYwOh4ZeGdLp75rMZ3g"
}
```