from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreationForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreationForm(data=request.POST)
        if form.is_valid():
            # form data is valid 
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Image added Successfully')
            # redirect to new created item detail
            return redirect(new_image.get_absolute_url())
        else:
            # Build form with data provided by the bookmarklet via GET
            form = ImageCreationForm(data=request.GET)
        return render(request,
                      'images/image/create.html',
                      {'section': 'images',
                       'form': form})