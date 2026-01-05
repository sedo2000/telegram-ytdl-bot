import os

ADMIN_ID = int(os.getenv("ADMIN_ID"))

def is_admin(user_id):
    return user_id == ADMIN_ID
