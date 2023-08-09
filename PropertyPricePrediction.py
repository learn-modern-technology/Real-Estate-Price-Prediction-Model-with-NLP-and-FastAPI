from pydantic import BaseModel
from typing import Optional

class PropertyPricePrediction(BaseModel):
    Property_Type: Optional[int] = None
    Club_House: Optional[int] = None
    School_University_In_Township: Optional[int] = None
    Hospital_In_Township: Optional[int] = None
    Mall_In_Township: Optional[int] = None
    Park_Jogging_Track: Optional[int] = None
    Swimming_Pool: Optional[int] = None
    Gym: Optional[int] = None
    Property_Area_in_SqFt: Optional[float] = None
    Price_By_SubArea: Optional[float] = None
    Amenities_Score: Optional[int] = None
    Price_By_Amenities_Score: Optional[float] = None
    Noun_Counts: Optional[int] = None
    Verb_Counts: Optional[int] = None
    Adjective_Counts: Optional[int] = None
    boasts_elegant: Optional[int] = None
    elegant_towers: Optional[int] = None
    every_day: Optional[int] = None
    great_community: Optional[int] = None
    mantra_gold: Optional[int] = None
    offering_bedroom: Optional[int] = None
    quality_specification: Optional[int] = None
    stories_offering: Optional[int] = None
    towers_stories: Optional[int] = None
    world_class: Optional[int] = None    