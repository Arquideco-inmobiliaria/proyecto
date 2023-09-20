from werkzeug.security import check_password_hash

class User():
    def __init__(self, idUsuario, correo, password1) -> None:
        self.idUsuario = idUsuario
        self.correo = correo
        self.password1 = password1
        
        
        
    @classmethod
    def check_password(self, hashed_password, password1):
        return check_password_hash(hashed_password, password1)
    
    
