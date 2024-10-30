from app.models.tasks import *
from app.backend.db import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='users', cascade='save-update, merge, delete')



# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(Task.__table__))
