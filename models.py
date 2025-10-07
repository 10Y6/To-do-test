from id_creator import Hash
import os.path as path
import os
import json

#json route
to_do_route =  os.path.dirname(os.path.abspath(__file__))
cache_route = os.path.join(to_do_route,"cache.json")


class Task():
    def __init__(self,id=None,title=None,description=None,done=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
    
    def create_task(self):
        #Create a task to be added to json cache
        
        hash = Hash(self.title)
        self.id = hash.string_to_hash()
        
        task = {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'done': self.done
        }
        return task

    def json_to_dict(self):
        #Convert from json cache to a dict
        dictio = None
        with open(cache_route,'r') as file:
            dictio = json.loads(file.read())
        return dictio
    
    def add_task(self):
        #Add a task to the json cache
        dictio = {}
        with open(cache_route,'r') as file:
                dictio = file.read()
                dictio = json.loads(dictio)
        
        with open(cache_route,'w') as file:
            dicti = {self.create_task()['id']:self.create_task()}
            dictio.update(dicti)
            file.write(json.dumps(dictio))
    
    def delete_task(self,ID):
        #delete a task from the json cache
        dictio = {}
        flag = False
        with open(cache_route,'r') as file:
            dictio = file.read()
            dictio = json.loads(dictio)
            if ID in dictio: flag = True #is task ID in file?
        
        if flag:
            with open(cache_route,'w') as file:
                del dictio[ID]
                file.write(json.dumps(dictio))
        