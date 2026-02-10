Before doing expanded quiz test, firstly i took the programm for the class and added the next prompt 
"here is the additional criterias
Option 2 - Quiz Game (Expanded):

Functions needed:

- load_questions() - creates/returns question list

- ask_question(question, answer) - handles one question

- calculate_grade(score, total) - returns letter grade

- show_results(score, total, grade) - displays final results

- play_quiz() - runs the whole quiz
also could you add timer for one minute for each question and the timer should go on while answerind the question,if the time would run out answer would be not accepted"
And after i received the programm
Project Report: Resilient Weather Monitoring program
Goal: The goal was to develop a Python-based weather application capable of autonomous data retrieval with a built-in "offline-first" fail-safe. The system was required to maintain functionality during internet outages by utilizing the most recent cached data.

Technical Implementation: 1. Data Acquisition: The program utilizes the requests library to interface with the Open-Meteo API, fetching real-time meteorological parameters. 2. Persistence Layer: I implemented a local caching mechanism using the json module. Every successful API call overwrites a local file (weather_cache.json), creating a permanent "last known good" state. 3. Error Handling & Fallback: The core logic is wrapped in a try-except block. If a ConnectionError or Timeout occurs, the system catches the exception and automatically re-routes the data stream to pull from the local cache instead of the cloud. 4. Automation: A while True loop combined with the time module enables the program to refresh its data automatically at set intervals without user intervention.

Conclusion: The resulting application demonstrates a robust approach to network dependency, ensuring that critical information remains accessible regardless of connectivity status.

Would you like me to add a section on how to handle potential "data corruption" in the cache file as an extra layer of security?
