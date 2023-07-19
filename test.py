# user_data = (
#     ("JohnDoe", "dark", "profile1.jpg"),
#     ("JaneSmith", "light", "profile2.jpg"),
#     ("MikeJohnson", "dark", "profile3.jpg"),
#     ("SarahWilliams", "light", "profile4.jpg"),
#     ("DavidBrown", "dark", "profile5.jpg")
# )

# # Contoh definisi metode to_json() dalam kelas model User

# def to_json(username,theme,image):
#     return {
#         "username": username,
#         "theme": theme,
#         "image": image
#     }

# data = [to_json(user[0],user[1],user[2]) for user in user_data]

# print(data)

text = 'hello'
encode_string = bytes(text, 'ascii')
print(text)
print(encode_string)