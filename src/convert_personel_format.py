from typing import Dict, Any


def convert_one_user_format(user: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "full-name": f"{user['firstName']} {user['lastName']}",
        "email": user["emailAddress"],
        "status": "active" if user["isActive"] else "inactive",
    }


def convert_personel_format(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "user-list": [convert_one_user_format(user) for user in data["users"]],
        "count": data["totalCount"],
    }
