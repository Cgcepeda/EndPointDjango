from rest_framework import serializers
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from .models import Reviews, PropertyTypes, States, Cities, Categories, Properties, Transaction

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id','feedback', 'rating','avatar')

class PropertyTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyTypes
        fields = ('id','slug')

class StatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = States
        fields = ('id','slug')

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('id','slug')

class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = ('id','slug','zip','state')

class PropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Properties
        fields = ('id','title','image','price','city','bath','beds','sqft','category')

class TranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')

class TransactionSerializer(serializers.ModelSerializer):
    transaction = TranSerializer(read_only=True)

    class Meta:
        model = Properties
        fields = ('transaction','propertietypes')

class TransactionResource(DjangoResource):
    preparer = FieldsPreparer(fields= {
        'properties_transaction': 'transaction.id',
        'properties_slug': 'transaction.slug',
        'properties_propertietypes': 'propertietypes.slug'
        #'properties_propertietypes': 'propertietypes'
    })

    def list(self):
        return Properties.objects.all()