from pydantic import BaseModel, Field, validator, AnyUrl, EmailStr
from typing import Optional
from faker import Faker
import random
from datetime import datetime
from uuid import UUID, uuid4
from email_validator import validate_email
import time

fake = Faker()

MANDATORY = ["id", "timestamp", "email"]


class Event(BaseModel):
    """
    Event model.
    Absolute must-have in this program.
    Candidate can choose which fields should be added, this is just an example.
    Variety of types could be a nice way of showing the knowledge of pydantic, however lets KISS and not
    expect a new type per field, examplanation for that would be nice.
    """

    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.now)
    email: EmailStr = Field(default_factory=fake.email)
    first_name: Optional[str] = Field(default_factory=fake.first_name)
    last_name: Optional[str] = Field(default_factory=fake.last_name)
    source: Optional[AnyUrl] = Field(default_factory=fake.url)

    @validator("email")
    def email_validator(cls, email):
        """
        Validator example.
        The recruited person should be able to add some sort of validation/test to their program.
        Can be written for any value the model contains, not necessarily the email.
        But if they're writing email validator - please don't use regex (or do, I dare you).
        """
        email = validate_email(email).email


def generator(amount: int = 1, per_time: int = 0):
    """
    Generator function example.
    This can be reaaally made in many ways.

    What to look for while recuiting a candidate:
    - are they adding fields here or in the model
    - how are they storing the events
    - are they using async/sleep
    - how is the model being used
    - imho it would be cool to see the random amount of values generated - sometimes the event returns all values,
      sometimes just a few columns, only mandatory ones, etc
    """
    events = []

    for i in range(amount):
        to_remove = []
        for field in Event.schema()["properties"]:
            if field in MANDATORY:
                continue
            if random.getrandbits(1) == 1:
                to_remove.append(field)
        fields = {field: None for field in to_remove}
        event = Event(**fields)
        events.append(event)
        time.sleep(per_time)
    return events
