from dataclasses import dataclass


@dataclass
class Answer:
    value: dict


@dataclass
class Question:
    quest: int
