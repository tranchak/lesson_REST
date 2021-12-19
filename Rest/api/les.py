from datetime import datetime

from django.conf import settings
from rest_framework import serializers
settings.configure()

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

print(comment.email,comment.content,comment.created)

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serial=CommentSerializer(comment)
print(serial.data)
