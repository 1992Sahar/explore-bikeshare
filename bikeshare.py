import time
import pandas as pd
import numpy as np
import datetime as dt

# Create lists for common use throughout program
city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

month_list = ['all', 'january','february',
              'march','april','may','june']

day_list = ['all', 'sunday','monday','tuesday',
            'wednesday','thursday','friday','saturday']


def get_user_input(prompt, choices=['yes','no'], hint=['yes', 'no']):
    """
    Prompt user input given an array of valid choices.

    Args:
        (str) prompt - output message to be shown to user
        (list) choices - array of valid and possible choices
        (list) hint - assistance message showing possible choices when user input is "help"
    Returns:
        (str) choice - user input
    """

    while True:
        choice = input(prompt).lower().strip()
        # Break when choice is valid
        if choice in choices:
            break
        # Exit program when the user input is "end"
        elif choice == 'end':
            raise SystemExit
        # Print possible choices when user input is "help"
        elif choice == 'help':
            print('Options:', end =' ')
            print(*hint, sep=', ')
            continue
        # Print error message when user input is invalid
        else:
            print('Sorry, not a valid input - Type "help" for possible choices')
            continue

    return choice


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Print welcome message and some useful hints
    print('Hello! Let\'s explore some US bikeshare data!'
      '\nHINT: At any time, type:'
      '\n - "end" to exit the program'
      '\n - "help" for possible choices')

    while True:
        # Get user input for city
        city = get_user_input(
            prompt='Which city would you like to explore its data?\n',
            choices=city_data.keys(), hint=city_data.keys())

        # Get user input for wish to apply filters
        if get_user_input(
            prompt='Would you like to specify a month or/and a day?\n') == 'yes':

            # Get user input for month
            month = get_user_input(
                prompt='Which month would you like to explore its data?\n',
                choices=month_list, hint=month_list)

            # Get user input for day of week
            day = get_user_input(
                prompt='Which day of the week would you like to explore its data?\n',
                choices=day_list, hint=day_list)
        else:
            month = 'all'
            day = 'all'

        # Get user input for filter confirmation
        print('The filters you applied:'
              '\n City: {}\n Month: {}\n Day: {}'.format(city, month, day))
        confirmation = get_user_input('Are these filters correct?\n')
        if confirmation == 'yes':
            break
        elif confirmation == 'no':
            print("\nLet's try this again!")
        elif confirmation == 'help':
            choice = 'help'

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

    # Create dataframe and load selected city data
    df = pd.read_csv(city_data[city])

    # Drop unnecessary column
    df.drop(columns='Unnamed: 0', inplace=True)

    # Rename columns for usability purposes
    column_names = ['start_time', 'end_time', 'trip_duration', 'start_station',
                    'end_station','user_type', 'gender', 'birth_year']

    # Handle the different number of columns between datasets
    if len(df.columns) == 6:
        df.columns = column_names[0:6]
    else:
        df.columns = column_names

    # Convert start_time to datetime object
    df.start_time = pd.to_datetime(df.start_time)

    # Create new columns by extracting datetime attributes
    df['month'] = df.start_time.dt.month_name()
    df['dow'] = df.start_time.dt.weekday_name
    df['hour'] = df.start_time.dt.hour

    # Filter according to month and day
    if month != 'all':
        df = df[df.month.str.lower() == month]

    if day != 'all':
        df = df[df.dow.str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is:",
          df.month.mode()[0])

    # display the most common day of week
    print("The most common day of week is:",
          df.dow.mode()[0])

    # display the most common start hour
    print("The most common hour is:",
          df.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is:",
          df.start_station.mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is:",
          df.start_station.mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most frequent start-end stations combination:",
          (df.start_station + ' - ' + df.end_station).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is:",
          df.trip_duration.sum())

    # display mean travel time
    print("The total mean time is:",
          df.trip_duration.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df.user_type.value_counts()
    print('Counts of user types:')
    for i, count in enumerate(user_count):
        print(' {}: {}'.format(user_count.index[i], count))
    print()

    # Display counts of gender if applicable
    if 'gender' in df.columns:
        gender_count = df.gender.value_counts()
        print('Counts of gender:')
        for i, count in enumerate(gender_count):
            print(' {}: {}'.format(gender_count.index[i], count))
        print()

    # Display earliest, most recent, and most common birth years if applicable
    if 'birth_year' in df.columns:
        print("Earliest birth year:",
          int(df.birth_year.min()))
        print("Most recent birth year:",
          int(df.birth_year.max()))
        print("Most common birth year:",
          int(df.birth_year.mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df, bookmark=0):
    """
    Displays raw data upon request by the user

    Args:
        (DataFrame) df - processed dataset
        (int) bookmark - stores index to iterate over rows
    Returns:
        None
    """

    # Get user input for wish to see raw data
    if get_user_input(
        prompt='\nWould you like to see first 5 rows of raw data?\n') == 'yes':

        while True:
            for i in range(bookmark, len(df)):
                print(df.iloc[bookmark:bookmark+5].to_string())
                bookmark += 5

                # Get user input for wish to continue
                if get_user_input('\nWould you like to see the next 5 rows?\n') == 'yes':
                    continue
                else:
                    break
            break

        else:
            pass


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = get_user_input('\nWould you like to restart?\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
