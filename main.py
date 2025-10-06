from models import Task


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

task.dict_to_json()    
print(task.json_to_dict())