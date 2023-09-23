"""Write a Python program that converts seconds into days, hours, minutes, and seconds."""

if __name__ == "__main__":
    time = float(input("\n Enter the time in seconds: "))

    days = time / (24*60*60)
    hours = (days % 1) * 24
    minutes = (hours % 1) * 60
    seconds = (minutes % 1) * 60

    print("\n Time given: {} days {} hours {} minutes {} seconds".format(round(days),
                                                                         round(hours),
                                                                         round(minutes),
                                                                         round(seconds))) 