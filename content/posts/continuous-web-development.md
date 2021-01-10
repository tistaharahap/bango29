+++
author = "Batista Harahap"
categories = ["flask", "flask-assets", "python", "jenkins", "continuous integration", "defensive programming"]
date = 2014-09-22T05:38:12Z
description = ""
draft = false
slug = "continuous-web-development"
tags = ["flask", "flask-assets", "python", "jenkins", "continuous integration", "defensive programming"]
title = "Continuous Web Development with Flask & Jenkins"

+++


We've all heard of [Continuous Integration (CI)](http://en.wikipedia.org/wiki/Continuous_integration). This blog post is a practical example of the topic with web development in Python and CI with Jenkins. A bit of [Test Driven Development (TDD)](http://en.wikipedia.org/wiki/Test-driven_development) is practiced. Ultimately it's the reader's choice to figure out what's right your themselves.

## Why CI?

The idea is to create a process of which in practice builds foundation for software. A safety net to catch defects early is part of the side effect, localizing complex systems into micro parts and test them to ensure quality over time.

It's great for any pragmatists. Gives you a virtual sense of protection against bad & smelly codes.

> It's tested or it's broken

No matter how good your tests are, you still can't outrun bad design decisions. 

Tests are derived from design decisions. It's impossible to make it work perfect the first time, tests can be considered as battles. The more battles you won, the greater the chances of winning the war.

Jenkins is there to make sure codes will always work on vanilla environments out of the box. Yes configurations are necessary evils. A great hat tip is to keep configurations separate from codes.

## Objectives

