from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

challenges = {
    "january": "Push ups daily — 20 reps",
    "february": "Read daily — 20 minutes",
    "march": "Walk daily — 30 minutes",
    "april": "Drink enough water daily — 2 liters",
    "may": "Meditate daily — 10 minutes",
    "june": "Learn something new daily — 20 minutes",
    "july": "Squats daily — 30 reps",
    "august": "No junk food — daily",
    "september": "Write daily — 10 minutes",
    "october": "Plank daily — 2 minutes",
    "november": "Sleep 8 hours daily",
    "december": None
}

def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenges_by_number(request, month: int):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Wrong Month Number")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month: str):
    try:
        challenge = challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge": challenge,
            "month": month
        })
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    