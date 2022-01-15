from collections import defaultdict
from fastapi import FastAPI, Response, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



while True:

    try:
        conn =  psycopg2.connect(host = 'localhost', database = 'name-of-database', username = 'postgres', password = 'password-of-database', cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print('database connection was successfull')
    except Exception as error:
        print('connection to database failed')
        print("Error: ", error)
        time.sleep(2)


my_posts = [{"title":"title of post", "content":"content 1", "id": 1},{"title":"title of post 2", "content":"content 2", "id": 2}]



def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def index():
    return {"message": "hello World !"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}



@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING * """, (posts.title, posts.content, posts.published))
    new_post = cursor.fetchone()
    
    conn.commit()

    return {"data": new_post}



@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    return {"data": post}



@app.delete("/delete/post/{id}", )
def delete_post(id: int):
    cursor.execute("""DELETE * FROM posts WHERE id = %s RETURNING""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/update/post/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE ID = %s RETURNING * """,(posts.title, posts.content, posts.published, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    return {"data": updated_post}


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# @app.get("/")
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