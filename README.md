# Installation

## Installing the template is easy, you don't really have to do much:

```bash
django-admin.py startproject --template='~/project_template' --extension py,yaml,md <project_name>
```

## After installation, you need to change the following:
* Change this README.
* Customize the `.env` file.
* Add your domain in `settings.py`'s `ALLOWED_HOSTS`.

## Installing apps.
```bash
cd <project_name>
python manage.py startapp --template='~/app_template' <app_name>
```
---

## Contributing

If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### How to make a clean pull request

Look for a project's contribution instructions. If there are any, follow them.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- ...
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

# Contributors
```json
{
  "AdityaBhalsod":{
    "repositorie": "https://github.com/AdityaBhalsod/django-rest-api-template",
    "email":"adityabhalsod99@gmail.com"
  }
}
```

## #TODO:
1. Unit-testcase. (if possible)
1. Docker support.
2. Multiple storage support. (GCP/AWS/AZURE)
3. Heroku support.
4. Digital ocean support.
5. Multiple environment support. (Settings)
6. Django celery support.
7. All auth support. (ex: Google, facebook.. etc)
