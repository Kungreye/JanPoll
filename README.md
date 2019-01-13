## JanPoll

A simple Django app to conduct Web-based polls.

For each question, visitors can choose between a fixed number of answers.

---
## Quick start




<ol>
 
<li> Clone:

Run `git clone https://github.com/Kungreye/JanPoll.git`</li>


<li> Install Prerequisites:

 `pip install -r requirements` (at top directory)</li>  


<li> Database setup:

Set `DATABASES` in `JanJoll/JanPoll/settings`, according to your preferences.

(refer to <a href="https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES">Django docs</a> for database setting)

<i>Note: make sure the specified DB user has privilege of CREATE DATABASE, since automatic creation of a TEST DATABASE will be needed.</i></li>


<li> Create models

Run `python manage.py migrate`, to create polls models.</li>


<li> Try tests

Run `python manage.py test polls`</li>


<li> Start admin & Create a poll

Run `python manage.py runserver`

Visit `http://127.0.0.1/admin/` to create a poll.</li>


<li> Play with your poll

Visit `http://127.0.0.1/polls/` to participate in the poll.

</li>

</ol>

---
## Reusabilty

If you want to reuse this app in your project:

- Copy the `polls` directory into your project.

- Add `polls` to your `INSTALLED_APPs` of project settings, like:
`INSTALLED_APPS = [..., 'polls.apps.PollsConfig',]`

- Include the polls URLconf in your project urls.py, like:
`path('polls/', include('polls.urls'))`

---
## Demo images

- admin
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/admin.png">
<br>

- admin change list
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/admin_change_list.png">
<br>

- admin change list detail
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/admin_change_detail.png">
<br>

- poll list
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/polls.png">
<br>

- poll detail
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/polls_id.png">
<br>

- poll result
<img src="https://github.com/Kungreye/JanPoll/blob/master/IMGs/polls_id_results.png">
<br>
