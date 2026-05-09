from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Details



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_details(request):

    details = Details.objects.all()

    data = []

    for i in details:
        data.append({
            'id': i.id,
            'name': i.name,
            'age': i.age,
            'image': i.image.url if i.image else None,
            'created_at': i.created_at,
        })

    return Response(data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_details(request):

    name = request.data.get('name')
    age = request.data.get('age')
    image = request.FILES.get('image')

    details = Details.objects.create(
        name=name,
        age=age,
        image=image
    )

    return Response({
        'message': 'Data created successfully',
        'id': details.id,
        'name': details.name,
        'age': details.age,
        'image': details.image.url if details.image else None,
        'created_at': details.created_at,
    })


@api_view(['PUT'])
def update_details(request, id):

    try:
        details = Details.objects.get(id=id)
    except Details.DoesNotExist:
        return Response({"error": "Data not found"})

  
    name = request.data.get('name')
    age = request.data.get('age')

    if not name or not age:
        return Response({"error": "name and age are required in PUT"})

    details.name = name
    details.age = age


    if request.FILES.get('image'):
        details.image = request.FILES.get('image')

    details.save()

    return Response({
        "message": "Updated successfully",
        "name": details.name,
        "age": details.age,
        "image": details.image.url if details.image else None
    })



@api_view(['PATCH'])
def patch_details(request, id):

    try:
        obj = Details.objects.get(id=id)
    except Details.DoesNotExist:
        return Response({"error": "not found"})

    if 'name' in request.data:
        obj.name = request.data['name']

    if 'age' in request.data:
        obj.age = request.data['age']

    if request.FILES.get('image'):
        obj.image = request.FILES['image']

    obj.save()

    return Response({
        "id": obj.id,
        "name": obj.name,
        "age": obj.age,
        "image": obj.image.url if obj.image else None,
        "created_at": obj.created_at
    })



@api_view(['DELETE'])
def delete_details(request, id):

    try:
        details = Details.objects.get(id=id)
        details.delete()

        return Response({"message": "Deleted successfully"})

    except Details.DoesNotExist:
        return Response({"error": "Data not found"})
