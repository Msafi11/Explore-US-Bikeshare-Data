import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New york city or Washington?").lower()
        if  city not in CITY_DATA :
            print("Sorry, your response was not valid(Enter " +  "chicago, new york city, washington only --> Please Try again...!).")
            continue
        else:
            break
        
    # get user input for filter or not
    options = ["month","day","both","none"]
    while True:
        filter_option = input("Would you like to filter the data by month, day, both, or not at all? Type" + " none " +"for no time filter.").lower()
        if  filter_option not in options :
            print("Sorry, your response was not valid(Enter " +  "Month/day/both/none only --> Please Try again...!).")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january","february","march","april","may","june","all"]
    if filter_option == "month" :
        day = "all"
        
        while True:
            month = input("Which Month? January, February, March, April, May, June or all ? ").lower()
            if month not in months :
                print("Sorry, your response was not valid(Enter " +  "January, February, March, April, May, June or all only --> Please Try again...!).")
                continue
            else:
                break
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    if filter_option == "day" :
        month = "all"
        while True:
            day = input("Which day? Please type your day (e.g., Sunday).").lower()
            if  day not in days :
                print("Sorry, your response was not valid(Enter " +  "sunday,monday....etc or all only --> Please Try again...!).")
                continue
            else:
                break
                
                
    if filter_option == "both" :
        while True:
            month = input("Which Month? January, February, March, April, May, June or all ? ").lower()
            if month not in months :
                print("Sorry, your response was not valid(Enter " +  "January, February, March, April, May, June or all only --> Please Try again...!).")
                continue
            else:
                break
        while True:
            day = input("Which day? Please type your day (e.g., Sunday).").lower()
            if  day not in days :
                print("Sorry, your response was not valid(Enter " +  "sunday,monday....etc or all only --> Please Try again...!).")
                continue
            else:
                
                break    
    
    if filter_option == "none" :
        month = day = "all"
        

    print('-'*40)
    
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    months = {"january" : 1,
                 "february" : 2,
                 "march" : 3,
                 "april" : 4,
                 "may" : 5,
                 "june" : 6}
     
    
    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month == "all":
        df = df
    else:
        
        df = df[df['Start Time'].dt.month == months[month]]
        
    if day == "all":
        df = df
    else:
        df = df[df['Start Time'].dt.day_name() == day.capitalize()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ["January","February","March","April","May","June"]
    try:
        print("The Most common month: ",months[int(df.mode()['Start Time'].dt.month[0])-1])
    except:
        print("No month data to share")

    # TO DO: display the most common day of week
    try:
        print("The Most common day of week: ",int(df.mode()['Start Time'].dt.dayofweek[0]))
    except:
        print("No day data to share")

    # TO DO: display the most common start hour
    try:
        print("The Most common start hour: ",int(df.mode()['Start Time'].dt.hour[0]))
    except:
        print("No start hour data to share")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        print("The Most common Start Station: ",df.mode()['Start Station'][0])
    except:
        print("No Start station data to share")
    # TO DO: display most commonly used end station
    try:
        print("The Most common End Station: ",df.mode()['End Station'][0])
    except:
        print("No End station data to share")

    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['comb'] = '(' + df['Start Station'] + ' , ' +  df['End Station'] + ')'
        print("The most frequent combination of start station and end station trip: ",df.mode()['comb'][0])
    except:
        print("No station data to share")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        print("The total travel time: ",df['Trip Duration'].sum())
    except:
        print("No travel time data to share")
        

    # TO DO: display mean travel time
    try:
        print("The mean travel time: ",df['Trip Duration'].sum() / df.shape[0])
    except:
        print("No travel time data to share")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print("The counts of user types: ",df['User Type'].value_counts())
    except:
        print("No user types data to share")

    # TO DO: Display counts of gender
    try:
        print("The counts of gender: ",df['Gender'].value_counts())
    except:
        print("No Gender data to share")

    # TO DO: Display earliest, most recent, and most common year of birth.,m.,m
    
    try:
        print("The earliest year of birth : ",int(df['Birth Year'].min()))
        print("The most recent year of birth : ",int(df['Birth Year'].max()))
        print("The most common year of birth : ",int(df.mode()['Birth Year'][0]))
    except:
        print("No year of birth data to share")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def display_data(df):
    view_display = input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ")
    start_loc = 0
    while (view_display.lower() == "yes" and start_loc + 5 <= df.shape[0]):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? Enter yes or no: ")
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
