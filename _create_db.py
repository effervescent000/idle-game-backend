from app.db.db import engine
from app.db.schema import Base

try:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)
