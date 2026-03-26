import requests
from rich import print

print("[bold cyan]Example - Latitude: 13.1, Longitude: 103.2 (Battambang Province)[/bold cyan]")

lat = float(input("Enter the Latitude: "))
long = float(input("Enter your Longitude: "))

API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true&timezone=auto"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()

    print("[bold green]----- Weather Fetched Successfully -----[/bold green]")

    current = data['current_weather']
    timezone = data.get('timezone', 'N/A')
    units = data['current_weather_units']

    print(f"[bold blue]Current Timezone is:      [/bold blue][bold yellow]{timezone}  [/bold yellow]")
    print(f"[bold blue]Current Time is:          [/bold blue][bold yellow]{current ['time']}  [/bold yellow]")
    print(f"[bold blue]Current Weather is:       [/bold blue][bold yellow]{current ['temperature']} {units ['temperature']} [/bold yellow]")
    print(f"[bold blue]Current Windspeed is:     [/bold blue][bold yellow]{current ['windspeed']} {units ['windspeed']} [/bold yellow]")
    print(f"[bold blue]Current Winddirection is: [/bold blue][bold yellow]{current ['winddirection']}  [/bold yellow]")

else:
    print("[bold red]----- Failed to fetch weather -----[/bold red]")