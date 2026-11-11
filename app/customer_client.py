
import os
import requests
from fastapi import HTTPException

CUSTOMER_SERVICE_URL = os.getenv(
    "CUSTOMER_SERVICE_URL",
    "http://localhost:8001"
)


def validate_customer(customer_id: int):
    try:
        response = requests.get(
            f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}",
            timeout=5
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Customer does not exist"
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=503,
                detail="Customer validation unavailable"
            )

        return response.json()

    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Customer Service is unavailable"
        )
