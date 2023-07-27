# fn

```
curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh

fn start

fn list contexts

fn use context default

// To use Fn for local development, set the registry to an arbitrary value
fn update context registry fndemouser

//To use Fn for normal development, set the registry to your Docker Hub user name
fn update context registry your-docker-hub-user-name

```


# fn - Python

```
//The --runtime option is used to indicate that the function we’re going to develop will be written in Python

fn init --runtime python pythonfn

//it will create a pythonfn directory

func.py
- contains your actual Python function is generated along with several supporting files



func.yml

-  schema_version–identifies the version of the schema for  this function file. Essentially, it determines which fields are present in func.yaml.
-  name–the name of the function. Matches the directory name.
-  version–automatically starting at 0.0.1.
-  runtime–the name of the runtime/language which was set based on the value set in --runtime.
-  memory–The max memory size for a function in megabytes.
-  entrypoint–the name of the executable to invoke when your function is called


requirements.txt
– specifies all the dependencies for your Python function

```

```
fn create app pythonapp

fn --verbose deploy --app pythonapp --local

fn list apps

fn list functions pythonapp

```

```
// Invoke your Deployed Function
fn invoke pythonapp pythonfn

// Getting a Function’s Invoke Endpoint

fn inspect function pythonapp pythonfn
curl -X "POST" -H "Content-Type: application/json" http://localhost:8080/invoke/01DJRP8FT8NG8G00GZJ0000002

```







# postgres
```
sudo apt install postgresql
psql -h localhost -p 5432 -U permify -d permify

```



# Permify Schemas

```
entity user {}

entity group {

      relation member @user
      relation admin @user
      relation moderator @user

      action create = member
      action join = member
      action leave = member
      action invite_to_group = admin
      action remove_from_group = admin or moderator
      action edit_settings = admin or moderator
      action post_to_group = member
      action comment_on_post = member
      action view_group_insights = admin or moderator

}

entity post {

      relation owner @user
      relation group @group
      action view_post = owner or group.member
      action edit_post = owner or group.admin
      action delete_post = owner or group.admin

      permission group_member = group.member

}

entity comment {

      relation owner @user
      relation post @post

      action view_comment = owner or post.group_member
      action edit_comment = owner
      action delete_comment = owner


}

entity like {

      relation owner @user
      relation post @post

      action like_post = owner or post.group_member
      action unlike_post = owner or post.group_member
}

entity poll {

      relation owner @user
      relation group @group

      action create_poll = owner or group.admin
      action view_poll = owner or group.member
      action edit_poll = owner or group.admin
      action delete_poll = owner or group.admin
}

entity file {

      relation owner @user
      relation group @group


      action upload_file = owner or group.member
      action view_file = owner or group.member
      action delete_file = owner or group.admin
}

entity event {

      relation owner @user
      relation group @group

      action create_event = owner or group.admin
      action view_event = owner or group.member
      action edit_event = owner or group.admin
      action delete_event = owner or group.admin
      action RSVP_to_event = owner or group.member
}
```


