import json
import os
import hmac
import hashlib
import time
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from decouple import config


SLACK_BOT_TOKEN = config('SLACK_BOT_USER_TOKEN', default=None)
SLACK_SIGNING_SECRET = config('SLACK_SIGNING_SECRET', default=None)

Client = WebClient(token=SLACK_BOT_TOKEN)


@method_decorator(csrf_exempt, name='dispatch')
class Events(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'})

    def post(self, request, *args, **kwargs):
        timestamp = request.headers.get('X-Slack-Request-Timestamp')
        if abs(time.time() - int(timestamp)) > 60 * 5:
            return HttpResponse(status=403)

        sig_basestring = f"v0:{timestamp}:{request.body.decode('utf-8')}"
        print(sig_basestring)
        my_signature = "v0=" + hmac.new(
            SLACK_SIGNING_SECRET.encode(),
            sig_basestring.encode(),
            hashlib.sha256
        ).hexdigest()
        slack_signature = request.headers.get('X-Slack-Signature')
        print(slack_signature, my_signature)
        if not hmac.compare_digest(my_signature, slack_signature):
            return HttpResponse(status=403)

        event_data = json.loads(request.body)
        if event_data.get('type') == 'url_verification':
            return JsonResponse({'challenge': event_data.get('challenge')})

        if 'event' in event_data:
            event = event_data['event']
            if event.get('type') == 'message' and 'bot_id' not in event:
                channel = event['channel']
                user = event['user']
                text = event.get('text', '')
                if 'hi' in text.lower():
                    try:
                        Client.chat_postMessage(channel=channel, text=f"Hi <@{user}> :wave:")
                    except SlackApiError as e:
                        print(f"Error Sending Message: {e.response['error']}")
        return HttpResponse(status=200)
