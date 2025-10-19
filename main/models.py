# main/models.py
from django.db import models

class RoomGallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    room_type = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Room Gallery"
        ordering = ['-created_at']

class RoomType(models.Model):
    ROOM_CATEGORIES = [
        ('single', 'Single Room'),
        ('family', 'Family Room'),
        ('presidential', 'Presidential Room'),
        ('deluxe', 'Deluxe Room'),
        ('suite', 'Suite'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=ROOM_CATEGORIES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')
    amenities = models.TextField(help_text="List amenities separated by commas")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price_per_night}/night"

class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/')
    is_active = models.BooleanField(default=True)
    valid_until = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.rating} stars"

# NEW MODELS FOR INDEX.HTML
class HeaderImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='header/')
    subtitle = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Header Images"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    event_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-event_date']

class RestaurantMenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('mains', 'Mains'),
        ('desserts', 'Desserts'),
        ('drinks', 'Drinks'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        verbose_name_plural = "Restaurant Menu Items"
        ordering = ['category', 'name']








#######for about

# About Page Models
class AboutDescription(models.Model):
    title = models.CharField(max_length=200, default="Welcome!")
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Description"
        verbose_name_plural = "About Description"
    
    def __str__(self):
        return "About Description"

class Leadership(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='leadership/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name_plural = "Leadership Team"
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    caption = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return self.title if self.title else f"Photo {self.id}"


class History(models.Model):
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name_plural = "History Events"
    
    def __str__(self):
        return f"{self.year} - {self.title}"
    

class AboutHeaderImage(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    image = models.ImageField(upload_to='about_headers/')
    subtitle = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Header Images"
        ordering = ['-created_at']



class EventsHeaderImage(models.Model):
    title = models.CharField(max_length=200, default="Events")
    image = models.ImageField(upload_to='events_headers/')
    subtitle = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Events Header Images"
        ordering = ['-created_at']






# main/models.py - Add these models

class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Contact Information"
    
    class Meta:
        verbose_name_plural = "Contact Information"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"




### for room header

# main/models.py - Add this model

class RoomHeaderImage(models.Model):
    title = models.CharField(max_length=200, default="Rooms Header")
    image = models.ImageField(upload_to='headers/')
    subtitle = models.CharField(max_length=300, blank=True, help_text="Optional subtitle text")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Room Header Images"
        ordering = ['-created_at']


### home header description


# main/models.py - Add this model

class HomePageDescription(models.Model):
    welcome_title = models.CharField(max_length=200, default="Welcome!")
    welcome_description = models.TextField(
        default="Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
    )
    photos_title = models.CharField(max_length=200, default="Photos")
    photos_description = models.TextField(
        default="Explore our beautiful hotel through these stunning photographs showcasing our facilities, rooms, and amenities."
    )
    menu_title = models.CharField(max_length=200, default="Our Unique Menu")
    menu_description = models.TextField(
        default="Experience culinary excellence with our diverse menu featuring the finest ingredients and innovative dishes prepared by our expert chefs."
    )
    testimonials_title = models.CharField(max_length=200, default="What Our Guests Say")
    events_title = models.CharField(max_length=200, default="Latest Events")
    events_description = models.TextField(
        default="Stay updated with our latest events and happenings. Join us for memorable experiences."
    )
    learn_more_text = models.CharField(max_length=100, default="Learn More")
    learn_more_link = models.URLField(blank=True, default="#")
    
    # SEO Fields
    meta_title = models.CharField(max_length=200, default="Cinnamon Chalet - Luxury Hotel & Resort")
    meta_description = models.TextField(
        default="Experience luxury accommodation at Cinnamon Chalet. Enjoy premium amenities, exquisite dining, and unforgettable stays in a serene environment."
    )
    meta_keywords = models.CharField(max_length=300, default="luxury hotel, resort, accommodation, dining, events")
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"
    
    def __str__(self):
        return "Home Page Description"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and HomePageDescription.objects.exists():
            # Update the existing instance instead of creating new one
            existing = HomePageDescription.objects.first()
            existing.welcome_title = self.welcome_title
            existing.welcome_description = self.welcome_description
            existing.photos_title = self.photos_title
            existing.photos_description = self.photos_description
            existing.menu_title = self.menu_title
            existing.menu_description = self.menu_description
            existing.testimonials_title = self.testimonials_title
            existing.events_title = self.events_title
            existing.events_description = self.events_description
            existing.learn_more_text = self.learn_more_text
            existing.learn_more_link = self.learn_more_link
            existing.meta_title = self.meta_title
            existing.meta_description = self.meta_description
            existing.meta_keywords = self.meta_keywords
            return existing.save(*args, **kwargs)
        return super().save(*args, **kwargs)
    




    ###for contact header image,

    
    
# Add this to your existing models.py

    
# Add this to your existing models.py
class ContactHeaderImage(models.Model):
    title = models.CharField(max_length=200, default="Contact Us")
    image = models.ImageField(upload_to='contact_headers/')
    subtitle = models.CharField(max_length=300, blank=True, help_text="Optional subtitle text")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Contact Header Images"
        ordering = ['-created_at']



