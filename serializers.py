from rest_framework import serializers
class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    #variable = Attribute.type(of data store).
    due_date = serializers.CharField(required=False, allow_null=True)
    estimated_hours = serializers.FloatField()
    importance = serializers.IntegerField()
    dependencies = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
        )
    
