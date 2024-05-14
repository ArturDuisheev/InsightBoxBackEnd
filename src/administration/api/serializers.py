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
    # payment_amount = serializers.ReadOnlyField()
    # package = PackageSerializer(source='package.id', read_only=True)
    package = serializers.IntegerField()

    # class Meta:
    #     model = mod_payment.Payment
    #     fields = (
    #         'user',
    #         'payment_amount',
    #         'package',
    #         'created_at',
    #         'status',
    #     )
