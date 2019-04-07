
from django.http import Http404

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from .serializers import MenuSectionSerializer
from .models import MenuSection


class SectionList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        response = {}
        section = MenuSection.objects.all()
        serializer = MenuSectionSerializer(section, many=True)
        response['MenuSection'] = serializer.data
        return Response(response)

    def put(self, request, format=None):
        serializer = MenuSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SectionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object_by_id(self, pk):
        try:
            return MenuSection.objects.filter(id=pk)
        except MenuSection.DoesNotExist:
            raise Http404

    def get_object_by_name(self, name):
        try:
            return MenuSection.objects.filter(name=name)
        except MenuSection.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        response = {}
        section = self.get_object_by_id(pk)
        serializer = MenuSectionSerializer(section, many=True)
        response['MenuSection'] = serializer.data
        return Response(response)

    def post(self, request, pk):
        response = {}

        section = self.get_object_by_id(pk)
        section[0].name = request.data.get('name')
        data = {}
        data['id'] = pk
        data['name'] = request.data.get('name')
        serializer = MenuSectionSerializer(section[0], data=data)

        if serializer.is_valid():
            serializer.save()
            response['Success'] = True
            response['MenuSection'] = [serializer.data]
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        section = self.get_object_by_id(pk)
        section.delete()
        response = {'Success': True}
        return Response(response, status=status.HTTP_202_ACCEPTED)
