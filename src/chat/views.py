import openai
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["POST"])
def chat_with_gpt(request):
    user_message = request.data.get("message", "")

    if not user_message:
        return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
            api_key=settings.OPENAI_API_KEY
        )
        return Response({"response": response["choices"][0]["message"]["content"]})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
