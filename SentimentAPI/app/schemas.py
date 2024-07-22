from pydantic import BaseModel, constr

class TextInput(BaseModel):
    """
    Schema for validating the text input.
    
    Attributes:
        text (str): The text to be analyzed. Must be between 1 and 500 characters long.
    """
    text: constr(min_length=1, max_length=500)