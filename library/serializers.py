from rest_framework import serializers

from library.models import News, Documents, EventScenarios, WorkPlan, CalendarSignificantDates, Competitions, \
    RegulatoryDocuments, ProfessionalPublications, HistoryLibrarianship, Certification, MethodicalRecommendations


class NewsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера News """

    class Meta:
        model = News
        fields = "__all__"


class DocumentsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера Documents """

    class Meta:
        model = Documents
        fields = "__all__"


class EventScenariosSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера Documents """

    class Meta:
        model = EventScenarios
        fields = "__all__"


class WorkPlanSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера Documents """

    class Meta:
        model = WorkPlan
        fields = "__all__"


class CalendarSignificantDatesSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера CalendarSignificantDates """

    class Meta:
        model = CalendarSignificantDates
        fields = "__all__"


class CompetitionsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера Competitions """

    class Meta:
        model = Competitions
        fields = "__all__"


class RegulatoryDocumentsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера RegulatoryDocuments """

    class Meta:
        model = RegulatoryDocuments
        fields = "__all__"


class ProfessionalPublicationsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера ProfessionalPublications """

    class Meta:
        model = ProfessionalPublications
        fields = "__all__"


class HistoryLibrarianshipSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера HistoryLibrarianship """

    class Meta:
        model = HistoryLibrarianship
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера Certification """

    class Meta:
        model = Certification
        fields = "__all__"


class MethodicalRecommendationsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллера MethodicalRecommendations """

    class Meta:
        model = MethodicalRecommendations
        fields = "__all__"