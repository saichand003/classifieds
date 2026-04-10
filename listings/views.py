from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListingForm
from .models import Listing


def _render_db_setup_page(request):
    return render(request, 'db_not_ready.html', status=503)


def listing_list(request):
    try:
        listings = Listing.objects.select_related('owner').all()
        return render(request, 'listings/listing_list.html', {'listings': listings})
    except OperationalError as exc:
        if 'no such table' in str(exc).lower():
            return _render_db_setup_page(request)
        raise


def listing_detail(request, pk):
    try:
        listing = get_object_or_404(Listing.objects.select_related('owner'), pk=pk)
        return render(request, 'listings/listing_detail.html', {'listing': listing})
    except OperationalError as exc:
        if 'no such table' in str(exc).lower():
            return _render_db_setup_page(request)
        raise


@login_required
def create_listing(request):
    try:
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
    except OperationalError as exc:
        if 'no such table' in str(exc).lower():
            return _render_db_setup_page(request)
        raise
