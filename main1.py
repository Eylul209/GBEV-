import requests
from pprint import pprint
"""
requests: HTTP istekleri yapmak için kullanılan popüler bir Python kütüphanesidir. Bu kütüphane ile API'ye istek gönderebilir ve yanıtları alabilirsiniz.
pprint: JSON verilerini güzel bir şekilde (pretty print) yazdırmak için kullanılır. Büyük veri yapılarının okunabilir şekilde yazdırılmasını sağlar.
"""

# API endpoint
endpoint = 'https://jsonplaceholder.typicode.com/posts'

def create_post(title, body, user_id):
    data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    response = requests.post(endpoint, json=data)
    return response.json()

""" data sözlüğü ile postun başlık, içerik ve kullanıcı ID'si verilerini hazırlıyoruz.
requests.post() fonksiyonu ile POST isteği yapıyoruz. Bu istek ile yeni bir post oluşturuluyor. """

def get_post(post_id):
    response = requests.get(f'{endpoint}/{post_id}')
    return response.json()

""" f'{endpoint}/{post_id}' dinamik olarak belirli bir postu almak için kullanılır. """

def update_post(post_id, title=None, body=None):
    data = {}
    if title:
        data['title'] = title
    if body:
        data['body'] = body
    if not data:
        return {"error": "No data provided for update."}
    response = requests.put(f'{endpoint}/{post_id}', json=data)
    return response.json()

def delete_post(post_id):
    response = requests.delete(f'{endpoint}/{post_id}')
    return response.status_code == 200  # 200 OK dönerse başarılı

def list_posts():
    response = requests.get(endpoint)
    return response.json()

# Kullanım örnekleri
print("Create İşlemi")
new_post = create_post("Yeni Başlık", "Yeni içerik eklendi", 1)
pprint(new_post)

post_id = new_post['id']  # Yeni oluşturulan postun ID'si

print("Read İşlemi")
post = get_post(post_id)
pprint(post)

print("Update İşlemi")
updated_post = update_post(post_id, title="Güncellenmiş Başlık")
pprint(updated_post)

print("Silme İşlemi")
deleted = delete_post(post_id)
print(f"Post başarıyla silindi: {deleted}")

print("Listeleme İşlemi")
posts = list_posts()
pprint(posts)
