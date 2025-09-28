from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from workouts.forms import ClientForm, WorkoutForm
from workouts.models import Client, Workout

# Index View - show client list or option to add a client
@login_required
def index_view(request):
    user_id = request.user.id
    clients = Client.objects.filter(trainer_id=user_id).order_by('last_name', 'first_name')
    context = {
        'clients': clients,
    }
    return render(request, 'workouts/index.html', context)

# Show all workouts for all clients trained by this trainer
@login_required
def all_workouts_view(request):
    user_id = request.user.id
    workouts = Workout.objects.filter(client__trainer_id=user_id).order_by('-date')
    context = {
        'workouts': workouts,
    }
    return render(request, 'workouts/all_workouts_list.html', context)

# Add a new client
@login_required
def new_client_view(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.trainer = request.user
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'workouts/new_client_form.html', context)

# Update a client
@login_required
def client_update_view(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'client': client,
        'form': form,
    }
    return render(request, 'workouts/client_update_form.html', context)

# Delete a client
@login_required
def delete_client_view(request, id):
    client = Client.objects.get(id=id)
    if request.method == "POST":
        client.delete()
        return redirect('index')
    context = {
        'client': client,
    }
    return render(request, 'workouts/delete_client_confirm.html', context)

# Workout list for a client
@login_required
def workout_list_by_client_view(request, id):
    client = get_object_or_404(Client, id=id)
    workouts = Workout.objects.filter(client=client).order_by('-date')
    context = {
        'client': client,
        'workouts': workouts,
    }
    return render(request, 'workouts/workout_list_by_client.html', context)

# Add a new workout
@login_required
def new_workout_view(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.client = client
            workout.save()
            return redirect('workout list by client', id=client.id)
    form = WorkoutForm()
    context = {
        'client': client,
        'form': form
    }
    return render(request, 'workouts/new_workout_form.html', context)

# Update a workout
@login_required
def workout_update_view(request, id):
    workout = get_object_or_404(Workout, id=id)
    client = workout.client
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout list by client', id=client.id)
    form = WorkoutForm(instance=workout)
    context = {
        'workout': workout,
        'client': client,
        'form': form,
    }
    return render(request, 'workouts/workout_update_form.html', context)

# Delete a workout
@login_required
def delete_workout_view(request, id):
    workout = get_object_or_404(Workout, id=id)
    client = workout.client
    if request.method == "POST":
        workout.delete()
        return redirect('workout list by client', id=client.id)
    context = {
        'workout': workout,
        'client': client,
    }
    return render(request, 'workouts/delete_workout_confirm.html', context)
