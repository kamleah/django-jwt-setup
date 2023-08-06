from drf_yasg import openapi

# Create Your Schema Here ....

LoginSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='example@gmail.com'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description="*********")
    }
)