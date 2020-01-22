from django.urls import path
from scholarship.views import ScholarShipCreateListAPIView, AdminApproveScholarShip, SponsorListUpdateAPIView

urlpatterns = [
    path("scholarships/", ScholarShipCreateListAPIView.as_view(), name="scholarships"),
    path("scholarships/approve/<pk>/",
         AdminApproveScholarShip.as_view(), name="RUD-scholarship"),
    path("scholarships/sponsor/<pk>", SponsorListUpdateAPIView.as_view())
]
