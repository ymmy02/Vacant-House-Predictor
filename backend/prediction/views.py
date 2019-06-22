from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from PIL import Image
from .serializers import HouseImageSerializer
from .predictor import predict

class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'

class PredictionView(APIView):
    parser_class = (ImageUploadParser,)

    def post(self, request, *args, **kwargs):
        house_image_serializer = HouseImageSerializer(data=request.data)
        # house_image_serializer.save()
        if house_image_serializer.is_valid():
            pil_image = Image.open(request.data['image']).convert('RGB')
            occupied_pct, vacant_pct = predict(pil_image)
            return Response({"occupied": occupied_pct, "vacant": vacant_pct})
        else:
            return Response(house_image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
