from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListingForm
from .models import Listing


def listing_list(request):
    listings = Listing.objects.select_related('owner').all()
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, pk):
    listing = get_object_or_404(Listing.objects.select_related('owner'), pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})
