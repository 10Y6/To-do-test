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
        if not self.title:
            print("La tarea debe tener un titulo.")
        if not self.description:
            print("La tarea debe tener una descripcion.")
        
        hash = Hash(self.title)
        self.id = hash.string_to_hash()
        
        task = {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'done': self.done
        }
        return task
    
    def dict_to_json(self):
        lista = []
        
        with open(cache_route,'r') as file:
             lista = file.read(245768)
             lista = json.loads(lista)
        
        with open(cache_route,'w') as file:
            lista.append(self.create_task())
            file.write(json.dumps(lista))

    def json_to_dict(self):
        dictio = None
        with open(cache_route,'r') as file:
            dictio = json.loads(file.read())
        return dictio