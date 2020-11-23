import requests

response = requests.get("https://barnamenevisan.info/api/courses/getactiveCourses")

# print(response) # output => <Response [200]>
# data = response.text
# jsonDate = response.json()
# print(jsonDate)

# for course in jsonDate:
#     print(f"{course['title']}\n{course['teacher']}")

jsonData = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 1})

print(jsonData.json())

