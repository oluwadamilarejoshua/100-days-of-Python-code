import requests

url = "https://sephora.p.rapidapi.com/reviews/list"

querystring = {"ProductId":"P454378","Limit":"60","Offset":"0"}

headers = {
	"X-RapidAPI-Host": "sephora.p.rapidapi.com",
	"X-RapidAPI-Key": "eb3d580a21mshffeb13a56ebe386p10985fjsn777a1b1976bc"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)