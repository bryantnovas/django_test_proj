import django
django.setup()
import requests
from test_proj.models import User, Profile


def populate_tables():
  r = requests.get('https://randomuser.me/api/?page=3&results=10')
  response = r.json()['results']
  User.objects.all().delete()
  Profile.objects.all().delete()

  for i in response:
    name = i['name']
    email = i['email']
    street_num = i['location']['street']['number']
    street_name = i['location']['street']['name']
    city = i['location']['city']
    state = i['location']['state']
    country = i['location']['country']
    full_address = f'{street_num} {street_name}, {city}, {state}, {country}'
    
    user = User.objects.create(first_name = name['first'], last_name=name['last'])
    profile = Profile.objects.create(user_id=user.id, address=full_address, email=email)

if __name__ == '__main__':
  populate_tables()