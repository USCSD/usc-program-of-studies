# USC Program of Studies

Hi! If you are reading this, then you probably need to maintain this software, or to change something. Good luck! I'll try to help you out as much as possible.

Hopefully you are familiar with the current system, both from the teacher/admin page and from the student experience.

I recommend reading through the whole README to understand how the code works, what the dependencies are, and how to build and deploy.

## Structure

This software is split into two parts. The frontend, which is written in Vue 3 (was Vue 2, but I migrated it), and the backend, which is written in Django and Python. The frontend handles what the student sees, and the backend handles the data as well as the admin page.

### Backend

Now for some more details about the backend. The backend stores all information in a SQLite 3 database. There are commands that can import data into the database, but they are essentially useless because the data has changed so much over the years.

There is also a file upload place (in the `media` folder) for hosting PDFs that students may need to see.

There are two main parts of the backend. The API (seen in the `api` folder)
