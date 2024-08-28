from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        actor_name = self.request.query_params.get('actor')
        director_name = self.request.query_params.get('director')
        
        if actor_name:
            queryset = queryset.filter(actors__name__icontains=actor_name)
        if director_name:
            queryset = queryset.filter(directors__name__icontains=director_name)
        
        return queryset

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=False, methods=['post'])
    def delete_if_not_associated(self, request):
        actor_id = request.data.get('id')
        try:
            actor = Actor.objects.get(id=actor_id)
        except Actor.DoesNotExist:
            return Response({'error': 'Actor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if not actor.movies.exists():
            actor.delete()
            return Response({'message': 'Actor deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Actor is associated with movies and cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
