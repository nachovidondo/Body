from pprint import pprint
from .Google import Create_Service, convert_to_RFC_datetime


def create_event(name):
    CLIENTE = "credentials.json"
    API_NAME = "calendar"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    service = Create_Service(CLIENTE,API_NAME,API_VERSION,SCOPES)
    calendar_id = 'c8do5koghfaug8f3k7ahj9hh6g@group.calendar.google.com'
    hour_adjustment = -2
    event_request_body = {
                 "start":{
        "dateTime": convert_to_RFC_datetime(2021,11,27,12,0),
        "timeZone": "Europe/London"
        },
                 "end":{
        "dateTime": convert_to_RFC_datetime(2021,11,27,13,0),
        "timeZone": "Europe/London",
        },
                 "summary":name,
                 "description":"",
                 "colorId":5,
                 "status":"confirmed",
                 "transparency":"opaque",
                 "visibility":"private",
                 "location":"Denmark",
                 "attendees":[{
                         "comment":name,
                         "email":"nachovidondo@gmail.com",
                         "responseStatus":"accepted",
                         }]
                 }
    maxAttendees = 5
    sendNotification = True
    sendUpdate = "none"
    supportAttachments = True
    response = service.events().insert(
                calendarId = calendar_id,
                maxAttendees = maxAttendees,
                sendNotifications = sendNotification,
                sendUpdates = sendUpdate,
                supportsAttachments= supportAttachments,
                body = event_request_body,
                ).execute()
    pprint(response)