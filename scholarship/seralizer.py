from rest_framework import serializers
from scholarship.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    """ serializer for scholarships """
    class Meta:
        model = Scholarship
        # fields = "__all__"
        fields = ('birth_certificate', 'national_id',
                  'adress', 'phone', 'school_name', 'school_adress', 'academic_level', 'year_of_completion', 'is_approved')
        extra_kwargs = {'adress': {'required': True}}

    def update(self, instance, validated_data):
        """ update an existing scholarship """
        instance.is_approved = validated_data.get(
            'is_approved', instance.is_approved)

        instance.save()
        return instance
