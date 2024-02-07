# utils.py

from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_token(user):
    # Generate a refresh token and access token for the given user
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),                    # Convert tokens to strings
        'access': str(refresh.access_token),
    }
