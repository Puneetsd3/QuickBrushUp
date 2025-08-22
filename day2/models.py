from dataclasses import dataclass, asdict
from db_config import get_conn

@dataclass
class User:
    id: int = None
    username: str = None
    
@dataclass
class Post:
    id: int = None
    user_id: int = None
    content: str = None
    

class UserDAO:
    @staticmethod
    def create(username):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        uid = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return User(id=uid, username=username)
    
    @staticmethod
    def fetch(user_id):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM users WHERE id=%s",(user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return User(*row)
        return None
    
    @staticmethod
    def list():
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM users")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [User(*row) for row in rows]
    
class PostDAO:
    @staticmethod
    def create(user_id, content):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (user_id, content) VALUES (%s, %s) RETURNING id", (user_id, content))
        pid = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return Post(id=pid, user_id=user_id, content=content)
    
    @staticmethod
    def fetch(post_id):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, user_id, content FROM posts WHERE id = %s", (post_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Post(*row)
        return None
    
    @staticmethod
    def list():
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, user_id, content FROM posts")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Post(*row) for row in rows]

