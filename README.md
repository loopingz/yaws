# yaws
Yet Another AWS Tools

This tool is to add functionalities that are blocked in PullRequest on official client

```
usage: yaws [-h] [--profile PROFILE] {export,rotate-keys,test}
```

## export

Generate variable for bash so you can export them to environment variable easily

```
eval `yaws --profile MyProfile export`
```

## rotate-keys

It will take your current AWS credentials, create a new credential then remove the old one

```
yaws --profile test rotate-keys
```

