from rest_framework import serializers

from administration.models import PaymentModel as mod_payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = mod_payment.Payment
        fields = (
            'user',
            'payment_amount',
            'package',
            'created_at',
            'status',
        )