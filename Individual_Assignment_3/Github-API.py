# -*- coding: utf-8 -*-

#%%

import requests
response = requests.get("https://api.github.com/users/lukasrafaelhauser/repos")

def github_repos():
    text = response.json()
    summary = []
    j = 0
    for i in text:
        summary.append( {} , )  
        summary[j].update(Name = text[j]["name"])
        summary[j].update({"Stars" : text[j]["stargazers_count"]})
        summary[j].update(Language = text[j]["language"])
        summary[j].update(URL = text[j]["url"])
        j += 1
    return summary