What I wanna do is to extend both an idea and an implementation written by [Aria Rajasa](https://twitter.com/rajasa). He wrote a client to interface on an Online Banking frontend. It was necessary for him to check on it regularly without all the fuzz.

The codes are written in PHP. I decided to clone it and build a Python equivalent with CI and best practices in mind. As of this writing, it's still an ongoing effort.

What the codes will do is to automatically retrieve the latest mutation history of your bank account. An HTML frontend will then display the results.

It was supposed to be a weekend project but I learned a thing or two on how to structure Flask projects more efficiently. Being a small and loose web framework, engineers can get lost with their separation of concerns.

A lot of the implementations are inspired from Rails. I despise the language but I love the separation of concerns brought up by Rails. And _conventions over configurations_ is also neat.

## Recipe

These are the building blocks for this project:

- Python 2.7.x - [link](https://www.python.org/)
- Flask 0.10 - [link](http://flask.pocoo.org)
- Jenkins 1.580 - [link](http://jenkins-ci.org)
- Git SCM - [link](http://git-scm.com)
- Github - [link](https://github.com)
- Glowing Octo Tyrion - [link](https://github.com/tistaharahap/glowing-octo-tyrion)

## Git

Before anything else, `git` is the most important topic. My remotes always have these branches:

- `develop`
- `release`
- `master`

Some remotes does not have the `release` branch yet. The branch is only pushed if an actual release is ready.

### Flow

The `develop` branch is where I merge different local (and remote if applicable) `feature/*` branches. A typical vanilla `git` repo will likely look like below.

```bash
$ git init
$ vim README.md
$ vim .gitignore
$ git add README.md .gitignore
$ git commit -m "initial commit" .
$ git remote add origin git@github.com:tistaharahap/some_project.git
$ git push origin master
$ git checkout -b develop
```

After pushing the initial commit to the `master` branch, immediately switch to the `develop` branch. Then set up the basic structure of the project. After I am done, I switch to a `feature` branch to start working.

```bash
# Let's say that I wanna write some codes for the login feature
$ git checkout -b feature/auth

# When I'm done with the feature, I commit and merge it with develop branch
$ git commit -m "Add login feature" .
$ git checkout develop
# Pull latest changes from remote first
$ git pull origin develop
# Merge with feature/auth
$ git merge --no-ff feature/auth

# Let's do another feature: user profile
$ git checkout -b feature/user_profile
# Done
$ git commit -m "add user profile controller" .
$ git checkout develop
$ git pull origin develop
$ git merge --no-ff feature/user_profile

# Logout
$ git checkout feature/auth
# The last time I was here, things have been progressing
$ git merge --no-ff develop
# Do my thing and commit
$ git commit -m "add logout to auth" .
$ git checkout develop
$ git pull origin develop
$ git merge --no-ff feature/auth
```

At the end of a sprint, I would want a `release` branch for QA to test what I've been working at.

```bash
# Sync local develop branch with remote
$ git checkout develop
$ git pull origin develop
$ git checkout -b release
$ git merge --no-ff develop
$ git push origin develop
$ git push origin release

# QA says the logout feature is buggy
$ git checkout feature/auth
# Do my work and commit
$ git commit -m "fix buggy logout" .
# Checkout release and merge the changes
$ git checkout release
$ git pull origin release
$ git merge --no-ff release
```

If you see at the last 2 steps above, I checked out and merged to the `release` branch after QA's report of a buggy feature. As long as the QA process is going on, do not merge anything to `develop` that is not a part of that release cycle.

When QA has given the go ahead, it's time to merge to the `master` branch.

```bash
# Sync local with remote master branch
$ git checkout master
$ git pull origin master

# Merge release with master and tag a version
$ git merge --no-ff release
$ git tag v0.1.0
$ git push --tags origin master

# Merge back to develop branch
$ git checkout develop
$ git pull origin develop
$ git merge --no-ff master
```

This flow is inspired from [here](http://nvie.com/posts/a-successful-git-branching-model/). The `release` branch strategy is the only difference.

## Flask

Flask is a micro yet powerful web framework. It is definitely not for anyone who wants structure. Being micro, Flask does not try to solve all the problems of a web framework. It simply wants to be a micro framework and do it great.

Structure is key to a successful Flask project. My weekend is spent setting up solid structures with tested codes.

```
glowing-octo-tyrion
|__ app
|__ __ config
|__ __ controllers
|__ __ errors
|__ __ __ __init__.py
|__ __ __ errors.py
|__ __ helpers
|__ __ services
|__ __ __init__.py
|__ static
|__ __ coffee
|__ __ css
|__ __ js
|__ __ out
|__ templates
|__ tests
|__ __ helpers
|__ __ __init__.py
|__ __ base_test.py
|__ .gitignore
|__ README.md
|__ deps
|__ start
```

The structure above is revolving that will eventually be a boilerplate.

### Testing

Let's take an example from the Glowing Octo Tyrion project.

We have 3 helpers: `app_helper.py`, `args_helper.py` and `yaml_helper.py`. The helpers is matched with these test classes: `app_helper_test.py`, `args_helper_test.py` and `yaml_helper_test.py`.

```
|__ app
...
|__ __ helpers
|__ __ __ __init__.py
|__ __ __ app_helper.py
|__ __ __ args_helper.py
|__ __ __ yaml_helper.py
...
|__ tests
|__ __ helpers
|__ __ __ __init__.py
|__ __ __ app_helper_test.py
|__ __ __ args_helper_test.py
|__ __ __ yaml_helper_test.py
...
```

Let's examine `yaml_helper.py` and `yaml_helper_test.py`.

```python
# yaml_helper.py
from app.errors import ConfigNotFoundError
import yaml
import os.path


def read_yaml(filename):
    if not os.path.isfile(filename):
        raise ConfigNotFoundError('The file %s is not found' % filename)

    doc = {}

    with open(filename, 'r') as f:
        doc = yaml.load(f)

    return doc
```

I am a proponent of [Defensive Programming](http://en.wikipedia.org/wiki/Defensive_programming) and the error handling above is a reflection of it. Never trust parameters.

In Java a method signature is allowed to throw all kinds of exceptions, this is lacking in Python. We'd never know what kind of exceptions a method can throw. That's why the unit test should also reflect the exceptions as seen below.

```python
# yaml_helper_test.py
from tests.base_test import BaseTest
from app.helpers import read_yaml
from nose.tools import raises, ok_
from app.errors import ConfigNotFoundError


class YamlHelperTest(BaseTest):

    def test_read_yaml(self):
        path = 'app/config/config.yml'
        config = read_yaml(path)

        ok_(isinstance(config, dict),
            msg='Returned object must be an instance of dict')
        ok_(len(config.keys()) > 0,
            msg='Returned object must not be empty')

    @raises(ConfigNotFoundError)
    def test_read_yaml_imaginary_file_should_raises_error(self):
        path = '/a/b/s/c.yml'
        config = read_yaml(path)
```

If you see the test above, it is not as robust as I want it to be. Comparing the `yaml_helper.py` codes, there is still an untested line.

```python
doc = yaml.load(f)
```

After looking into [PyYAML](http://pyyaml.org/wiki/PyYAML)'s source code, the error handling mechanism does not raises any exception upon failing. This is why I can only do so much to test the codes.

However my second test case `test_read_yaml_imaginary_file_should_raises_error` is already defining possible exceptions. In this case, only 1 exception. Just by reading the unit test, supposedly it can and will be the best documentation of an application.

### Configuration

Rails prides itself being a [_convention over configuration_](http://en.wikipedia.org/wiki/Convention_over_configuration) framework. Although the concept is nothing new, Rails brought the concept mainstream. Lending this concept to this project opened up some more niceties.

#### Config Separated From Codes

I love dictionaries, hash maps or anything else you'd want to call it as. Cognitive load becomes cheap. I choose to use [YAML](http://www.yaml.org/) as the configuration files format. It has smart referencing for generic objects and libraries are available in any platform. Python has [PyYAML](http://pyyaml.org/wiki/PyYAML) as mentioned before.

```
|__ app
|__ config
|__ __ config.yml.sample
|__ __ routes.yml
...
```

The file `config.yml.sample` is no much different than what you'd find in any Rails installation. While the `routes.yml` is a convenience over Flask's verbose routing procedures when trying out Flask's getting started tutorial.

```yaml
# routes.yml
home:
    uri: '/'
    methods:
        - GET
    controller: home

about:
    uri: '/about'
    methods:
        - GET
    controller: about
```

Let's now examine the codes to make the routes applicable.

```python
# Excerpts from app/helpers/app_helper.py
def create_routes(app, app_routes=routes):
    if not app_routes:
        raise ConfigNotFoundError('Routes are empty')

    for (k, v) in app_routes.iteritems():
        route = app_routes[k]

        try:
            loaded_mod = load_class('app.controllers.%sController' % route['controller'].title())
        except AttributeError:
            raise ControllerNotFoundError('Class %sController is not found' % route['controller'].title())

        clsmethods = dir(loaded_mod)
        for method in route['methods']:
            method = method.lower()
            if method not in clsmethods:
                raise HTTPMethodNotImplementedError('Class %sController is not implementing method %s' % (route['controller'].title(), method.upper()))

        app.add_url_rule(route['uri'],
                         view_func=loaded_mod.as_view('%s_controller' % route['controller']),
                         methods=route['methods'])
```

The codes above dynamically load proper controllers for each available endpoint read from `routes.yaml` and look for the controller in the `app/controller` directory. For each declared route, the configuration also registers applicable HTTP Methods. This is validated against the controller class and raises `HTTPMethodNotImplementedError ` if it's not satisfied.

This way we are actually enforcing a pattern to be followed upon creating/modifying any endpoints.

Also apparent, by keeping the configuration file in its own DSL, the application side (Python) of the project is prohibited to make direct modifications to its content. In other words, Cowboy moments are a thing of the past.

### Frontend Static Assets

With a dynamic and less verbose routing mechanism, the next subject is to manage frontend static assets. For this project, I have a few static asset formats I want to compile, minify and not worry about versioning at all. This is where [Flask Assets](http://flask-assets.readthedocs.org/en/latest/) came handy.

Flask Assets is a wrapper around [Webassets](http://webassets.readthedocs.org/en/latest/). Here are the file types of my static assets:

- CoffeeScript
- JavaScript
- CSS

Specifically to CoffeeScript, I don't want to execute another watcher each time I do my development. I want my app to be smart enough to see the changes and refresh accordingly.

```python
# Excerpts from app/helpers/app_helper.py
def compile_assets(app, controller_name):
    if not isinstance(controller_name, str):
        raise TypeError('The parameter controller_name must be an instance of String')
    if len(controller_name) == 0:
        raise ValueError('The parameter controller_name must have a length of more than 0')

    assets = Environment(app)

    coffee = compile_asset(controller_name=controller_name,
                           asset_type=ASSET_TYPE_COFFEE)
    css = compile_asset(controller_name=controller_name,
                        asset_type=ASSET_TYPE_CSS)
    js = compile_asset(controller_name=controller_name,
                       asset_type=ASSET_TYPE_JS)

    assets.register('coffee_all', coffee)
    assets.register('css_all', css)
    assets.register('js_all', js)
```

As you can infer from the codes above, the static assets are managed when the routes are created. My own CoffeScript codes will be compiled to JavaScript. The JavaScript assets are third party libraries I'd need. CSS is still plain old CSS. However, should in the future I'd want to add support to [LESS](http://lesscss.org/), I can just add support for it.

```python
# Excerpts from app/helpers/app_helper.py
def compile_asset(controller_name, asset_type):
    eligible_asset_types = [
        ASSET_TYPE_CSS,
        ASSET_TYPE_COFFEE,
        ASSET_TYPE_JS
    ]

    if not isinstance(controller_name, str):
        raise TypeError('The parameter controller_name must be an instance of String')
    if len(controller_name) == 0:
        raise ValueError('The parameter controller_name must have a length of more than 0')
    if not isinstance(asset_type, str):
        raise TypeError('The parameter controller_name must be an instance of String')
    if len(asset_type) == 0:
        raise ValueError('The parameter controller_name must have a length of more than 0')
    if asset_type not in eligible_asset_types:
        raise ValueError('The parameter asset_type is unknown')

    asset_path = '%s/' % asset_type

    static_abs_path = os.path.abspath('static')
    bundle = ['%smain.%s' % (asset_path, asset_type)]

    controller_asset_path = '%s/%s/%s.%s' % (static_abs_path, asset_type, controller_name, asset_type)
    if os.path.isfile(controller_asset_path):
        bundle.append('%s%s.%s' % (asset_path, controller_name, asset_type))

    bundle_params = {
        ASSET_TYPE_COFFEE: {
            'filters': 'coffeescript,rjsmin',
            'out': 'out/a.js'
        },
        ASSET_TYPE_CSS: {
            'filters': 'cssmin',
            'out': 'out/a.css'
        },
        ASSET_TYPE_JS: {
            'filters': 'rjsmin',
            'out': 'b.js'
        }
    }

    asset = Bundle(*bundle,
                   filters=bundle_params[asset_type]['filters'],
                   output=bundle_params[asset_type]['out'])

    return asset
```

The codes above is lending concepts from Java and Rails. From Java, I enjoy having constants as values instead of just values. It's much more readable. While from Rails, the conventions within the codes are very apparent. We assume the assets are located in prescribed directories.

Nearing to the end of the codes before returning is something that is truly Pythonic.

```python
asset = Bundle(*bundle,
               filters=bundle_params[asset_type]['filters'],
               output=bundle_params[asset_type]['out'])
```

Notice that the `Bundle` constructor only accepts multiple unnamed arguments as its files bundle. With Python, I can just put the files into a `List` and prefix a `*` to the `bundle` variable. This means that the `Bundle` constructor should accept all of the list elements within the `bundle` variable as it parameters.

### Error Handling

What is the best way to really know about your application?

Yes certainly debatable. Personally, I feel the best answer for me is to know about all the errors that can and might happen within my application. By doing so, I enable myself a deeper understanding of the application and practice proper Defensive Programming.

For this reason, I have a special package called `errors`.

```
|__ app
...
|__ __ errors
|__ __ __ __init__.py
|__ __ __ errors.py
...
```

```python
class GlowingOctoTyrionError(Exception): pass

class HTTPMethodNotImplementedError(GlowingOctoTyrionError): pass

class ControllerNotFoundError(GlowingOctoTyrionError): pass

class NoEnvSpecifiedError(GlowingOctoTyrionError): pass

class ConfigNotFoundError(GlowingOctoTyrionError): pass
```

Errors or Exceptions is preferrably as detailed as it can be. Grouping errors is ok but not generic errors as it defeats the purpose of error handling. For this, I borrow the concept from Java.

## Jenkins

Jenkins is tightly related with the Git flow mentioned above. A matrix of how this relationship is formed is shown below.

|            | develop | release | master |
|------------|---------|---------|--------|
| dev        |    X    |         |        |
| staging    |         |    X    |        |
| production |         |         |    X   |

The `X` axis defines the Git branches while the `Y` axis shows the environments of which the branches are applied to.

### Plugins

Jenkins comes with an awesome plugins collection supported by a great community of engineers. For our purpose, we will need to have these plugins:

- [Git](https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin)
- [Github](https://wiki.jenkins-ci.org/display/JENKINS/Github+Plugin)
- [ShiningPanda](https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin)
- [Cobertura](https://wiki.jenkins-ci.org/display/JENKINS/Cobertura+Plugin)

More about creating a project on Jenkins later.

#### Git

Obviously the plugin is crucial to use Git. Other than this plugin, make sure you have Git properly installed on your server.

```bash
$ sudo apt-get install git
```

#### Github

Create a personal token and give it permissions to access your repos. Configure this within Jenkins `Configure System` menu.

#### Shining Panda

With this plugin, we can localize our Python projects by using `virtualenv`. On every build, we can also choose to do a vanilla install of the project. Ideal to keep your projects running out of the box.

### Setting Up a Job

Since we're developing in Python, let's make sure that all the necessary dependencies are satisfied.

```bash
$ sudo apt-get install build-essential python-dev python-pip
$ sudo pip install --upgrade pip
$ sudo pip install nose nosexcover
```

Assuming Jenkins is already up and running, let's try setting up a new Jenkins job for the `develop` branch.

![New Jenkins Job](http://bango29.com/content/images/2014/Sep/newitem.png)

![New Job Spec](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-6-26-23-PM.png)

When the dust settles, let's configure the job to suit our needs.

![Configure Job](http://bango29.com/content/images/2014/Sep/configure.png)

If you haven't added Jenkins' public key to your SCM's `authorized_keys`, now's a good time.

![Git Source Code](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-6-54-05-PM.png)

![Github Hook](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-10-00-PM.png)

![Virtualenv Builder](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-13-31-PM.png)

![Virtualenv Shell Script](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-18-40-PM.png)

![JUnit Report](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-21-23-PM.png)

![Cobertura Report](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-25-18-PM.png)

### Result

After all that configuration, this is what becomes of it.

![Result](http://bango29.com/content/images/2014/Sep/Screen-Shot-2014-09-22-at-7-28-27-PM.png)

Feel free to click on the links there. You will find all kinds of useful information about your codes and the unit test.

#### Coverage

Code coverage report is enabled by the Cobertura plugin. With this, you can get an overview of how well your unit testing codes are. This bit decides what kind of weather icons assigned to your job after every build.

---

For this blog post, this is as far as it goes. Next topic will be talking more about deployments.