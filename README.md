# Address Book Management
A simple API built with Django Rest Framework and MySQL that allows you to add, update, view and delete addresses. 

## Steps to Replicate
1. Clone the code in the repository with ```git clone https://github.com/vishnureddys/address-book-management``` and then ```cd address-book-management```.
2. In MySQL, create a database and accordingly change the username and password in the ```settings.py``` file. For instance, in my case I created a database with the name ```address_book_management```, username ```djangouser``` and password ```password```. 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'address_book_management',
        'USER': 'djangouser',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
3. Now enter ```python manage.py makemigrations``` and ```python manage.py migrate``` in the terminal to update the database. 
4. To start the server, run ```python manage.py runserver```. 
5. Go to Postman and accordingly access the API endpoints. 

## API Endpoints
1. Make a POST request to ```http://127.0.0.1:8000/address-api/create/``` with data in the JSON format to **add an address**. 
```json
{
    "name": "Tony Stark",
    "phone_no": "9538881114",
    "door_no" : "#189",
    "street" : "17th cross road",
    "locality" : "Wilson Garden",
    "city" : "Bangalore",
    "state" : "Karnataka",
    "pincode" : "560030"
}
```
2. Make a GET request to ```http://127.0.0.1:8000/address-api/detail/<id>/``` for a **detailed view of the address**, where ```id``` is the primary key of the address you would like to view. It would return a JSON response as shown below when a request is made to ```http://127.0.0.1:8000/address-api/detail/1/```. 
```json
{
    "id": 1,
    "name": "Vishnu S Reddy",
    "phone_no": "9742914197",
    "door_no": "#545/146A",
    "street": "22nd main road",
    "locality": "HSR Sector 1",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560102"
}
```
3. Make a PUT request to ```http://127.0.0.1:8000/address-api/update/<id>/``` to **update/change the address**. For example, when a request is made to ```http://127.0.0.1:8000/address-api/update/2/``` with a JSON, it will make changes to the address with the primary key mentioned in ```id```. You can verify the changes in MySQL shell or in the Django Shell. 
![Updated Database](https://i.imgur.com/PR6MQyG.png)
4. Make a DELETE request to ```http://127.0.0.1:8000/address-api/delete/<id>/``` to **delete the address** from the database. For example, when a request is made to ```http://127.0.0.1:8000/address-api/delete/2/```, it deletes the address with the primary key ```2```.
![MySQL Deletion](https://i.imgur.com/cc4MLQ6.png)
5. Make a GET request to ```http://127.0.0.1:8000/address-api/all-addresses/``` to **view all addresses** in the database. It returns a list of JSONs as shown below. 
```json
[
    {
        "id": 1,
        "name": "Vishnu S Reddy",
        "phone_no": "9742914197",
        "door_no": "#545/146A",
        "street": "22nd main road",
        "locality": "HSR Sector 1",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560102"
    },
    {
        "id": 2,
        "name": "Tony Stark",
        "phone_no": "9538881114",
        "door_no": "#189",
        "street": "17th cross road, 11th main road",
        "locality": "Wilson Garden",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560030"
    }
]
```
6. Make a GET request to ```http://127.0.0.1:8000/address-api/detail/phone/<phone number>/``` to get details based on the phone number of the user. 
7. Make a GET request to ```http://127.0.0.1:8000/address-api/all-addresses/pincode/<pincode>/``` to filter addresses based on pincode. For example, check out the below JSON returned for the request ```http://127.0.0.1:8000/address-api/all-addresses/pincode/560102/```.

```json
[
    {
        "id": 1,
        "name": "Vishnu S Reddy",
        "phone_no": "9742914197",
        "door_no": "#545/146A",
        "street": "22nd main road",
        "locality": "HSR Sector 1",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560102"
    },
    {
        "id": 4,
        "name": "Jerry Sienfelf",
        "phone_no": "9538884111",
        "door_no": "#1891",
        "street": "19th main road",
        "locality": "HSR Layout",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560102"
    }
]
```