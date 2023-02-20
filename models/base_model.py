""" BASE MODEL CLASS """
import uuid
from datetime import datetime

class BaseModel:
    """" Class basemodel """
    
    
    def __init__(self, *args, **kwargs):
        """ init """
        if kwargs is not None or len(kwargs) > 0:
            self.id = kwargs.get("id", self.getID())
            self.created_at = kwargs.get("created_at",  self.getDate())
            self.updated_at = kwargs.get("updated_at",  self.getDate())
        elif len(args) < 1:
            self.id = self.getID()
            self.created_at = self.getDate()
            self.updated_at = self.getDate()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})]"
    
    def save(self):
        self.update_at = self.getDate()
    
    def to_dict(self):
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = str(new_dict["created_at"])
        new_dict["updated_at"] = str(new_dict["updated_at"])
        return new_dict
    
    @staticmethod
    def getDate():
        chaine = datetime.now().isoformat()
        return datetime.fromisoformat(chaine)
    @staticmethod
    def getID():
        return str(uuid.uuid4())