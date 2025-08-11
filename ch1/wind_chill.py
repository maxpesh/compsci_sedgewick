import sys

wind_temp: float = float(sys.argv[1])
wind_speed: float = float(sys.argv[2])

wind_chill: float = 35.74 + 0.6215 * wind_temp + (0.4275 * wind_temp - 35.75) * wind_speed ** 0.16
print(f'Wind temperature = {wind_temp:.1f} ℉')
print(f'Wind speed = {wind_speed:.1f} mph')
print(f'Wind chill = {wind_chill:.1f} ℉')
