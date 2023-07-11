import os
from app.db.db import Session
from app.db.schema import User

with Session() as session:
    session.add(
        User(username="admin", role="admin", password=os.environ["ADMIN_PASSWORD"])
    )
    session.add(User(username="test_user", password=os.environ["USER_PASSWORD"]))
    session.commit()
