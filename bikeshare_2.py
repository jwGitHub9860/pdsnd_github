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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city != "chicago" and city != "new york city" and city != "washington":  # MUST CHOOSE CITY
        city = input("Please choose data from one of the following cities (chicago, new york city, washington): ").lower()

    filter_choice = ""
    while filter_choice != 'month' and filter_choice != 'day' and filter_choice != 'all' and filter_choice != 'none':
        filter_choice = input("Please choose one of the following filters (month, day, all, none): ").lower()

    month = ""  # initializes "month"
    day = ""    # initializes "day"
    if filter_choice == 'month' or filter_choice == 'all':
        # get user input for month (all, january, february, ... , june)
        while month != "january" and month != "february" and month != "march" and month != "april" and month != "may" and month != "june":
            month = input("Please choose one of the following month options (january, february, march, april, may, june): ").lower()
    if filter_choice == 'day' or filter_choice == 'all':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        while day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday":
            day = input("Choose a day of the week (monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()

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
    df = pd.read_csv(CITY_DATA[city])  # load data file into a dataframe

    df['Start Time'] = pd.to_datetime(df['Start Time'])     # converts string to DateTime object (ex. String: 2001-12-24 12:38 ---> DateTime: 2001-12-24 12:38:00)

    df['month'] = df['Start Time'].dt.month  # creates new column containing months of 'Start Time'
    df['day'] = df['Start Time'].dt.weekday_name     # creates new column containing weekdays of 'Start Time'

    if month != "":     # if NO filters
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = month_list.index(month) + 1   # obtains number corresponding to month
        df = df[df['month'] == month]  # filters by month

    if day != "":   # if NO filters
        df = df[df['day'] == day.title()]  # filters by day: produces weekday name & capitalizes first letter of weekday

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'].value_counts()
    most_common_month = df['month'].mode()[0]   # finds most common month
    print("Most Common Month:", most_common_month)

    # display the most common day of week
    df['day'].value_counts()
    most_common_day = df['day'].mode()[0]   # finds most common day of week
    print("Most Common Day of the Week:", most_common_day)

    # display the most common start hour
    df['Start Hours'] = df['Start Time'].dt.hour  # creates new column holding "Start Hours"
    df['Start Hours'].value_counts()
    most_common_start_hour = df['Start Hours'].mode()[0]   # finds most common start hour
    print("Most Common Start Hour:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()



    # display most commonly used start station
    #common_start_section = pd.dat
    df['Start Station'].value_counts()
    commonly_used_start_station = df['Start Station'].mode()[0]   # finds most common start station
    print("Most Common Start Station:", commonly_used_start_station)

    # display most commonly used end station
    df['End Station'].value_counts()
    most_commonly_used_end_station = df['End Station'].mode()[0]   # finds most common end station
    print("Most Commonly Used End Station: ", most_commonly_used_end_station)

    # display most frequent combination of start station and end station trip
    df['Combinations'] = df['Start Station'].str.cat(df['End Station'], sep=' and ')    # combines "Start Station" and "End Station" columns
    df['Combinations'].value_counts()
    most_frequent_combination = df['Combinations'].mode()[0]   # finds most common combination
    print("Most Frequent Combination of Start and End Stations: ", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].count()
    print("User Type Count: ", user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].count()
        print("Gender Count: ", gender_count)
    except:
        print("This file has no data about gender.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("Earliest Birth Year: ", earliest_birth_year)
        print("Most Recent Birth Year: ", most_recent_birth_year)
        print("Most Common Year: ", most_common_year)
    except:
        print("This file has no data about birth years.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):   # shows raw data
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    row = 0    # initial row
    column = 5  # initial column
    show_raw_data = input("Do you want to see 5 lines of raw data (y or n): ").lower()
    while show_raw_data != "y" and show_raw_data != "n":
        show_raw_data = input("Please choose one of the following options (y or n): ").lower()
    while show_raw_data == "y":
        if row >= len(df):  # checks if end of raw data is reached
            print("These are the last 5 lines of data.")
            break
        print(df.iloc[row:column])
        show_raw_data = input("Do you want to see another 5 lines of raw data (y or n): ").lower()
        if show_raw_data == "n":
            break
        elif show_raw_data != "y" and show_raw_data != "n":
            while show_raw_data != "y" and show_raw_data != "n":
                show_raw_data = input("Please choose one of the following options (y or n): ").lower()
        else:   # if show_raw_data == "y"
            row += 5
            column += 5

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)   # shows raw data

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
