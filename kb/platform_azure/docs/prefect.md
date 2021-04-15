# Prefect

## Tokens
### 1. Runner token (do this once)
```
prefect auth create-token -n TOKEN_NAME -s RUNNER
```
### 2. User token (per user)
Note that this is currently not working -- create and use a tenant token instead.

## Project
`prefect create project "velux"`

## Docker Agent
### 1. Set up the VM
#### 1.1 Create the VM
```
az vm create \ 
--resource-group myResourceGroup \ 
--name myVM \ 
--image UbuntuLTS \ 
--admin-username ubuntu \ 
--generate-ssh-keys
```
Save the ssh keys into `~/.ssh`, then `ssh` into the instance and to continue the setup:
`ssh ubuntu@VM_PUBLIC_IP -i %USERPROFILE%/.ssh/SSH_KEY_NAME.pem`
#### 1.2 Install & set up Docker
```
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# execute docker commands without sudo
sudo groupadd docker
sudo usermod -aG docker $USER  

# reload groups inplace so we don't have to relog
newgrp docker

# start Docker on startup
sudo systemctl enable docker  

# reload for good measure
sudo systemctl daemon-reload
sudo systemctl restart docker
```
#### 1.3 Log in to Docker
Note that for GitHub registry, user is the GitHub username, and password is a GitHub personal access token (make sure to [create a new token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token#creating-a-token) for the prefect agent).
```
export REGISTRY_URL=docker.pkg.github.com
export DOCKER_USER=YOUR_DOCKER_USER
export DOCKER_PASSWORD=YOUR_DOCKER_PASSWORD
docker login $REGISTRY_URL -u $DOCKER_USER -p $DOCKER_PASSWORD
```
#### 1.4
Add a Prefect Secret with your GitHub token. This token will be used by the agent to pull the latest flow version from GitHub.
[guide](https://docs.prefect.io/orchestration/concepts/secrets.html#setting-cloud-secrets)

#### 1.5
Update the `github_token` secret in Prefect UI to the new token.

#### 1.6 Install pip & prefect
```
sudo apt install python3-pip
pip3 install prefect[all]
```
Relog so that Ubuntu can find the prefect script.

#### 1.6 Run the Prefect Agent
We use `> /dev/null 2>&1 &` to run it as a daemon process.
```
prefect agent docker start -t RUNNER_TOKEN -n velux -l velux > /dev/null 2>&1 &
```

## Resources
- https://towardsdatascience.com/serverless-data-pipelines-made-easy-with-prefect-and-aws-ecs-fargate-7e25bacb450c#289a
- https://coda.io/@laura-lorenz/streaming-in-prefect-contributor-hq
