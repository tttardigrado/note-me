import datetime

def get_date(hour: bool) -> list:
    """Get the current date
    Args:
        hour (bool): select if you want the day or the hour

    Returns:
        list: returns the day or the hour
    """
    if hour: # return hour
        today = datetime.datetime.today()
        # Day/Hour/Minute
        day = today.strftime("%d")
        hour = today.strftime("%H")
        minute = today.strftime("%M")

        return [day, hour, minute]

    else: # returns day
        today = datetime.datetime.now()
        # Day/Month/Year
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        year = str(year)[-2:]
        return [day, month, year]

def get_hour_next() -> list:
    """Get the current date
    Args:
        
    Returns:
        list: returns the day or the hour
    """
    tomorrow = datetime.datetime.now()
    tomorrow = tomorrow + datetime.timedelta(days = 1)
    # Day/Month/Year
    day = tomorrow.strftime("%d")
    hour = tomorrow.strftime("%H")
    minute = tomorrow.strftime("%M")
    return [day, hour, minute]

def get_date_next() -> list:
    """Get the current date
    Args:
        
    Returns:
        list: returns the day or the hour
    """
    tomorrow = datetime.datetime.now()
    tomorrow = tomorrow + datetime.timedelta(days = 1)
    # Day/Month/Year
    day = tomorrow.strftime("%d")
    month = tomorrow.strftime("%m")
    year = tomorrow.strftime("%Y")
    year = str(year)[-2:]
    return [day, month, year]

if __name__ == "__main__":
    print(get_date_next())