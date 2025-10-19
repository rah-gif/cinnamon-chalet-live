# main/admin.py - Update the imports at the top
from django.contrib import admin
from .models import (
    AboutHeaderImage, EventsHeaderImage, AboutDescription, Leadership, Photo, History,
    RoomGallery, RoomType, SpecialOffer, Testimonial, HeaderImage, Event, RestaurantMenuItem,
    ContactInfo, ContactMessage,RoomHeaderImage,HomePageDescription,ContactHeaderImage # Add these
)

@admin.register(AboutHeaderImage)
class AboutHeaderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    
    def has_add_permission(self, request):
        # Allow adding only if no active header exists or we have less than 5
        active_count = AboutHeaderImage.objects.filter(is_active=True).count()
        total_count = AboutHeaderImage.objects.count()
        if active_count >= 1 and total_count >= 5:
            return False
        return True

@admin.register(RoomGallery)
class RoomGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'room_type', 'is_active', 'created_at']
    list_filter = ['is_active', 'room_type', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_per_night', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'room_type', 'discounted_price', 'is_active', 'valid_until']
    list_filter = ['is_active', 'valid_until']
    search_fields = ['title', 'description']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured']
    search_fields = ['customer_name', 'content']

# NEW ADMIN CLASSES
@admin.register(HeaderImage)
class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'subtitle']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'event_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'event_date'
    
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description', 'image', 'event_date')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(RestaurantMenuItem)
class RestaurantMenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']



##########for about




@admin.register(AboutDescription)
class AboutDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('About Section', {
            'fields': ('title', 'description', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'position']
    fieldsets = (
        ('Leadership Info', {
            'fields': ('name', 'position', 'quote', 'image')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'caption']
    fieldsets = (
        ('Photo Info', {
            'fields': ('title', 'image', 'caption')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['year', 'title']
    fieldsets = (
        ('History Event', {
            'fields': ('year', 'title', 'description')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(EventsHeaderImage)
class EventsHeaderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    
    def has_add_permission(self, request):
        # Allow adding only if no active header exists or we have less than 5
        active_count = EventsHeaderImage.objects.filter(is_active=True).count()
        total_count = EventsHeaderImage.objects.count()
        if active_count >= 1 and total_count >= 5:
            return False
        return True
    

#########  contact


# main/admin.py - Add these admin classes

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'is_active', 'updated_at']
    list_editable = ['is_active']
    
    def has_add_permission(self, request):
        # Allow only one contact info instance
        if self.model.objects.count() >= 1:
            return False
        return True

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']



##for about header image, 

# main/admin.py - Add this admin class

@admin.register(RoomHeaderImage)
class RoomHeaderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'subtitle']
    
    def has_add_permission(self, request):
        # Allow adding multiple headers but show warning if many exist
        return True
    


##home header description


# main/admin.py - Add this admin class

@admin.register(HomePageDescription)
class HomePageDescriptionAdmin(admin.ModelAdmin):
    list_display = ['meta_title', 'updated_at']
    readonly_fields = ['updated_at']
    
    fieldsets = (
        ('Welcome Section', {
            'fields': ('welcome_title', 'welcome_description', 'learn_more_text', 'learn_more_link')
        }),
        ('Photos Section', {
            'fields': ('photos_title', 'photos_description')
        }),
        ('Menu Section', {
            'fields': ('menu_title', 'menu_description')
        }),
        ('Testimonials Section', {
            'fields': ('testimonials_title',)
        }),
        ('Events Section', {
            'fields': ('events_title', 'events_description')
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Timestamps', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Allow only one home page description instance
        if HomePageDescription.objects.count() >= 1:
            return False
        return True
    



# for contactc header image

# Add this to your existing admin.py
@admin.register(ContactHeaderImage)
class ContactHeaderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active']
    search_fields = ['title', 'subtitle']


