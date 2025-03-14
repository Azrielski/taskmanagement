from models import Session, engine, User, Task
from sqlalchemy.orm import sessionmaker

# Set up the session factory
Session = sessionmaker(bind=engine)

# Create a new user
def create_user(name):
    session = Session()
    if session.query(User).filter_by(name=name).first():
        print("User already exists")
        session.close()
        return
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    print(f"User '{name}' created successfully!")

# Get all users
def get_all_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    
    return [f"ID: {user.id}, Name: {user.name}" for user in users] 

# Find a user by name
def find_user_by_name(name):
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    session.close()
    return user

# Delete a user
def delete_user(name):
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{name}' deleted successfully.")
    else:
        print("User not found.")
    session.close()

# Create a new task
def create_task(description, user_name, status="Pending"):
    session = Session()
    user = session.query(User).filter_by(name=user_name).first()
    
    if not user:
        print("User not found. Task cannot be created.")
        session.close()
        return  # Stop execution if user does not exist
    
    task = Task(description=description, status=status, user_id=user.id)
    session.add(task)
    session.commit()
    print(f"Task '{description}' created successfully for user '{user_name}'.")
    session.close()

# Get all tasks (formatted output)
def get_all_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()

    if not tasks:
        return "No tasks found."
    
    return [f"ID: {task.id}, Desc: {task.description}, Status: {task.status}, User ID: {task.user_id}" for task in tasks]

# Find a task by ID
def find_task_by_id(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    session.close()
    return task

# Update a task's status
def update_task(task_id, status):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.status = status
        session.commit()
        print(f"Task {task_id} updated to '{status}'.")
    else:
        print("Task not found.")
    session.close()

# Delete a task
def delete_task(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task {task_id} deleted successfully.")
    else:
        print("Task not found.")
    session.close()
