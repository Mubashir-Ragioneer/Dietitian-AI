from bson import ObjectId
from typing import Any, Dict

def convert_mongo_id_to_str(data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert MongoDB ObjectId to string in the dictionary."""
    if "_id" in data:
        data["id"] = str(data.pop("_id"))
    return data

def convert_str_to_object_id(id_str: str) -> ObjectId:
    """Convert string ID to MongoDB ObjectId."""
    try:
        return ObjectId(id_str)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {str(e)}")

def format_datetime(dt: Any) -> str:
    """Format datetime object to ISO format string."""
    if hasattr(dt, 'isoformat'):
        return dt.isoformat()
    return str(dt) 