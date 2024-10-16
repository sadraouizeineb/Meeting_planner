from .models import Room,Meeting  
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Meeting
from django.urls import reverse


from .forms import MeetingForm

# def room_list_view(request):
    # Récupérer toutes les instances de Room
    # rooms = Room.objects.all()
    
    # Passer les rooms au template
    # return render(request, 'room_list.html', {'rooms': rooms})
    

# def meetings_list_view(request):
#     meetings = Meeting.objects.all()  # Récupère toutes les réunions
#     return render(request, 'meetings.html', {'meetings': meetings})
def meetings_list_view(request):
    meetings = Meeting.objects.all()  # Get all meetings
    # rooms = Room.objects.all()  # Get all rooms
    #should add ('rooms': rooms)
    return render(request, 'meetings.html', {'meetings': meetings, })
    
# def detail(request, id):
#   meeting = Meeting.objects.get(pk=id)
#   return render(request, "details.html", {"meeting": meeting})
def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Correct model name and function
    return render(request, "details.html", {"meeting": meeting})




def room_detail(request, id):
    room = get_object_or_404(Room, id=id)  # Get the room by ID
    return render(request, "rooms.html", {"room": room})  # Render the room detail template


def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Get the meeting by ID
    if request.method == "POST":
        meeting.delete()  # Delete the meeting
        return redirect('meetings_list_view')  # Redirect to the meetings list view after deletion
    return render(request, 'confirm_delete.html', {'meeting': meeting})  # Render confirmation page
 
def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('meetings_list_view')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'new.html', {'form': form})

def update_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Récupérer la réunion par ID

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)  # Passer l'instance à mettre à jour
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('meetings_list_view')  # Rediriger vers la liste des réunions
    else:
        form = MeetingForm(instance=meeting)  # Remplir le formulaire avec les données existantes

    return render(request, 'update_meeting.html', {'form': form})  # Rendre le template