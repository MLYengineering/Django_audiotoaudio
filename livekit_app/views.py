from django.shortcuts import render
from livekit.plugins import openai
import os

# Create your views here.





from django.shortcuts import render
import uuid


from livekit import api
import os

# will automatically use the LIVEKIT_API_KEY and LIVEKIT_API_SECRET env vars
def room_view(request):
    """
    Renders the LiveKit Audio Room frontend and generates a token for joining.
    """
    room_name = "my-room"  # You can make this dynamic based on your application's logic

    # Generate a unique identity for the participant
    identity = f"user_{uuid.uuid4().hex[:8]}"

    # Generate the token
    token = api.AccessToken() \
        .with_identity(identity) \
        .with_name("Python Bot") \
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room_name,
        )).to_jwt()

    context = {
        "livekit_ws_url": os.getenv("LIVEKIT_WS_URL"),
        "token": token,
        "room_name": room_name,
    }
    return render(request, 'livekit_app/room.html', context)