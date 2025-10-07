from models import Task
import json
import os.path as path
import os

to_do_route =  os.path.dirname(os.path.abspath(__file__))
cache_route = os.path.join(to_do_route,"cache.json")

task_title = ''
task_description = ''
task_id = ''
task_done = False

task = Task()
task.done = task_done

while True:
    if not task_title: 
        task_title = input("Como se llama la tarea.")
    else:
        task.title = task_title
        if task_description and task_title: break
    if not task_description:
        task_description = input("Diga una descripcion de la tarea.")
        task.description = task_description
    else:
        task.description = task_description
        if task_description and task_title: break
try :
    task.add_task()
    task.delete_task("#408000003672")
except json.decoder.JSONDecodeError:
    with open(cache_route,'w') as file:
        dictio = {}
        file.write(json.dumps(dictio))
    task.add_task()
    task.delete_task("#408000003672")