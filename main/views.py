# main/views.py
from django.shortcuts import render, get_object_or_404, redirect  # Add redirect import
from django.db import OperationalError
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import (
    RoomGallery, RoomType, SpecialOffer, Testimonial, 
    HeaderImage, Event, RestaurantMenuItem,
    AboutDescription, Leadership, Photo, History, 
    AboutHeaderImage, EventsHeaderImage,
    ContactInfo,ContactMessage,RoomHeaderImage,HomePageDescription,ContactHeaderImage
)

# main/views.py - Update home function

from datetime import datetime, timedelta


def home(request):
    try:
        # Get active header image
        header_image = HeaderImage.objects.filter(is_active=True).first()
        
        # Get home page description
        home_content = HomePageDescription.objects.first()
        if not home_content:
            home_content = HomePageDescription.objects.create()
        
        # Get featured testimonials
        testimonials = Testimonial.objects.filter(is_featured=True)[:3]
        
        # Get gallery images for photos section
        room_gallery = RoomGallery.objects.filter(is_active=True)[:7]
        
        # Get events
        events = Event.objects.filter(is_active=True)[:3]
        
        # Get restaurant menu items by category
        mains = RestaurantMenuItem.objects.filter(category='mains', is_available=True)
        desserts = RestaurantMenuItem.objects.filter(category='desserts', is_available=True)
        drinks = RestaurantMenuItem.objects.filter(category='drinks', is_available=True)
        
    except OperationalError:
        header_image = None
        home_content = None
        testimonials = Testimonial.objects.none()
        room_gallery = RoomGallery.objects.none()
        events = Event.objects.none()
        mains = RestaurantMenuItem.objects.none()
        desserts = RestaurantMenuItem.objects.none()
        drinks = RestaurantMenuItem.objects.none()
    
    # Add dates for booking form
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    
    context = {
        'header_image': header_image,
        'home_content': home_content,
        'testimonials': testimonials,
        'room_gallery': room_gallery,
        'events': events,
        'mains': mains,
        'desserts': desserts,
        'drinks': drinks,
        'today': today.isoformat(),
        'tomorrow': tomorrow.isoformat(),
    }

    return render(request, 'main/index.html', context)

# main/views.py - Update the rooms function

def rooms(request):
    try:
        # Get active room header image
        room_header = RoomHeaderImage.objects.filter(is_active=True).first()
        
        # Get all rooms and gallery images
        all_rooms = RoomType.objects.filter(is_available=True)
        special_offers = SpecialOffer.objects.filter(is_active=True)
        room_gallery = RoomGallery.objects.filter(is_active=True)
    except OperationalError:
        # If tables don't exist yet, use empty querysets
        room_header = None
        all_rooms = RoomType.objects.none()
        special_offers = SpecialOffer.objects.none()
        room_gallery = RoomGallery.objects.none()
    
    context = {
        'room_header': room_header,  # Add this
        'rooms': all_rooms,
        'special_offers': special_offers,
        'room_gallery': room_gallery,
    }
    return render(request, 'main/rooms.html', context)

def blog_detail(request, slug):
    return render(request, 'main/blog_detail.html', {'slug': slug})

# main/views.py - Update the about function

def about(request):
    try:
        # Get active about header image
        about_header = AboutHeaderImage.objects.filter(is_active=True).first()
        
        # Get or create the about description - FIXED VERSION
        about_description = AboutDescription.objects.first()
        if not about_description:
            # Create default about description if none exists
            about_description = AboutDescription.objects.create(
                title='Welcome to Cinnamon Chalet',
                description='Experience luxury and comfort at Cinnamon Chalet, where we blend modern amenities with traditional hospitality to create unforgettable stays for our guests.'
            )
        
        # Get active leadership members
        leadership = Leadership.objects.filter(is_active=True).order_by('order')
        
        # Get active photos
        photos = Photo.objects.filter(is_active=True).order_by('order')
        
        # Get active history events
        history = History.objects.filter(is_active=True).order_by('order')
        
    except Exception as e:
        # Fallback if there's any error
        print(f"Error in about view: {e}")
        about_header = None
        about_description = {
            'title': 'Welcome to Cinnamon Chalet',
            'description': 'Experience luxury and comfort at Cinnamon Chalet, where we blend modern amenities with traditional hospitality to create unforgettable stays for our guests.'
        }
        leadership = []
        photos = []
        history = []
    
    context = {
        'about_header': about_header,
        'about_description': about_description,
        'leadership': leadership,
        'photos': photos,
        'history': history,
    }
    
    return render(request, 'main/about.html', context)

def events(request):
    try:
        # Get active events header image
        events_header = EventsHeaderImage.objects.filter(is_active=True).first()
        
        # Get all active events, ordered by date (newest first)
        events_list = Event.objects.filter(is_active=True).order_by('-event_date')
        
    except Exception as e:
        # Fallback if there's any error
        events_header = None
        events_list = Event.objects.none()
    
    context = {
        'events_header': events_header,
        'events': events_list,
    }
    return render(request, 'main/events.html', context)

# main/views.py - Update the contact function
# main/views.py - Update the contact function
# main/views.py - Update the contact function
def contact(request):
    try:
        # Get active contact header image
        contact_header = ContactHeaderImage.objects.filter(is_active=True).first()
    except:
        contact_header = None
        
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()
            
            # Send email notification to admin
            try:
                subject = f'New Contact Message from {contact_message.name} - Cinnamon Chalet'
                message = f'''
New contact form submission:

Name: {contact_message.name}
Email: {contact_message.email}
Phone: {contact_message.phone or 'Not provided'}

Message:
{contact_message.message}

Submitted: {contact_message.created_at.strftime("%Y-%m-%d %H:%M")}

---
This message was sent from the Cinnamon Chalet contact form.
                '''
                
                # Send to admin email
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
                
            except Exception as e:
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
            
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'contact_header': contact_header,  # Add this
        'contact_info': contact_info,
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'main/contact.html', context)

def reservation(request):
    return render(request, 'main/reservation.html')





