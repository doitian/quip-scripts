import os
import requests


def get_thread(id):
    # Get Threads
    # GET https://platform.quip.com/1/threads/{id}
    response = requests.get(
        url="https://platform.quip.com/1/threads/{id}".format(id=id),
        headers={
            "Authorization": "Bearer {token}".format(token=os.environ['QUIP_TOKEN']),
        },
    )

    return response.json()


def get_recent_messages(id, limit=1000000):
    response = requests.get(
        url="https://platform.quip.com/1/messages/{id}".format(id=id),
        headers={
            "Authorization": "Bearer {token}".format(token=os.environ['QUIP_TOKEN']),
        },
        params={
            "count": str(limit),
        },
    )

    return response.json()
