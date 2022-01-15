from passlib.context import CryptContex



pwd_context = CryptContex(schemas=['bcrypt'], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)