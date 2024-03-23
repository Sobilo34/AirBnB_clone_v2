from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Set-up the DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.environ['HBNB_MYSQL_USER'],
                                              os.environ['HBNB_MYSQL_PWD'],
                                              os.environ['HBNB_MYSQL_HOST'],
                                              os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            objects = []
            for cls in classes:
                objects.extend(self.__session.query(cls).all())
        else:
            objects = self.__session.query(cls).all()
        return {"{}.{}".format(type(
            obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the created database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)
