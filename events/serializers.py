from rest_framework import serializers
from django.utils import timezone

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "start_datetime",
            "end_datetime",
            "max_attendants",
            "location",
            "organizer",
        ]

    def validate_start_datetime(self, value):
        today = timezone.now()

        if value <= today:
            raise serializers.ValidationError("start_datetime must be after today")

        return value

    def validate_end_datetime(self, value):
        today = timezone.now()

        if value <= today:
            raise serializers.ValidationError("end_datetime must be after today")

        return value

    def validate(self, data):
        data = super().validate(data)

        start_datetime = data.get("start_datetime")
        end_datetime = data.get("end_datetime")

        if end_datetime and start_datetime >= end_datetime:
            raise serializers.ValidationError(
                "end_datetime must be after start_datetime"
            )

        return data
