from datetime import datetime
def get_days_until_date(date):
    date = "2023-03-08"
    input_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.now()
    delta = input_date.toordinal() - current_date.toordinal() 
    return delta
print(get_days_until_date("2023-03-08"))


  
   


    


