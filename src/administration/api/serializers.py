from rest_framework import serializers

from administration.models import PaymentModel as mod_payment


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod_payment.Package
        fields = (
            'name',
            'how_month',
            'price',
            'sale_price',
        )


class PaymentSerializer(serializers.Serializer):
    package = serializers.IntegerField()


class PaymentStatusSerializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
