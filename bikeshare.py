import time
import pandas as pd
import numpy as np

chicago = pd.read_csv('chicago.csv')
ny = pd.read_csv('new_york_city.csv')
washington = pd.read_csv('washington.csv')

CITY_DATA = { 'chicago': chicago,
              'new york city': ny,
              'washington': washington }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    valid_cities = ['chicago', 'new york city', 'washington', 'all']
    while True:
        city =  str(input("Enter City Name Chicago, New York City or Washington: ")).lower()
        if city in valid_cities:
            print("You entered: {}".format(city).title())
            break
        else:
            print("Entry {} not found, please choose another city.".format(city))

    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month =  str(input("Please enter a month. Choose from 'All, January, February, March, April, May, June': ")).lower()
        if month in valid_months:
            print("You entered: {}".format(month).title())
            break
        else:
            print("Entry {} not found, please choose another month.".format(month))

    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day =  str(input("Please enter a day: ")).lower()
        if day in valid_days:
            print("You entered: {}".format(day).title())
            break
        else:
            print("Entry {} not found, please choose another day.".format(day))

    return city, month, day
    print('-'*40)

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
    df = CITY_DATA[city]

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day is {}".format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular rental time is {}:00".format(popular_hour))

    return(popular_month, popular_day, popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most people start at {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Peopel most often finish their ride at {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + '_'  + df['End Station']
    popular_combination = df['Start to End'].mode()[0]
    print("The most popular start-stop combination is {}.".format(popular_combination))

    return(popular_start_station, popular_end_station, popular_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Rental Time'] = df['End Time'] - df['Start Time']
    # TO DO: display mean travel time
    mean_rental_time = df['Rental Time'].mean()
    print("The average rental duration is {}".format(mean_rental_time))

    return(mean_rental_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = print(df.groupby('User Type')['User Type'].count())

    # TO DO: Display counts of gender
    gender_count = print(df.groupby('Gender')['Gender'].count())

    # TO DO: Display earliest, most recent, and most common year of birth
    yob_erliest = int(df['Birth Year'].min())
    yob_most_recent = int(df['Birth Year'].max())
    yob_most_common = int(df['Birth Year'].mode())

    print("The oldest person to rent a bike was born in {}, the youngest in {} and most people overall in {}.".format(yob_erliest, yob_most_recent, yob_most_common))

    return(yob_erliest, yob_most_recent, yob_most_common)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df):
    """Ask the user if he wants to see a preview of is data"""
    preview =  str(input("Do you want to see a preview of your data? yes - no: ")).lower()
    lower_bound = 0
    upper_bound = 5

    if preview == 'yes':
        # display first 5 lines
        print(df.iloc[lower_bound:upper_bound])
        # Enter a loop to ask the user if hew wants to see additional 5 lines until he enters 'no'
        while True:
            preview =  str(input("Do you want to preview 5 more lines? yes - no: ")).lower()
            if preview == 'yes':
                lower_bound += 5
                upper_bound += 5
                print(df.iloc[lower_bound:upper_bound])
            else:
                # leave the data preview and move on
                print("Alright let\'s head on then!")
                break

    # Proceed when no data preview is being requested
    else:
        print("Alrighty, no data preview it is!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'washington':
            print("Sorry, we have no user information for Washington.")
        else:
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
