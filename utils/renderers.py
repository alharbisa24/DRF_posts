from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        response = renderer_context.get('response')

        if response.status_code >= 400:
            return super().render({
                "success": False,
                "message": "Error occurred",
                "data": None,
                "errors": data
            }, accepted_media_type, renderer_context)

        return super().render({
            "success": True,
            "message": "Request successful",
            "data": data,
            "errors": None
        }, accepted_media_type, renderer_context)
