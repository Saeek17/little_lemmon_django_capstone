from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
def home(request): return render(request, 'index.html')
class MenuListCreateView(generics.ListCreateAPIView):
    queryset=Menu.objects.all().order_by('id'); serializer_class=MenuSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all(); serializer_class=MenuSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
class BookingListCreateView(generics.ListCreateAPIView):
    queryset=Booking.objects.all().order_by('booking_date'); serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Booking.objects.all(); serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]
