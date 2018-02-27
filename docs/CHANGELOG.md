# Changelog
All notable changes to this project will be documented in this file.

## 2018-02-26
### Added
- User model to associate with a Report
- Email template in HTML and TXT formats
- Emailing with Gmail server
- Conditional algorithm for determining spikes in sessions and when to notify user by email

### Changed
- Associate reports to users
- Settings.py for emailing

## 2018-02-21
### Added
- Added accounts URL paths
- HTML pages for logged_out, password_reset_complete, password_reset_confirm, password_reset_done, password_reset_email, and password_reset_form.html

### Changed
- Settings: login, email backend, and templates path

## 2018-02-19
### Added
- Added db to .gitignore

## 2018-02-18
### Added
- Login HTML form

## 2018-02-13
### Added
- Report detail HTML page, displaying sessions and countries for a Report

## 2018-02-12
### Added
- List class based view for Reports
- Detail class based view for Reports
- Corresponding HTML templates
- Lots of python dependences for requirements.txt

### Changed
- Updated README for important installation steps
- Put service_account as secret in .gitignore

## 2018-02-11
### Added
- Admin class for the "Report" model
- Base HTML template with sidebar and content wrapper
- Dashboard index page
- Basic CSS styles
- TODO for pyanalytics feature based contribution style

### Changed
- Settings.py timezone, static files, etc default settings

## 2018-02-07
### Added
- Django app as major switch from Flask due to larger libraries, users, and sessions.
- Dashboard app to display GA (Google Analytics) data

### Removed
- Flask App

## 2018-01-30
### Added
- This CHANGELOG file to hopefully serve as an evolving example of a standardized open source project CHANGELOG.
- Emoji to README
- Started work of Flask app for the analytics dashboard

### Removed
- HelloAnalytics_v3.py since pyanalytics will use v4 of google analytics

## 2018-01-28
### Added
- Added working implementation of Google Analytics v4 in python. Sample outputs the number of sessions for the last seven days for the given view.

### Changed
- Refer to original HelloAnalytics toy example as HelloAnalytics_v3.py

## 2018-01-26
### Added
- Start analytics API implementation
- More items to .gitignore: environments, jupyter notebooks, django, and Google API secrets
- Ignored secrets include client_secrets.json and service_account.json
- Setup virtualenv (requirements.txt) for python3

## 2018-01-25
### Added
- Created and expanded the README, CONTRIBUTING guideline, CODE_OF_CONDUCT, and LICENSE
- .gitignore file to ignore .DS_Store for mac users
