from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from pydantic import BaseSettings

from app import database



class Settings(BaseSettings):
    database_password: str = ""
    database_username: str = ""
    secret_key: str = ""

settings = Settings()

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)





















#--------------------------------------------previous code-------------------------------------------------------------
#def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
# 
# 

#  @app.get("/")
# def index():
#     return {"message": "hello World !"}


# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}



# @app.post("/createpost", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING * """, (posts.title, posts.content, posts.published))
#     new_post = cursor.fetchone()
    
#     conn.commit()

#     return {"data": new_post}



# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
#     return {"data": post}



# @app.delete("/delete/post/{id}", )
# def delete_post(id: int):
#     cursor.execute("""DELETE * FROM posts WHERE id = %s RETURNING""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/update/post/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE ID = %s RETURNING * """,(posts.title, posts.content, posts.published, str(id),))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
#     return {"data": updated_post}