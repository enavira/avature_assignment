# Prepare

Build the external JobberwockyExteneralJobs docker image.
command need to run in the repo root of each project or use -f and dockerfile path.

```
$ docker build . -t avatureexternaljobs
```

Build the assignment application docker image as well.

```
$ docker build . -t avaturejobs
```

# deploy

Once you have the images are ready use the docker-compose file created to deploy the services.

```
$ docker-compose up -d
```
