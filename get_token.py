# 토큰 발급 받기
import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type": "authorization_code",
    "client_id": "12d363076da48bee57318795823b1ea4",
    "redirect_uri": "https://localhost.com",
    "code": "Y9nj5Tkw3zY76OBSxs5CcBvGprlDOgQqBfScfqTElfCFt-7SAVCP7wlPQfs3O0aVidzuyAorDKYAAAGCGSVD1Q",
}

response = requests.post(url, data=data)

# 요청 실패
if response.status_code != 200:
    print("error! because ", response.json())
else:  # 요청 성공
    tokens = response.json()
    print(tokens)
