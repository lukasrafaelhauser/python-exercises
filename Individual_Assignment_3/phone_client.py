# -*- coding: utf-8 -*-
#%%


import requests

def get_phonebook_client(): 
    request = requests.get('http://127.0.0.1:5000/home')
    
    return request.json()


def add_contact_client(number, name): 
    request = requests.post('http://127.0.0.1:5000/add-contact/{}/{}'.format(number, name))
    
    return request.json()


def get_phone_client(name): 
    request = requests.get('http://127.0.0.1:5000/get-phone/{}'.format(name))
    
    return request.json()


def delete_contact_client(name): 
    request = requests.delete('http://127.0.0.1:5000/delete-contact/{}'.format(name))
    
    return request.json()

def update_contact_client(name, number):
    request = requests.put('http://127.0.0.1:5000/update-contact/{}/{}'.format(name, number))
    
    return request.json()
    