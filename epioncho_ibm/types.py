from enum import Enum

from pydantic import BaseModel, conlist


class RandomConfig(BaseModel):
    gender_ratio: float = 0.5


worms_stages = 21

micro_stages = 21

WormsStageList = conlist(
    item_type=float, min_items=worms_stages, max_items=worms_stages
)

MicroStageList = conlist(
    item_type=float, min_items=micro_stages, max_items=micro_stages
)


class Sex(Enum):

    male = "male"

    female = "female"


class BlackflyLarvae(BaseModel):

    L1: int  # 4: L1

    L2: int  # 5: L2

    L3: int  # 6: L3


class Person(BaseModel):

    treated: bool  # 1: column used during treatment
    age: float  # 2: current age
    sex: Sex  # 3: sex

    blackfly: BlackflyLarvae

    mf: MicroStageList  # microfilariae stages (21)

    worms: WormsStageList  # Worm stages (21)

    mf_current_quantity: int

    exposure: float

    new_worm_rate: float

    @classmethod
    def generate_random(
        cls, random_config: RandomConfig
    ) -> "Person":  # Other params here

        raise NotImplementedError
