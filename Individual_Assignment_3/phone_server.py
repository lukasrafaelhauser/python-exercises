# -*- coding: utf-8 -*-

#%%

from flask import Flask, jsonify


server = Flask("Phonebook")

phonebook = {"ringo": "11001101100",
             "john": "229933992299",
             "paul": "99664477",
             "george": "100000000",
             "pepe": "123456789"}


@server.route("/home")
def get_phonebook():
    return jsonify(phonebook)

    
@server.route("/add-contact/<number>/<name>", methods=["POST"])
def add_contact(number, name): 
    

    if name not in phonebook: 
        phonebook.update({name:number})
        return jsonify (name + " : " + number + " was added to your phonebook")
    
    else: 
        return jsonify("name already exists in phonebook")


@server.route("/get-phone/<name>")
def get_number(name): 
    
    if name in phonebook: 
        return jsonify(name + ": " + phonebook[name])
    
    else: 
        return jsonify("Can't find that name in your phonebook")


@server.route("/delete-contact/<name>", methods=["DELETE"])
def delete_contact(name):   
    if name not in phonebook: 
        
        return jsonify("Can't find that name in your phonebook")
    else:
        del phonebook[name]
        
        return jsonify(name + " is OUT!")         


                  
@server.route("/update-contact/<name>/<number>", methods=["PUT"])
def update_contact(name, number): 
    
    if name not in phonebook: 
        return jsonify("Can't find that name in your phonebook")
    
    else: 
        phonebook[name] = number
        return jsonify(name + " has been updated to: " + number)
    
        
    
server.run()

#%%

