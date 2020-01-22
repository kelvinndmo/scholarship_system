# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scholarship.seralizer import ScholarshipSerializer
from scholarship.models import Scholarship

from rest_framework import generics

from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework import status
from django.core.mail import send_mail
from utils.permissions import IsApplicant, IsSponsor, IsStaff, ReadOnly


class ScholarShipCreateListAPIView(generics.ListCreateAPIView):
    """ list and create scholarships """
    serializer_class = ScholarshipSerializer
    permission_classes = (IsApplicant | ReadOnly,)

    def get_queryset(self):

        user = self.request.user

        # if the user is an applictant, he/she can only see her own application
        if user.role == 'AP':
            return Scholarship.active_objects.for_applicant(applicant=user)

        return Scholarship.objects.all()

    def post(self, request, *args, **kwargs):

        user = request.user
        scholarship = request.data

        serializer = self.serializer_class(data=scholarship)
        serializer.is_valid(raise_exception=True)

        serializer.save(applicant=user)

        response = {
            "data": serializer.data,
            "message": "Scholarship application submittted successfully"}

        return Response(response)


class AdminApproveScholarShip(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScholarshipSerializer
    permisssion_classes = (IsStaff, )
    lookup_field = 'pk'

    def get_queryset(self):

        user = self.request.user

        # if the user is an applictant, he/she can only see her own application
        if user.role == 'AP':
            return Scholarship.active_objects.for_applicant(applicant=user)

        return Scholarship.objects.all()

    def update(self, request, *args, **kwargs):

        user = request.user
        approve = request.data

        approving_scholarship = self.get_object()

        if approving_scholarship is None:
            return Response({
                "errors": "we did not find the scholarship you are looking for"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(
            approving_scholarship, data=approve, partial=True)
        serializer.is_valid()
        serializer.update(approving_scholarship, approve)
        return Response(serializer.data)


class SponsorList(generics.ListCreateAPIView):
    serializer_class = ScholarshipSerializer
    permission_classes = (IsSponsor, )
    lookup_field = "pk"

    def get_queryset(self):
        return Scholarship.active_objects.approved_scholarships()


class SponsorListUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ScholarshipSerializer
    permission_classes = (IsSponsor, )

    def get_queryset(self):
        return Scholarship.active_objects.all_objects()

    def update(self, request, *args, **kwargs):

        user = request.user
        sponsor_details = request.data

        approving_scholarship = self.get_object()

        if approving_scholarship.is_approved == False:
            return Response({
                "errors": "This scholarship has not been approved yet"
            })

        if approving_scholarship is None:
            return Response({
                "errors": "we did not find the scholarship you are looking for"
            })
        if sponsor_details['sponsor'] == True:
            approving_scholarship.sponsor = user
            payload = {
                "subject": "ScholarShip Acceptance",
                "recipient": [approving_scholarship.applicant],
                "context": {
                    'title': "REGARDING YOUR SCHOLARSHIP APPLICATION",
                    'message': "You scholarship has been approved.Kindly login back in to check more info"
                }
            }
            send_mail(payload['subject'],
                      payload['context']['message'], "no-reply@scholarship.com", payload['recipient'])

            serializer = self.serializer_class(
                approving_scholarship, data=sponsor_details, partial=True)
            serializer.is_valid()
            serializer.update(approving_scholarship, sponsor_details)
            return Response(serializer.data)

        return Response({
            "message": "If you want to sponsor this student kindly pass in sponsor field to be true"
        })
