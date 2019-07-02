import requests
import json

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE4ZjBkNTk1MGM2MGYyYzUyNmJjNWJmMTNlNWE3ZDY3ZjFkZDQzMjM0NTNmNDQyOTFlZjIyN2JhZTY0YWE1NjdmMjc3NjEwMzc0ZTQ0Y2UwIn0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6ImE4ZjBkNTk1MGM2MGYyYzUyNmJjNWJmMTNlNWE3ZDY3ZjFkZDQzMjM0NTNmNDQyOTFlZjIyN2JhZTY0YWE1NjdmMjc3NjEwMzc0ZTQ0Y2UwIiwiaWF0IjoxNTYyMDM5ODEzLCJuYmYiOjE1NjIwMzk4MTMsImV4cCI6MTU3NzU5MTgxMywic3ViIjoiMjc0ODYyNzc5OSIsInNjb3BlcyI6WyJyZWFkIl19.LD1k125zJA7QWD4Q5bvtLsV0Rqhw_W70b273jkFzE79qqU5V_kboxVyK70_mnAw1lLqAjm_QMPtGbpEEnbkiKro8ishTW71-Iu5Z1Cbs4gRMP7vw1pXRPAIUoOa_QM6KizSMiiZplY2E5fUneJ6ePADATzwR5snb-bSWXQchzgD0ZA7zcCG6upw8YCZeQZVBUHeaSZLBsFG5GBqdYTCpA6gKUIB5IZmtij6W7GLmaUBdeDqSdUzfWM6UzPc95dWKI6KoH_pOi-bHoJLCiOJyAycJwbX2eumdgwITUlGRXHg0GinEGRFzOS6xviftUlZMl0BgacEn0PrZ4dsTeUL2Xw',
}

params = (
    ('level', '3'),
)

res = requests.get('https://apiv2.twitcasting.tv/internships/2019/games', headers=headers, params=params)

data = res.json()

q = data["question"]

op = ["+", "-", "*", "/"]

ans = ""

def f () :
    for i in op:
        for j in op:
            for k in op:
                for l in op:
                    for m in op:
                        for n in op:
                            opr = (data["question"][:-4]).split("?")
                            s = ""
                            s += opr[0]
                            s += i
                            s += opr[1]
                            s += j
                            s += opr[2]
                            s += k
                            s += opr[3]
                            s += l
                            s += opr[4]
                            s += m
                            s += opr[5]
                            s += n
                            s += opr[6]
                            if float(eval(s)) == float(data["question"].split("=")[-1]):
                                ans = f"{i}{j}{k}{l}{m}{n}"
                                return ans, s

ans, s = f()
res = requests.post('https://apiv2.twitcasting.tv/internships/2019/games/'+data["id"], headers=headers, data='{"answer":"'+ans+'"}')

print(res.json())
