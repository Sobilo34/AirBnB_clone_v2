from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
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
        """Set up the DBStorage"""
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                          .format(os.environ['HBNB_MYSQL_USER'],
                                                  os.environ['HBNB_MYSQL_PWD'],
                                                  os.environ['HBNB_MYSQL_HOST'],
                                                  os.environ['HBNB_MYSQL_DB']),
                                          pool_pre_ping=True)
        except KeyError as e:
            print(f"Error: Environment variable {e} is not set.")
            return
        except OperationalError as e:
            print(f"Error: {e}")
            return

    def all(self, cls=None):
        """Query the current database session"""
        if not self.__session:
            print("Error: Session is not initialized.")
            return {}

        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            objects = []
            for cls in classes:
                objects.extend(self.__session.query(cls).all())
        else:
            objects = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        """Add the object to the current database session"""
        if not self.__session:
            print("Error: Session is not initialized.")
            return

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        if not self.__session:
            print("Error: Session is not initialized.")
            return

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if not self.__session:
            print("Error: Session is not initialized.")
            return

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the created database"""
        if not self.__engine:
            print("Error: Engine is not initialized.")
            return

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

