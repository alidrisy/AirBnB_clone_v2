#!/usr/bin/python3
"""Create New engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Sqlalchemy engine to stored data"""

    __engine = None
    __session = None
    __classes = {}

    def __init__(self):
        """Inisialize data and getenv var"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == 'test':
            self.__engine.drop_all()

    def all(self, cls=None):
        """Query on the current database session"""
        dict1 = {}
        if cls is not None:
            if type(cls) is str:
                cls = self.__classes[cls]
            for clas in self.__session.query(cls).all():
                k = f'{clas.__class__.__name__}.{clas.id}'
                dict1[k] = clas
        else:
            for cl in self.__classes.values():
                for clas in self.__session.query(cl).all():
                    k = f'{clas.__class__.__name__}.{clas.id}'
                    dict1[k] = clas
        return dict1

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database, and create
        the current database session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity
        from models.base_model import Base
        self.__classes = {'State': State, 'City': City, 'User': User,
                          'Place': Place, 'Review': Review, 'Amenity': Amenity}
        Base.metadata.create_all(self.__engine)
        session_sco = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_sco)
        self.__session = Session()

    def close(self):
        """
        Call remove() method on the private session attribute (self.__session)
        """
        self.__session.close()
