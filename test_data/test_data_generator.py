from faker import Faker
import random
import json


def generate_random_schedule():
    # Initialize Faker object
    fake = Faker()
    random.seed = 1

    # Create list of event types and times
    event_types = ["Workshop", "Keynote", "Panel", "Networking", "Activity"]
    locations = ["Wondry Dungeons", "Wondry Ground Floor", "Seventh Tile from the Left"]

    # Generate fake schedule where events are in order of date and time
    schedule = []
    for i in range(2):  # 2 days of events
        num_of_events = random.randint(5, 10)  # random number of events per day
        event_times = [
            fake.time(pattern="%H:00:00", end_datetime=None)
            for _ in range(num_of_events)
        ]
        event_times.sort()

        for j in range(num_of_events):
            event_type = random.choice(event_types)
            start_time = event_times[j]
            duration = random.choice([60, 90, 120])  # 60, 90, or 120 minute event
            topic = fake.catch_phrase()
            speaker = fake.name()
            location = random.choice(locations)
            event = {
                "day": i + 1,
                "type": event_type,
                "start time": start_time,
                "duration": duration,
                "topic": topic,
                "speaker": speaker,
                "location": location,
            }
            schedule.append(event)

    # Write schedule to JSON file
    with open(f"test_data/schedule_data.json", "w") as outfile:
        json.dump(schedule, outfile)
