# Happy-Journey - A Bus Booking Application
"Happy-Journey" is a responsive modern "Full Stack" busbooking application.

## Tech Stack
**Client:** React Js, Redux

**Server:** Django, Django Reast Framework, Django Channels, Celery

# Features and Functionalities
- User Registration , Login , Logout , OTP Verification through Mail 
- Bus Searching
- Seats Booking
- Cancelling Seats befor departure time
- reminding you by giving notification befor 2 hour of departure time


# Interface

<video width="500" height="300" src="https://github.com/nuruzz9134/Becha-Kena/assets/120547305/d24b8cb6-1ec6-4e42-b870-9638a886b674"></video>

# Deployment
To run the project to your local machine, follows the steps.... 
## frontend-settings....
Before installing and using the Yarn package manager, you will need to have Node.js installed. To see if you already have Node.js installed, type the following command into your local command line terminal:

```bash
  node -v
```
install yarn package manager
```bash
  yarn install
```
to start yarn
```bash
  cd Happy_Journey
  cd bookinginterface
  yarn start
```
Other dependencies are...
```bash
  yarn add react@^18.2.0
  yarn add react-redux@^8.1.2
  yarn add @reduxjs/toolkit@^1.9.5
  yarn add axios@^1.5.0
  yarn add react-icons@^4.8.0
```


## backend-settings....
All dependencies are...
```bash
  pip install Django==4.1.6
  pip install djangorestframework==3.14.0
  pip install djangorestframework-simplejwt==5.2.2
  pip install channels==4.0.0
  python -m pip install -U 'channels[daphne]==4.0.0'
  pip install django-cors-headers==3.13.0
  pip install channels-redis==4.1.0
  pip install celery==5.2.7
  pip install django-celery-beat==2.5.0
  pip install django-celery-results==2.5.0
```
