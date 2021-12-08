from pprint import pprint
from .Google import Create_Service, convert_to_RFC_datetime
from datetime import datetime

def create_event(name,surname,date,time,phone_number,email,terapia,comments):
    CLIENTE = "1.json"
    API_NAME = "calendar"
    API_VERSION = "v3"
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    service = Create_Service(CLIENTE,API_NAME,API_VERSION,SCOPES)
    calendar_id = 'kliedb8osac6nc7fnbcv3lr438@group.calendar.google.com'
    hour_adjustment = -1
    #Config date time to google config
    date_y = int(date[0:4])
    date_m = int(date[5:7])
    date_d = int(date[8:10])
    
    time_h =int(time[0:2])
    time_m = int(time[3:5])
 

    event_request_body = {
                 "start":{
        "dateTime": convert_to_RFC_datetime(date_y,date_m,date_d,time_h+hour_adjustment,time_m),
        "timeZone": "Europe/London"
        },
                 "end":{
        "dateTime": convert_to_RFC_datetime(date_y,date_m,date_d,time_h+1+hour_adjustment,time_m),
        "timeZone": "Europe/London",
        },
                 "summary":terapia + "     "+ name+ "     " + surname,
                 "description": "Email:"+  email+ " Phone : "+ phone_number ,
                 "colorId":2,
                 "status":"confirmed",
                 "transparency":"opaque",
                 "visibility":"private",
                 "location":"Denmark",
                 "attendees":[{
                         "comment":comments,
                         "email":email,
                         "number":phone_number,
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