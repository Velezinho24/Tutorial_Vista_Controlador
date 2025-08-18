from abc import ABC, abstractmethod
from django.http import HttpRequest


class ImageStorage(ABC):

    @abstractmethod
    def store(self, request, HttpRequest):
        """
        Store the image from the request.
        :param request: The HTTP request containing the image.
        :param HttpRequest: The type of the HTTP request.
        :return: The path to the stored image.
        """
        pass
    