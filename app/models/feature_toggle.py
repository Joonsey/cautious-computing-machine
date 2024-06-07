from sqlmodel import SQLModel, Field


class FeatureToggleBase(SQLModel):
    name: str
    on: bool


class FeatureToggle(FeatureToggleBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class FeatureToggleCreate(FeatureToggleBase):
    pass

