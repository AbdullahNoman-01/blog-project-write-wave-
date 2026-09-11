from django.shortcuts import get_object_or_404, render
from .models import Recommendation


def recommendation_detail(request, pk):
    recommendation = get_object_or_404(
        Recommendation,
        pk=pk,
        is_published=True
    )
    return render(
        request,
        "recommendations/recommendation_detail.html",
        {
            "recommendation": recommendation
        }
    )