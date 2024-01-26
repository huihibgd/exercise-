from datetime import datetime
def date_passed(todays_date, scheduled_date):
  todays_date_object=datetime.strptime(todays_date,"%dth %B")
  scheduled_date_object =datetime.strptime(scheduled_date,"%dth %B")

  if todays_date_object > scheduled_date_object:
        print("has passed")
  elif todays_date_object < scheduled_date_object:
        print("yet to pass")
  else:
        if todays_date_object("%d") > scheduled_date_object("%d"):
         print("has passed")
        elif todays_date_object("%d") < scheduled_date_object("%d"):
         print("yet to pass")
        else:
           print("is today") 
date_passed('26th March', '25th March')