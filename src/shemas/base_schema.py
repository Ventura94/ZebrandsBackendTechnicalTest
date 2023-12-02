from datetime import datetime, date

from pydantic import ConfigDict, BaseModel


def convert_datetime_to_timestamp(dt: datetime) -> float:
    return dt.timestamp()


def convert_date_to_timestamp(d: date) -> float:
    return datetime.combine(d, datetime.min.time()).timestamp()


class BaseSchemas(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: convert_datetime_to_timestamp,
            date: convert_date_to_timestamp,
        },
    )
