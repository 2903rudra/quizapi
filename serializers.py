from rest_framework import serializers
from .models import Quiz ,Question ,Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice 
        fields = ['id' , 'text' ,'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many = True ,read_only = True )
    
    class Meta:
        model = Question
        fields = ['id' , 'text' , 'choices']

class Quizserializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True ,read_only = True )

    class Meta:
        model = Quiz
        fields = ['id' ,'name' ,'questions' ,'start_date' ,'end_date' ,'status']
