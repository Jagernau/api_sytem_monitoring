from dotenv import dotenv_values
import ast

env_dict = dotenv_values('.env')

LOGIN: dict = ast.literal_eval(str(env_dict["LOGIN"]))
PASSWORD: dict = ast.literal_eval(str(env_dict["PASSWORD"]))
DOMAI_NAME: dict = ast.literal_eval(str(env_dict["DOMAI_NAME"]))

DB_USER: str = str(env_dict["DB_USER"])
DB_PASSWORD: str = str(env_dict["DB_PASSWORD"])
DB_HOST: str = str(env_dict["DB_HOST"])
DB_NAME: str = str(env_dict["DB_NAME"])
