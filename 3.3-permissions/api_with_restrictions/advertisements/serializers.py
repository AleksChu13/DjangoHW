from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "description",
            "creator",
            "status",
            "created_at",
        )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        # У объявления есть статусы: `OPEN`, `CLOSED`.
        # Необходимо валидировать, что у пользователя не больше 10 открытых объявлений
        open_adv_count = Advertisement.objects.filter(
            creator=self.context["request"].user, status=AdvertisementStatusChoices.OPEN
        ).count()
        if open_adv_count >= 10 and (
            self.context["request"].method == "POST"
            or self.context["request"].data.get("status") == "OPEN"
        ):
            raise ValidationError("Превышен лимит открытых объявлений (10)")

        return data