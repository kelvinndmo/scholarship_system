from django.db.models import QuerySet, Q, Sum


class CustomQuerySet(QuerySet):
    """
    Custom queryset that will be reused by different models.
    It enables soft delete and precise filtering, (ie to get all
    property that has not been soft deleted, simply run:
        Property.active_objects.all_objects()
        )
    """

    def _active(self):
        """Return only objects that haven't been soft deleted."""
        return self.filter(is_deleted=False)

    def all_objects(self):
        """Return all objects that haven't been soft deleted"""
        return self._active()


class ScholarQuerySet(CustomQuerySet):
    """ queryset to be used for the scholarship model """

    def for_applicant(self, applicant):
        """ return only for the applicants """
        return self._active().filter(applicant=applicant)

    def unapproved_scholarships(self):
        """ return a list of unapproved scholarships """

        return self._active().filter(is_approved=False)

    def get_unapproved_scholarhip(self, scholarship_id):
        """ get a list of unapproved scholarships """
        return self.unapproved_scholarships().filter(pk=scholarship_id).first()

    def approved_scholarships(self):
        """ return approved scholarships """
        return self._active().filter(is_approved=True)
