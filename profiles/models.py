from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


NAIROBI = 'Nairobi'
MOMBASA = 'Mombasa'
KISUMU = 'Kisumu'
NAKURU = 'Nakuru'
ELDORET = 'Eldoret'
KIAMBU = 'Kiambu'
MERU = 'Meru'
KERICHO = 'Kericho'
NYERI = 'Nyeri'
EMBU = 'Embu'
KAKAMEGA = 'Kakamega'
BUNGOMA = 'Bungoma'
MACHAKOS = 'Machakos'
KILIFI = 'Kilifi'
MALINDI = 'Malindi'
LIMURU = 'Limuru'
NAIVASHA = 'Naivasha'
LAMU = 'Lamu'
THIKA = 'Thika'
VOI = 'Voi'
KAPSABET = 'Kapsabet'
KISII = 'Kisii'
HOMA_BAY = 'Homa Bay'
BUSIA = 'Busia'
GARISSA = 'Garissa'
MANDERA = 'Mandera'
MARSABIT = 'Marsabit'
ISIOLO = 'Isiolo'
WAJIR = 'Wajir'
TURKANA = 'Turkana'
SAMBURU = 'Samburu'
WEST_POKOT = 'West Pokot'
BARINGO = 'Baringo'
LAIKIPIA = 'Laikipia'
NYANDARUA = 'Nyandarua'
THARAKA_NITHI = 'Tharaka Nithi'
KITUI = 'Kitui'
TANA_RIVER = 'Tana River'
TAITA_TAVETA = 'Taita Taveta'
#WEST_POKOT
TRANS_NZOIA = 'Transnzoia'

COUNTIES = [
    (NAIROBI, 'Nairobi'),
    (MOMBASA, 'Mombasa'),
    (KISUMU, 'Kisumu'),
    (NAKURU, 'Nakuru'),
    (ELDORET, 'Eldoret'),
    (KIAMBU, 'Kiambu'),
    (MERU, 'Meru'),
    (KERICHO, 'Kericho'),
    (NYERI, 'Nyeri'),
    (EMBU, 'Embu'),
    (KAKAMEGA, 'Kakamega'),
    (BUNGOMA, 'Bungoma'),
    (MACHAKOS, 'Machakos'),
    (KILIFI, 'Kilifi'),
    (MALINDI, 'Malindi'),
    (LIMURU, 'Limuru'),
    (NAIVASHA, 'Naivasha'),
    (LAMU, 'Lamu'),
    (THIKA, 'Thika'),
    (VOI, 'Voi'),
    (KAPSABET, 'Kapsabet'),
    (KISII, 'Kisii'),
    (HOMA_BAY, 'Homa Bay'),
    (BUSIA, 'Busia'),
    (GARISSA, 'Garissa'),
    (MANDERA, 'Mandera'),
    (MARSABIT, 'Marsabit'),
    (ISIOLO, 'Isiolo'),
    (WAJIR, 'Wajir'),
    (TURKANA, 'Turkana'),
    (SAMBURU, 'Samburu'),
    (WEST_POKOT, 'West Pokot'),
    (BARINGO, 'Baringo'),
    (LAIKIPIA, 'Laikipia'),
    (NYANDARUA, 'Nyandarua'),
    (THARAKA_NITHI, 'Tharaka Nithi'),
    (KITUI, 'Kitui'),
    (TANA_RIVER, 'Tana River'),
    (TAITA_TAVETA, 'Taita Taveta'),
    (TRANS_NZOIA,'Trans nzoia'),
]


#Customer Account
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    contact information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True,
        choices=COUNTIES)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Choices for business type
BIZZ_TYPE_CHOICES = [
    ('WHOLE_SELLER', 'Whole Seller'),
    ('SUPPLIER', 'Supplier'),
    ('RETAILER', 'Retailer'),
    ('FARMER', 'Farmer'),
]

# Enhanced Seller Model
class Seller(models.Model):
    """Enhanced Database model for a seller (including farmers, suppliers, etc.)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    image = models.ImageField(upload_to='seller_images', blank=True)
    business_category = models.CharField(max_length=20, choices=BIZZ_TYPE_CHOICES, default='FARMER')
    phone_no = models.CharField(max_length=15, unique=True, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)  # Expanded for detailed location
    email = models.EmailField(unique=True)  # Added unique constraint
    date_joined = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False, null=True)
    premium_subscription_expiry = models.DateField(null=True, blank=True)  # To track premium validity
    business_description = models.TextField(blank=True)  # Brief description of their business
    verified = models.BooleanField(default=False)  # Whether the seller's account is verified
    average_rating = models.FloatField(default=0.0)  # Track average customer ratings
    total_reviews = models.IntegerField(default=0)  # Count of reviews received
    website = models.URLField(max_length=255, blank=True, null=True)  # Optional business website
    social_media_links = models.JSONField(blank=True, null=True)  # To store social media profiles (e.g., JSON: {"Facebook": "url", "Instagram": "url"})
    preferred_payment_methods = models.JSONField(blank=True, null=True)  # Preferred payment options (e.g., {"M-Pesa": True, "Visa": True})
    bank_account_details = models.JSONField(blank=True, null=True)  # For payouts (e.g., {"Bank Name": "", "Account No": ""})

    # Address details
    county = models.CharField(max_length=100, blank=True)  # Kenyan counties
    town = models.CharField(max_length=100, blank=True)

    # Additional fields for analytics or business growth
    total_products_sold = models.IntegerField(default=0)  # Track total products sold by the seller
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Total earnings from the platform

    def __str__(self):
        return f"{self.user.username} ({self.get_business_category_display()})"

    def update_rating(self, new_rating):
        """Update average rating when a new review is added."""
        total = self.average_rating * self.total_reviews
        total += new_rating
        self.total_reviews += 1
        self.average_rating = total / self.total_reviews
        self.save()

    def is_subscription_active(self):
        """Check if the premium subscription is active."""
        if self.premium_subscription_expiry:
            return self.premium_subscription_expiry >= timezone.now().date()
        return False

class General_Admin(models.Model):
    """This is the model for the General Site Administrator user for Verbose Overview Management"""

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Admin')
    Email = model.EmailField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()
