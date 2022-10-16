#!/usr/bin/python3
"""Class review"""

from models.base_model import Basemodel


class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    """
    place_id = ''
    user_id = ''
    text = ''
