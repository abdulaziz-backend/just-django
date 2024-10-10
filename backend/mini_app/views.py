from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Profile, Task, UserTask, Referral
from .serializers import ProfileSerializer, TaskSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get'])
    def user(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def friends(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        friends_count = Referral.objects.filter(referrer=request.user).count()
        referral_link = f"https://t.me/your_bot_username?start={profile.referral_code}"
        return Response({
            'friends_count': friends_count,
            'referral_link': referral_link
        })

    @action(detail=False, methods=['post'])
    def invite(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        profile.coins += 100
        profile.save()
        return Response({'message': 'Invitation sent successfully'})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        task = self.get_object()
        user_task, created = UserTask.objects.get_or_create(user=request.user, task=task)
        return Response({'message': 'Task started successfully'})

    @action(detail=True, methods=['post'])
    def claim(self, request, pk=None):
        task = self.get_object()
        user_task = get_object_or_404(UserTask, user=request.user, task=task)
        
        if user_task.last_completed and (timezone.now() - user_task.last_completed).seconds < task.cooldown:
            return Response({'message': 'Task is still in cooldown'}, status=status.HTTP_400_BAD_REQUEST)

        profile = get_object_or_404(Profile, user=request.user)
        profile.coins += task.prize
        profile.save()

        user_task.last_completed = timezone.now()
        user_task.save()

        return Response({'message': 'Task claimed successfully', 'coins': profile.coins})